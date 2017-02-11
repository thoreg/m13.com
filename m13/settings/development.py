from .base import *

ALLOWED_HOSTS = []
DEBUG = True
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6zu)bs6x#o_3)8(0)^=3!%e)@v#9p^h+m0n%gmws298+%32gnk'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'm13com',
        'USER': 'm13comu',
        'PASSWORD': 't0psecret',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
