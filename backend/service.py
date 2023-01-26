"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
import sys

from tornado.web import RequestHandler


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")


class HelloHandler(RequestHandler):
    def get(self):
        class Todo:
            def __init__(self, title, name) -> None:
                self.title = title
                self.name = name

        todos = [Todo("hi", "bye"), Todo("5", "4")]
        self.render("templates/todo_list.html", todos=todos)


# def main():


#     # from todo.views import todo_list

#     wsgi_app = get_wsgi_application()

#     container = tornado.wsgi.WSGIContainer(wsgi_app)
#     tornado_app = Application(
#         [
#             ("/todo", HelloHandler),
#             (".*", FallbackHandler, dict(fallback=container)),
#         ]
#     )

#     server = HTTPServer(tornado_app)
#     server.listen(8000)
#     IOLoop.instance().start()
def main() -> None:
    import uvloop  # pylint: disable=import-outside-toplevel
    from tornado.options import options, define

    from backend.tornado.run_tornado import DEFAULT_ADDRESS, DEFAULT_PORT, run_tornado

    define(
        "address",
        group="service",
        default=DEFAULT_ADDRESS,
        help="the address the service binds to",
    )
    define(
        "port",
        group="service",
        type=int,
        default=DEFAULT_PORT,
        help="the port the service listens on",
    )
    define(
        "preload",
        group="service",
        type=bool,
        default=True,
        help="whether or not to warm caches by preloading apps",
    )
    options.parse_command_line()

    # Run the event loop with libuv.
    uvloop.install()
    run_tornado(address=options.address, port=options.port, preload=options.preload)


if __name__ == "__main__":
    from django.conf import settings

    sys.path.append("./backend")
    print(settings.ROOT_URLCONF)
    # print(sys.path)
    main()
