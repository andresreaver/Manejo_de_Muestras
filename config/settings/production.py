import os
from .base import *

ADMIN_ENABLED = False
DEBUG = False
ALLOWED_HOSTS = ["10.26.3.248", "balalaika.app", "localhost", "127.0.0.1"]
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

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

CSRF_TRUSTED_ORIGINS = [
        "https://10.26.3.248",
        "https://balalaika.app",
    ]
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs/django_errors.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

STATICFILES_DIRS = [BASE_DIR / "config/static"]
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "config/staticfiles"

