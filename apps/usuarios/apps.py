from django.apps import AppConfig

class MuestrasConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.usuarios"  # ✅ Asegúrate de que esto coincide con `INSTALLED_APPS`
