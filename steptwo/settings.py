import sys
import os
from django.conf import settings

BASE_DIR=os.path.dirname(__file__)
DEBUG=os.environ.get('DEBUG', 'on') == 'on'
SECRET_KEY=os.environ.get('SECRET_KEY')
ALLOWED_HOSTS=os.environ.get('ALLOWED_HOSTS', '192.168.33.11').split(',')
ROOT_URLCONF='app'
MIDDLEWARE_CLASSES=(
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
)
INSTALLED_APPS=(
    'django.contrib.staticfiles',
)
TEMPLATES=(
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (os.path.join(BASE_DIR, 'templates'), ),
    },
)
STATICFILES_DIRS=(
    os.path.join(BASE_DIR, 'static'),
)
STATIC_URL='/static/'