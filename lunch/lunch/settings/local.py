from .base import *

SECRET_KEY = 'mp!3x633mxozny$)tc)86^^(@r5e(+i%-ybw__!g0!a883%*p8))'
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
