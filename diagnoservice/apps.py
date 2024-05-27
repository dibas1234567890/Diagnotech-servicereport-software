from django.apps import AppConfig


class DiagnoserviceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'diagnoservice'

    def ready(self):
        import digidiagno.signals
