import os

from config.settings.base import *
from dotenv import load_dotenv

load_dotenv('../../envs/.env.local')

ENV = load_dotenv('../../envs/.env.local')


# SECURITY WARNING: keep the secret key used in production secret!
from django.core.management.utils import get_random_secret_key
SECRET_KEY = os.getenv('SECRET_KEY', get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

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