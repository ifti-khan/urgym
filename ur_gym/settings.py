"""
Django settings for ur_gym project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
import dj_database_url
import environ
from pathlib import Path

# This initialise the environment variables
# which I have set as myenv
myenv = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
if 'SECRET_KEY' in os.environ:
    # Deployed env secret key
    SECRET_KEY = os.getenv("SECRET_KEY")
else:
    # Development env secret key
    SECRET_KEY = myenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
if 'DEVELOPMENT' in os.environ:
    # Status Deployed
    DEBUG = False
else:
    # Status Development
    DEBUG = True

if ' RENDER_HOSTNAME' in os.environ:
    # Deployment
    ALLOWED_HOSTS = ['iftikhan-urgym.onrender.com']
else:
    # Development
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # These apps copied from the allauth documentation
    # To allow users to login and out and signup with
    # socail media accounts
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # my created apps for the project
    'home',
    'products',
    'trolley',
    'checkout',
    'profiles',
    'community',

    # Other
    'crispy_forms',
    'crispy_bootstrap5',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ur_gym.urls'

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'

CRISPY_TEMPLATE_PACK = 'bootstrap5'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'allauth'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                # line below is required by allauth to access
                # http request objects from the templates
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # This is for the media URL template, for the no images
                'django.template.context_processors.media',
                # Shopping trolley context processor
                'trolley.contexts.trolley_contents',
            ],
            # Creating a list for the crispy forms tag we want to avaliable to
            # use in all the projects templates by default
            'builtins': [
                'crispy_forms.templatetags.crispy_forms_tags',
                'crispy_forms.templatetags.crispy_forms_field',
            ]
        },
    },
]

# This is to store messages in the session for the toasts
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# This code was taken from the allauth documentation website
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

# Deployed email settings
if 'EMAIL_HOST_USER' in os.environ:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
    DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')
else:
    # Development email settings
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = 'info@urgym.com'

"""
This block of code allows users to login via username or email
Also making sure that an email address is required to register
also making email verification mandatory and confirm email address
twice during registartion. This also set a min username char length,
login url and a login redirect to the homepage after successful login.
"""
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'

WSGI_APPLICATION = 'ur_gym.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# Database if statement to check environment variables
if not 'DATABASE_URL' in os.environ:
    # Deployed environment variable
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    # Development environment variable
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

if 'USE_AWS' in os.environ:
    # Cache control will tell the browser it ok to
    # cache static files for a long time, for better site
    # performance for the users.
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }
    # S3 Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'iftikhan-urgym-ms4'
    AWS_S3_REGION_NAME = 'eu-west-2'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files storage vars being pulled
    # from custom_storages.py file and telling which
    # storage dirs to use for static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs when deployed to heroku
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

# These two variables will be used to calculate the
# delivery cost of an order
FREE_DELIVERY_LIMIT = 50
STANDARD_DELIVERY_PERCENTAGE = 10

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Stripe
FREE_DELIVERY_LIMIT = 50
STANDARD_DELIVERY_PERCENTAGE = 10
STRIPE_CURRENCY = 'gbp'

# Stripe ifs to check wether keys are in deployment or development
if 'STRIPE_PUBLIC_KEY' in os.environ:
    STRIPE_PUBLIC_KEY = os.getenv("STRIPE_PUBLIC_KEY", '')
else:
    STRIPE_PUBLIC_KEY = myenv("STRIPE_PUBLIC_KEY")

if 'STRIPE_SECRET_KEY' in os.environ:
    STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", '')
else:
    STRIPE_SECRET_KEY = myenv("STRIPE_SECRET_KEY")

if 'STRIPE_WH_SECRET' in os.environ:
    STRIPE_WH_SECRET = os.getenv("STRIPE_WH_SECRET", '')
else:
    STRIPE_WH_SECRET = myenv("STRIPE_WH_SECRET")

# Google Maps API
GMAPS_API_KEY = myenv('GMAPS_API_KEY')
