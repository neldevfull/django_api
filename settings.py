from django.conf import settings
import secret


settings.configure(
    DEBUG=True,
    SECRET_KEY=secret.key,
    ROOT_URLCONF='hello',
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware'
    ),
)