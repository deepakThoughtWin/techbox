from django.apps import AppConfig


class DashboardConfig(AppConfig):
    name = 'apps.dashboard'

    def ready(self): #method just to import the signals
        import apps.dashboard.signals