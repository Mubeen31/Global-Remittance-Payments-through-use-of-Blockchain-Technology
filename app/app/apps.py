from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'app'


    def ready(self):
        from .integrations import toml, MyRailsIntegrations
        from polaris.integrations import register_integrations

        register_integrations(
            toml=toml,
            rails=MyRailsIntegrations()
        )
