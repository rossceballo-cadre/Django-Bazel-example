from http import HTTPStatus
from typing import Any, cast


from tornado.web import RequestHandler


class DisallowHeadRequestsMixin:
    async def head(self, *args: Any, **kwargs: Any) -> None:
        cast(RequestHandler, self).set_status(HTTPStatus.METHOD_NOT_ALLOWED)
        await cast(RequestHandler, self).finish()


class DisallowOptionsRequestsMixin:
    async def options(self, *args: Any, **kwargs: Any) -> None:
        cast(RequestHandler, self).set_status(HTTPStatus.METHOD_NOT_ALLOWED)
        await cast(RequestHandler, self).finish()
