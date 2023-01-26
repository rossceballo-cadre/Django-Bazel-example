"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application, FallbackHandler

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

django_app = get_asgi_application()


class DjangoHandler(FallbackHandler):
    def initialize(self, application):
        self.application = application

    async def prepare(self) -> None:
        self.request.path_args = [self.request.path[1:]]

    async def get(self):
        await self.application(self.request)

    async def post(self):
        await self.application(self.request)


def main():
    tornado_app = Application(
        [
            (r".*", DjangoHandler, {"application": django_app}),
        ]
    )
    server = HTTPServer(tornado_app)
    server.listen(8500)
    IOLoop.current().start()


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
    main()
