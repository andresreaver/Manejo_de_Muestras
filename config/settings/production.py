import os
from .base import *

DEBUG = False
ALLOWED_HOSTS = ["10.26.3.248"]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("BLKPYAPP_DB_NAME"),
        "USER": os.environ.get("BLKPYAPP_DB_USER"),
        "PASSWORD": os.environ.get("BLKPYAPP_DB_PASSWORD"),
        "HOST": os.environ.get("BLKPYAPP_DB_HOST", "10.26.3.248"),
        "PORT": os.environ.get("BLKPYAPP_DB_PORT", "5432"),
    }
}
CSRF_TRUSTED_ORIGINS = ["http://10.26.3.248"]

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
