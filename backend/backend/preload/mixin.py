from abc import ABC, abstractmethod


class PreloadableAppMixin(ABC):
    @abstractmethod
    def preload(self) -> None:
        """
        When preloading is enabled, the app will preload as necessary to ensure caches
        are warmed prior to sending traffic to the app
        """
