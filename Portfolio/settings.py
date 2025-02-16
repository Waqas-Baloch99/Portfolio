from pathlib import Path
import os
LOGIN_URL = '/login/'

STRIPE_PUBLIC_KEY = os.getenv("STRIPE_PUBLIC_KEY", "pk_test_51QQnd0BopiD2AhCIOYSy0ULv1UL04slC0c7Agflxa8tgGFG2j6XeEqvxviH9zdi43E43vaBZhO0cJLV9O3cc6hEr00K5pK3Xg3")
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "sk_test_51QQnd0BopiD2AhCIPcxiWRnFa24f4ZzfCEM7L3kp52J8jq0OPIroZxx2b2SXg7XKq8Kjjed4CUvdD9gIcVLGglFE00CKRpK0Qp")
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Custom user model
AUTH_USER_MODEL = 'portfolio_app.CustomUser'

# Quick-start development settings - unsuitable for production
SECRET_KEY = 'django-insecure-@j&)aivph@f6o6xvc4*$oi6a9)8s%5$!2v=@h-zyy#n=d(b0!x'

# Media files settings
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Debug settings
DEBUG = True

ALLOWED_HOSTS = [
    'portfolio-spdc.up.railway.app',
    '.railway.app',
]


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolio_app',
    'crispy_forms',
    'crispy_bootstrap5',
    'widget_tweaks',
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'portfolio_app.middleware.CheckMembershipMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'Portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'Portfolio.wsgi.application'

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Localization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files settings
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' 
# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'waqaskhosa99@gmail.com'
EMAIL_HOST_PASSWORD = 'mncc wotf vfri gnlt'
CSRF_TRUSTED_ORIGINS = [
    'https://portfolio-spdc.up.railway.app',
]

