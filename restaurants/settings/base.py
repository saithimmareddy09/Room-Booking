"""
Django settings for restaurants project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from typing import Any
from pathlib import Path
from decouple import config
import logging.config
import yaml
import cloudinary
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))




# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = config('restaurants-appkey')
SECRET_KEY = config('restaurants-appkey',default='django-insecure-+m1c0%5mwr5tp^r0*v_*orsj^ay059_sx3mfkt@a32(p0(j0!+')

with open(os.path.join(BASE_DIR, '../config/logging_app.yml'), 'rt') as f:
    LOGGING = yaml.safe_load(f.read())
logging.config.dictConfig(LOGGING)

# SECURITY WARNING: don't run with debug turned on in production!


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #name of the type of databse in this case it  is mysql
        'NAME': 'restaurants', #Name of the database
        'USER': 'root', #Name of the mysql user
        'PASSWORD': 'Sai481309@', #Password of the mysql
        'HOST':'localhost', # host of the sql 
        'PORT':'3306', # Running Port
    }
}


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Local apps
    'menu_app',
    'rest_framework',
    'rest_framework_simplejwt',
    'cloudinary',
    'django_otp',
    'django_celery_results',
    'django.contrib.humanize',
    'mathfilters',
    'rest_framework.authtoken',
    'lodging_app',
    'django_htmx',
]

LOGIN_URL = '/user_api/'

# Media files (user-uploaded files) storage location
MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'media'))
MEDIA_URL = '/media/'


AUTH_USER_MODEL = 'menu_app.CustomUser'
# Twilio configurations
OTP_TWILIO_ACCOUNT_SID =  config('OTP_TWILIO_ACCOUNT_SID')
OTP_TWILIO_AUTH_TOKEN =  config('OTP_TWILIO_AUTH_TOKEN')
OTP_TWILIO_FROM_NUMBER = config('OTP_TWILIO_FROM_NUMBER')


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
DEBUG = True

ALLOWED_HOSTS =['*']

ROOT_URLCONF = 'restaurants.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
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

WSGI_APPLICATION = 'restaurants.wsgi.application'
SESSION_COOKIE_AGE = 86400
SIMPLE_JWT: Any = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
}

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]

STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CELERY_BROKER_URL = 'amqp://localhost'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_DEFAULT_QUEUE = 'celery'
CELERY_TASK_RESULT_EXPIRES = 3600
CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'django-cache'
CELERY_CREATE_MISSING_QUEUES = True

APPEND_SLASH = False

CELERY_TASK_ALWAYS_EAGER = True

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True



AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]
SESAME_MAX_AGE = 15 * 60
SESAME_ONE_TIME = True
SESAME_TOKEN_NAME = "token"



# clousinary settings
cloudinary.config(
    cloud_name = 'dciadpthx',
    api_key = '655848731445838',
    api_secret = 'wXNMHNyaGkD87-VFTs-ruUd7X7U',
    secure = True
)


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'saitreddy06@gmail.com'
EMAIL_HOST_PASSWORD = 'rndmsnlspighpxjj'
EMAIL_USE_TLS = True


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
