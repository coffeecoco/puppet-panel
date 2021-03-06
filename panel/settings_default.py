# This file is part of puppet-panel.
#
# puppet-panel is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# puppet-panel is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with puppet-panel.  If not, see <http://www.gnu.org/licenses/>.

"""
Django settings for panel project.

Generated by 'django-admin startproject' using Django 1.8.15.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_rest_apikey',
    'djoser',
    'pipeline',
    'puppet',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'panel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR + '/panel/templates'
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

WSGI_APPLICATION = 'panel.wsgi.application'


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

STATIC_ROOT = BASE_DIR + '/static/'

STATICFILES_DIRS = [
    BASE_DIR + '/panel/static/'
]

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)


# Pipeline assets
# https://django-pipeline.readthedocs.io/

PIPELINE = {
    'STYLESHEETS': {
        'vendors': {
            'source_filenames': (
                'bower_components/angular-loading-bar/build/loading-bar.min.css',
                'bower_components/angular-ui-select/dist/select.min.css',
                'bower_components/bootstrap/dist/css/bootstrap.min.css',
                'bower_components/ng-table-bundle/ng-table.min.css',
            ),
            'output_filename': 'css/vendors.css'
        },
        'app': {
            'source_filenames': (
                'app.css',
            ),
            'output_filename': 'css/app.css'
        }
    },
    'JAVASCRIPT': {
        'vendors': {
            'source_filenames': (
                'bower_components/angular/angular.min.js',
                'bower_components/angular-bootstrap/ui-bootstrap-tpls.min.js',
                'bower_components/angular-loading-bar/build/loading-bar.min.js',
                'bower_components/angular-local-storage/dist/angular-local-storage.min.js',
                'bower_components/angular-route/angular-route.min.js',
                'bower_components/angular-ui-select/dist/select.min.js',
                'bower_components/ng-table-bundle/ng-table.min.js',
            ),
            'output_filename': 'js/vendors.js'
        },
        'app': {
            'source_filenames': (
                'scripts/*.js',
                'scripts/controllers/*.js',
                'scripts/services/*.js',
            ),
            'output_filename': 'js/app.js'
        }
    }
}


# Authentication

LOGIN_URL = 'rest_framework:login'
LOGOUT_URL = 'rest_framework:logout'


# REST API

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'django_rest_apikey.authentication.APIKeyAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}


# API documentation

SWAGGER_SETTINGS = {
    'APIS_SORTER': 'alpha',
    'OPERATIONS_SORTER': 'alpha',
    'DOC_EXPANSION': 'list',
    'VALIDATOR_URL': None
}
