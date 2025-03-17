import os
from .base import *

DEBUG = False
ALLOWED_HOSTS = ["10.26.3.248"]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "blkpyapp",
        "USER": "postgres",
        "PASSWORD": "PSQL-INSBlk.2024",
        "HOST": "10.26.3.248",
        "PORT": "5432",
    }
}
CSRF_TRUSTED_ORIGINS = ["http://10.26.3.248"]

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "config/staticfiles"

