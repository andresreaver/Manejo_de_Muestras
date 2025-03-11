from .base import *

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'gestion_muestras',
        'USER': 'postgres',
        'PASSWORD': 'Admin1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
