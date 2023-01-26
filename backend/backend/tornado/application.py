from tornado.web import Application, OutputTransform, RequestHandler, _HandlerDelegate
from typing import Any, List, Type, cast
from tornado.routing import Rule, URLSpec, _RuleList


class InstrumentedApplication(Application):
    def __init__(
        self,
        handlers: List[Rule] = None,
        default_host: str = None,
        transforms: List[Type[OutputTransform]] = None,
        **settings: Any,
    ) -> None:
        if handlers is None:
            handlers = []

        for handler in handlers:
            if handler.target_kwargs.get("route_pattern"):
                continue

            if isinstance(handler, URLSpec):
                handler.target_kwargs["route_pattern"] = handler.regex.pattern

        super().__init__(
            handlers=cast(_RuleList, handlers),
            default_host=default_host,
            transforms=transforms,
            **settings,
        )

    def log_request(self, handler: RequestHandler) -> None:
        """
        Disable the built in logger in favor of structlog
        """
