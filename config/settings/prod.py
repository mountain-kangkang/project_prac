from config.settings.base import *
from dotenv import dotenv_values

ENV = dotenv_values('../../envs/.env.prod')


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-4mf%v393(ixqsc#!3f%@h0ycu#f4vcud&nq8d75it589n-_$3*"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

STATIC_URL = "static/"