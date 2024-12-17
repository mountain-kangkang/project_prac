import os

from config.settings.base import *
from dotenv import dotenv_values

ENV = dotenv_values(BASE_DIR / 'envs/.env.prod')

from django.core.management.utils import get_random_secret_key
SECRET_KEY = ENV['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ENV.get('ALLOWED_HOSTS').split(', ')

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": ENV.get('POSTGRES_HOST'),
        "NAME": ENV.get('POSTGRES_DBNAME'),
        "USER": ENV.get('POSTGRES_USER'),
        "PASSWORD": ENV.get('POSTGRES_PASSWORD'),
        "PORT": ENV.get('POSTGRES_PORT'),
    }
}

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
