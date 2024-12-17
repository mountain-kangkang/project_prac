import os

from config.settings.base import *
from dotenv import dotenv_values, load_dotenv

load_dotenv('../../envs/.env.local')

ENV = dotenv_values('../../envs/.env.prod')

from django.core.management.utils import get_random_secret_key
SECRET_KEY = os.getenv('SECRET_KEY', get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ENV['ALLOWED_HOSTS'].split(',')

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": os.getenv('POSTGRES_HOST'),
        "NAME": os.getenv('POSTGRES_DBNAME'),
        "USER": os.getenv('POSTGRES_USER'),
        "PASSWORD": os.getenv('POSTGRES_PASSWORD'),
        "PORT": os.getenv('POSTGRES_PORT'),
    }
}

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, ".staticfiles")
