import os
from os import path
import sys

import dotenv


# Build paths inside the project like this: path.join(BASE_DIR, ...)
BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))

# Load settings from a .env file.
# NOTE: If this file doesn't exist in this repository's root directory,
# you need to create one.
dotenv.load_dotenv('.env')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z2^mu74za+7-j(90&js@5*5jt9x^3vy_5gm_(i%s@m)as%=j$!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'the-clubhouse.herokuapp.com',
    'clubhouse.pizza',
    'localhost',
]

TESTING = len(sys.argv) > 1 and sys.argv[1] == 'test'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'backend.app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = (
    'django.contrib.staticfiles.storage.StaticFilesStorage'
    if TESTING
    else 'whitenoise.storage.CompressedManifestStaticFilesStorage'
)

FRONTEND_DIR = path.join(BASE_DIR, 'frontend')

FRONTEND_INDEX = path.join(FRONTEND_DIR, 'build', 'index.html')

STATICFILES_DIRS = [
    path.join(FRONTEND_DIR, 'build', 'static'),
]

FRONTEND_INDEX = path.join(BASE_DIR, 'frontend', 'build', 'index.html')


# Hackathon clubhouse URL

COCO_CABANA_HANGOUT_URL = os.environ['COCO_CABANA_HANGOUT_URL']
