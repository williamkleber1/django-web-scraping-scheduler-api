from django.apps import AppConfig


class AutomationscrapperConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'automationScrapper'
    def ready(self):
        from automationScrapper import signals
