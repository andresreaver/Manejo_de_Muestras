import os
from .base import *

DEBUG = False
ALLOWED_HOSTS = ["10.26.3.248"]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("blkpyapp", "nombre_de_tu_bd"),
        "USER": os.environ.get("db_admin", "usuario_bd"),
        "PASSWORD": os.environ.get("PSQL_INSBlk_2024", "contraseña_bd"),
        "HOST": os.environ.get("DB_HOST", "10.26.3.248"),
        "PORT": os.environ.get("DB_PORT", "5432"),
    }
}
