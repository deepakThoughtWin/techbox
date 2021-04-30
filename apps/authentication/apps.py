from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    name = 'apps.authentication'

    def ready(self): #method just to import the signals
    	import apps.authentication.signals