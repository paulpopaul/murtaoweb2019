"""
Django settings for murtaoweb project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$*engvnvb^o&xf4fag-$1yh=eg%&l65e8t^-f(g1o*qb4(!000'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [u'127.0.0.1', u'murtao.cl', u'www.murtao.cl', u'192.168.1.8', u'192.168.1.10', u'192.168.1.7', u'0.0.0.0']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'simple_history',
    'crispy_forms',
    'easy_thumbnails',
    'blogapp',
    'contacto',
    'control_panelapp',
    'cartaapp',
    'eventosapp',
    'galeriaapp',
    'instaapp',
    'menuapp',
    'reservasapp',
    'suscripcionapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]

ROOT_URLCONF = 'murtaoweb.urls'

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
    'APP_DIRS': True,
    'OPTIONS': {
      'context_processors': [
        'django.contrib.auth.context_processors.auth',
        'django.template.context_processors.i18n',
        'django.template.context_processors.request',
        'django.contrib.messages.context_processors.messages',
      ]
    }
  }
]

WSGI_APPLICATION = 'murtaoweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_L10N = True

USE_TZ = True




'''
Servers:

POP (for receiving) — mail.webfaction.com
IMAP (for receiving) — mail.webfaction.com
SMTP (for sending) — smtp.webfaction.com
Ports:

 	Standard	Secure (SSL)	Secure (TLS)
POP	110	995
IMAP	143	993
SMTP	25	465	587
Servers:

POP (for receiving) — mail.webfaction.com
IMAP (for receiving) — mail.webfaction.com
SMTP (for sending) — smtp.webfaction.com
Ports:

 	Standard	Secure (SSL)	Secure (TLS)
POP 	110     	995
IMAP	143     	993
SMTP	25	        465	            587
'''

ADMINS = (('contactomurtao', 'contacto@murtao.cl'))
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_PASSWORD = 'Murtao4000'
EMAIL_HOST_USER = 'contactomurtao'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'contacto@murtao.cl'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CRISPY_TEMPLATE_PACK = 'bootstrap4'

THUMBNAIL_ALIASES = {
    '': {
        'eventos': {'size': (70, 50), 'crop': True},
        'menu': {'size': (260, 260), 'crop': True},
        'galeria': {'size': (780, 520), 'crop': True},
        'carta': {'size': (520, 780), 'crop': True},
        'blog': {'size': (720, 420), 'crop': True},
        'instagram': {'size': (900, 900), 'crop': True},
    },
}