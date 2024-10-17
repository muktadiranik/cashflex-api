from django.apps import AppConfig


class CollaboratorsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cashflex.collaborators'

    def ready(self):
        from cashflex.collaborators import signals

        if signals:
            pass
