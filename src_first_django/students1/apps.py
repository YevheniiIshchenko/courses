from django.apps import AppConfig


class Students1Config(AppConfig):
    name = 'students1'

    def ready(self):
        import students1.signals  # noqa
