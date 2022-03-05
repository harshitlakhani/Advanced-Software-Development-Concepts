import os
import django_heroku

from .common import * # NOQA

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ['DB_NAME'],
        "HOST": os.environ['DB_HOST'],
        "USER": os.environ['DB_USER'],
        "PASSWORD": os.environ['DB_PASSWORD'],
    }
}

django_heroku.settings(locals())
