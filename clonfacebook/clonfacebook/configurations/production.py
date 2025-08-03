from .base import *
DEBUG:False
ALLOWED_HOSTS = [ 'localhost',	 '3000']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}