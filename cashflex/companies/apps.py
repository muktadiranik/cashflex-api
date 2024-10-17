from django.apps import AppConfig


class CompaniesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cashflex.companies'
    label = 'companies'

    def ready(self):
        from cashflex.companies import signals

        if signals:
            pass
