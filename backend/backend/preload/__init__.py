from .mixin import PreloadableAppMixin


def preload_django_apps() -> None:
    from django.apps import apps

    for app_config in apps.get_app_configs():
        if isinstance(app_config, PreloadableAppMixin):
            app_name = getattr(app_config, "verbose_name")
            attributes = {
                "app_name": app_name,
            }
            app_config.preload()
