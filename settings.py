import sys
import os
from django.conf import settings

DEBUG = os.environ.get('DEBUG', 'on') == 'on'
SECRET_KEY = os.environ.get('SECRET_KEY', '{{ secret_key }}')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOST', '192.168.33.11').split(',')
DEBUG=DEBUG
ROOT_URLCONF='hello'
SECRET_KEY=SECRET_KEY
ALLOWED_HOSTS=ALLOWED_HOSTS
MIDDLEWARE_CLASSES=(
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
)