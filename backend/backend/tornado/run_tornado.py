import sys
import tornado.httpserver
import tornado.ioloop
import tornado.netutil
import tornado.process
import tornado.web
from asgiref.sync import sync_to_async
from asyncio import AbstractEventLoop
from tornado.platform.asyncio import BaseAsyncIOLoop
from django.core.handlers.asgi import ASGIHandler as ASGIApplication
from backend.handlers.asgi_handler import ASGIHandler
from django.apps import apps
from django.conf import settings
from django.utils.module_loading import import_string
import django
from typing import Any, Dict, List, Optional
from tornado.routing import AnyMatches, Rule
from backend.preload import preload_django_apps

from .application import InstrumentedApplication

DEBUG_SETTINGS = {
    "compiled_template_cache": False,
    "static_hash_cache": False,
    "serve_traceback": True,
}
DEFAULT_ADDRESS = "127.0.0.1"
DEFAULT_PORT = 8000


def setup_django() -> None:
    if not settings.configured:
        settings.configure()

    if not apps.ready:
        django.setup()


def get_routes(asgi_application: ASGIApplication) -> List[Rule]:
    routes: List[Rule] = []
    routes.append(
        Rule(
            AnyMatches(),
            ASGIHandler,
            {"asgi_application": asgi_application},
            "django",
        )
    )

    return routes


def run_tornado(
    protocol: Optional[str] = None,
    address: Optional[str] = None,
    port: Optional[int] = None,
    asgi_application: Optional[ASGIApplication] = None,
    preload: bool = False,
) -> None:
    if not address:
        address = DEFAULT_ADDRESS
    if not port:
        port = DEFAULT_PORT

    sockets = tornado.netutil.bind_sockets(port=port, address=address, reuse_port=True)

    setup_django()

    if not protocol:
        protocol = "http"
    if not asgi_application:
        asgi_application = import_string("django.core.handlers.asgi.ASGIHandler")()
    xheaders = settings.USE_X_FORWARDED_HOST or settings.USE_X_FORWARDED_PORT or False

    routes = get_routes(asgi_application)

    application_settings: Dict[str, Any] = DEBUG_SETTINGS if settings.DEBUG else {}
    tornado_app = InstrumentedApplication(routes, **application_settings)

    http_server = tornado.httpserver.HTTPServer(
        tornado_app,
        protocol=protocol,
        xheaders=xheaders,
        max_buffer_size=268435456,  # 256 MB
    )
    http_server.add_sockets(sockets)

    current_ioloop = tornado.ioloop.IOLoop.current()

    if not getattr(settings, "UNDER_MAINTENANCE", False) and preload:
        # Run via sync_to_async so that preloading is invoked in the same manner as all
        # other django code
        current_ioloop.add_callback(sync_to_async(preload_django_apps))

    if isinstance(current_ioloop, BaseAsyncIOLoop):
        if settings.DEBUG:
            current_ioloop.asyncio_loop.set_debug(True)

        def handle_async_exception(
            loop: AbstractEventLoop, context: Dict[str, Any]
        ) -> None:
            print(exc=context.get("exception", None))

            # XXX - if the exception comes from django (which is the most likely case),
            # the thread executor ends up in an unexpected state and hangs indefinitely
            # when joined in the futures atexit callback. Workaround this by
            # unregistering its atexit callback, allowing all other callbacks to
            # execute as per usual
            # atexit.unregister(getattr(concurrent_futures_thread, "_python_exit"))

            # Service is in a known bad state, so commence shutdown
            current_ioloop.stop()
            sys.exit(1)

        current_ioloop.asyncio_loop.set_exception_handler(handle_async_exception)

    current_ioloop.start()
    current_ioloop.close(all_fds=True)
