"""
Django settings for tarteel project.

Generated by 'django-admin startproject' using Django 1.11.13.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import django_heroku

import django.conf
import environ
import os
import warnings

# Env file setup
ROOT = environ.Path(__file__) - 2   # 2 directories up = tarteel.io/
BASE_DIR = ROOT()
ALLOWED_HOSTS = ['www.tarteel.io', 'tarteel.io', 'localhost', '127.0.0.1', '52.37.77.137', '.tarteel.io',
                 '172.31.22.119', '54.187.2.185', 'tarteel.io', 'tarteel-api.herokuapp.com']

env = environ.Env(
    # Set Casting and default values
    DEBUG=(bool, True)
)
env.read_env(str(ROOT.path('tarteel/.env')))

# GENERAL
# ------------------------------------------------------------------------------
SECRET_KEY = env('SECRET_KEY', str, default='development_security_key')
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env('DEBUG', bool, default=True)
# Local time zone: http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = env('TIME_ZONE', str, default='UTC')
# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = env('LANGUAGE_CODE', str, default='en-us')
# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = env('USE_I18N', bool, default=True)
# https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = env('USE_L10N', bool, default=True)
# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = env('USE_TZ', bool, default=True)
# Main site (1, tarteel.io) if local env, else (2, 127.0.0.1/localhost)
SITE_ID = 2 if DEBUG else 1

# FIXTURES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/howto/initial-data/
# Use this to set JSON files which initialize defaults (usually for testing)
# FIXTURE_DIRS = [
#     ROOT('tarteel/fixtures'),
# ]

# Set the sites migration folders locally to create default site changes for
# authentication testing. socialaccount added b/c it it depends on sites.
MIGRATION_MODULES = {
    'sites': 'tarteel.fixtures.sites_migrations',
    'socialaccount': 'tarteel.fixtures.socialaccount_migrations'
}

# RELATED TO HTTPS REDIRECT
SECURE_SSL_REDIRECT = env('SECURE_SSL_REDIRECT', bool, default=False)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = env('SESSION_COOKIE_SECURE', bool, default=False)
CSRF_COOKIE_SECURE = env('CSRF_COOKIE_SECURE', bool, default=False)
PREPEND_WWW = env('PREPEND_WWW', bool, default=False)

# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
]
THIRD_PARTY_APPS = [
    'rest_framework',
    'compressor',
    'corsheaders',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.github',
]
LOCAL_APPS = [
    'audio',
    'restapi',
    'evaluation',
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


# MIDDLEWARE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# URLS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = 'tarteel.urls'
# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'tarteel.wsgi.application'


# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ROOT('db.sqlite3'),
    }
}


# AUTHENTICATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
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
# Authentication backends
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Django Allauth Configs
# https://django-allauth.readthedocs.io/en/latest/configuration.html
# Dictionary containing provider specific settings.
""" Commented out until regular auth fully setup
SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'SCOPE': [
            'user',
            'read:user'
        ],
    },
    # https://django-allauth.readthedocs.io/en/latest/providers.html#facebook
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'default'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time',
        ],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': lambda request: 'en_US',  # Temp return just US
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.12',
    }
}
"""
# https://docs.djangoproject.com/en/dev/ref/settings/#login-url
# LOGIN_URL = env('LOGIN_URL')
# LOGOUT_URL = env('LOGOUT_URL')
# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = env('LOGIN_REDIRECT_URL', str, '/accounts/profile/')
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
# Development env. has email printed to console. Production uses actual email server
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = env('EMAIL_HOST', str, 'smtp.gmail.com')
EMAIL_PORT = env('EMAIL_PORT', int, 465)
EMAIL_HOST_USER = env('EMAIL_HOST_USER', str, 'contact.tarteel@gmail.com')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', str, 'mysupersecretpassword')

# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = ROOT('static')
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [
    ROOT('audio/static'),
    ROOT('evaluation/static')
]
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]

# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = ROOT('media')
# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'


# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ROOT('templates')],
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

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}

# django-compressor
# ------------------------------------------------------------------------------
# Compression setup
COMPRESS_ENABLED = not DEBUG
COMPRESS_OFFLINE = False
COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssRelativeFilter',
                        'compressor.filters.cssmin.CSSCompressorFilter',
                        'compressor.filters.yuglify.YUglifyJSFilter']


# django-corsheader
# ------------------------------------------------------------------------------
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

# Inorder we wanted to only whitelist our domains
# CORS_ORIGIN_WHITELIST = (
#     'localhost:3000',
# )

# Activate Django-Heroku.
django_heroku.settings(locals())
