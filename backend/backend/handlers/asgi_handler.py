from typing import Any, Dict

from django.core.handlers.asgi import ASGIHandler as ASGIApplication
from tornado.web import RequestHandler

from .mixins import DisallowHeadRequestsMixin, DisallowOptionsRequestsMixin

DEFAULT_CHARSET = "utf-8"


class ASGIHandler(
    DisallowHeadRequestsMixin, DisallowOptionsRequestsMixin, RequestHandler
):
    def initialize(self, asgi_application: ASGIApplication) -> None:
        super().initialize()
        self._asgi_application = asgi_application
        self._scope: Dict[str, Any] = {}

    async def get(self, *args: Any, **kwargs: Any) -> None:
        await self.handle_request()

    async def post(self, *args: Any, **kwargs: Any) -> None:
        await self.handle_request()

    async def delete(self, *args: Any, **kwargs: Any) -> None:
        await self.handle_request()

    async def patch(self, *args: Any, **kwargs: Any) -> None:
        await self.handle_request()

    async def put(self, *args: Any, **kwargs: Any) -> None:
        await self.handle_request()

    async def asgi_receive(self) -> Dict[str, Any]:
        return {"body": self.request.body or b"", "type": self._scope.get("type")}

    async def asgi_send(self, data: Dict[str, Any]) -> None:
        data_type = data.get("type")

        if data_type == "http.response.start":
            self.set_status(data["status"])

            # Clear tornado's defaults and defer to the asgi application
            self.clear_header("content-type")
            self.clear_header("server")
            self.clear_header("date")

            for h in data.get("headers", []):
                if len(h) == 2:
                    self.add_header(
                        h[0].decode(DEFAULT_CHARSET), h[1].decode(DEFAULT_CHARSET)
                    )

        elif data_type == "http.response.body":
            data_body = data.get("body")
            if data_body:
                self.write(data_body)

            data_more_body = data.get("more_body", False)
            if not data_more_body:
                self.finish()
        else:
            raise RuntimeError(
                f'Unsupported response type "{data_type}" for ASGI applications'
            )

    async def handle_request(self) -> None:
        # Flatten and encode the headers for the asgi application
        headers = []
        for k in self.request.headers:
            for v in self.request.headers.get_list(k):
                headers.append(
                    (k.encode(DEFAULT_CHARSET).lower(), v.encode(DEFAULT_CHARSET))
                )

        # For now, only handle http and https. Map https to http since ssl termination
        # is handled downstream
        asgi_type = "unknown"
        if self.request.protocol == "http" or self.request.protocol == "https":
            asgi_type = "http"

        self._scope = {
            "client": [self.request.remote_ip, 0],
            "headers": headers,
            "http_version": self.request.version,
            "method": self.request.method,
            "path": self.request.path,
            "query_string": self.request.query.encode(DEFAULT_CHARSET),
            "type": asgi_type,
        }

        await self._asgi_application(self._scope, self.asgi_receive, self.asgi_send)
