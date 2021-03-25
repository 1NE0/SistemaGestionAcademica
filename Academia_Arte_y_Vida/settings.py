"""
Django settings for Academia_Arte_y_Vida project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from django.conf import settings
# ENVIO DE CORREOS


EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))




# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zi6%idzlwb%^m&t^yl&_sy7-6tu#)@@=2i4v%_8%&%gvm7a#ep'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['howls.pythonanywhere.com','127.0.0.1']


# Application definition
# aqui se exportan las apps que se usan en el proyecto

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Academia_Arte_y_Vida.app.gestionacademica',
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

ROOT_URLCONF = 'Academia_Arte_y_Vida.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Agregan toda la dirección de donde esta las plantillas para las vista
        'DIRS': [
            os.path.join(BASE_DIR, 'plantillas'),
        ],
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

WSGI_APPLICATION = 'Academia_Arte_y_Vida.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
#Academia_Arte_y_Vida
""" DATABASES = {
 'default': {
         'ENGINE': 'django.db.backends.mysql',
         'NAME': 'howls$DB',
         'USER': 'howls',
         'PASSWORD': 'calcifer20',
         'HOST': 'howls.mysql.pythonanywhere-services.com',
         'PORT':'3306'
     }
} """
""" DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}  """

DATABASES  =  { 
    'default' :  { 
        'ENGINE' :  'django.db.backends.mysql' , 
        'NAME' :  'howls$DB' , 
        'USER' :  'howls' , 
        'PASSWORD' :  'calcifer20' , 
        'HOST' :  'howls.mysql.pythonanywhere-services.com' , 
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

LANGUAGE_CODE = 'es-col'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATE_INPUT_FORMATS = (
            '%d/%m/%Y',  # '25/10/2006'
                # '%b %d %Y', '%b %d, %Y',            # 'Oct 25 2006', 'Oct 25, 2006'
                    # '%d %b %Y', '%d %b, %Y',            # '25 Oct 2006', '25 Oct, 2006'
                        # '%B %d %Y', '%B %d, %Y',            # 'October 25 2006', 'October 25, 2006'
                            # '%d %B %Y', '%d %B, %Y',            # '25 October 2006', '25 October, 2006'
                            )

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (os.path.join(BASE_DIR,'static'),) 

# or, eg,
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

#files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'   # nombre de la carpeta donde se guardarán