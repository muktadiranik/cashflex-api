from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cashflex.core'
    verbose_name = 'Admin'
    

    def ready(self):
        pass
