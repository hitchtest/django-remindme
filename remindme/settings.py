"""
Django settings for remindme project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SITE_ID = 1


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ia8$&taf+sjjc$!tm-3#z+%*ay1z3!)$k%79$l$y$s5u$xh#57'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'remindme',
    'twitter_bootstrap',
    'crispy_forms',
    'pipeline',
    'allauth',
    'allauth.account',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'remindme.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        #'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'allauth.account.context_processors.account',
                'allauth.socialaccount.context_processors.socialaccount',
            ],
            'loaders': (
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            )
        },
    },
]


AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

WSGI_APPLICATION = 'remindme.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'remindme',
        'USER': 'remindme',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '15432',
    }
}

EMAIL_HOST = 'localhost'
EMAIL_PORT = 10025
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yui.YUICompressor'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.yui.YUICompressor'
PIPELINE_YUI_BINARY = 'yui-compressor'
PIPELINE_COMPILERS = ('pipeline.compilers.less.LessCompiler',)

PIPELINE_CSS = {
    'bootstrap': {
        'source_filenames': (
            'twitter_bootstrap/less/bootstrap.less',
        ),
        'output_filename': 'css/b.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
}

PIPELINE_JS = {
    'bootstrap': {
        'source_filenames': (
          'jquery/jquery.js',
          #'twitter_bootstrap/js/transition.js',
          #'twitter_bootstrap/js/modal.js',
          #'twitter_bootstrap/js/dropdown.js',
          #'twitter_bootstrap/js/scrollspy.js',
          #'twitter_bootstrap/js/tab.js',
          #'twitter_bootstrap/js/tooltip.js',
          #'twitter_bootstrap/js/popover.js',
          #'twitter_bootstrap/js/alert.js',
          #'twitter_bootstrap/js/button.js',
          #'twitter_bootstrap/js/collapse.js',
          #'twitter_bootstrap/js/carousel.js',
          #'twitter_bootstrap/js/affix.js',
        ),
        'output_filename': 'js/b.js',
    },
}


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), '../media').replace('\\','/')
STATIC_ROOT = os.path.join(os.path.dirname(__file__), '../static').replace('\\','/')
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'

LOGIN_REDIRECT_URL = '/dashboard'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

AUTH_USER_MODEL = 'remindme.ReminderUser'

BROKER_URL = "redis://localhost:16379/1"

#CELERY_RESULT_BACKEND = "redis"

#CELERYBEAT_SCHEDULE = {
    #'reminder-every-five-seconds': {
        #'task': 'remindme.celery.send_reminder',
        #'schedule': datetime.timedelta(seconds=5),
        #'args': (),
    #},
#}

#CELERY_ACCEPT_CONTENT = ['json', ]
#CELERY_TIMEZONE = 'UTC'

#CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']

#CELERYBEAT_MAX_LOOP_INTERVAL = 5
#CELERYBEAT_SYNC_EVERY = 1
