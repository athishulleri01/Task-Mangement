from os import getenv, path

from dotenv import load_dotenv

from .base import * #noqa

from .base import BASE_DIR

local_env_file = path.join(BASE_DIR, ".envs", ".env.local")

if path.isfile(local_env_file):
    load_dotenv(local_env_file)

DEBUG = True

SITE_NAME = getenv("SITE_NAME")
    

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY =  getenv("DJNAGO_SECRET_KEY","4XeyITfLVx0JYDdGQTcsu3rRWBgdsNn4aUFhqS96s8H_qAuimXs")
# 'django-insecure-$(ub-&=99n=3fw=+@bccj$cjjy*1o)5vck(e(0g)daz2*o6@0u'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost","127.0.0.1","0.0.0.0"]

ADMIN_URL = getenv("DJANGO_ADMIN_URL")


DOMAIN = getenv("DOMAIN")


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(name)-12s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}