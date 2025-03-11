import os
from .base import *

DEBUG = False
ALLOWED_HOSTS = ["10.26.3.248"]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("blkpyapp"),
        "USER": os.getenv("db_admin"),
        "PASSWORD": os.getenv("PSQL_INSBlk.2024"),
        "HOST": os.getenv("10.26.3.248"),
        "PORT": os.getenv("5432"),
    }
}
