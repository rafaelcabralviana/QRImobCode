from django.apps import AppConfig


class MensagensConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "mensagens"

    def ready(self):
        import mensagens.signals
