import os
from .base import *

DEBUG = False
ALLOWED_HOSTS = ["10.26.3.248"]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "blkpyapp",
        "USER": "db_admin",
        "PASSWORD": "PSQL_INSBlk.2024",
        "HOST": "10.26.3.248",
        "PORT": "5432",
    }
}
