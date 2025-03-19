from datetime import timedelta
from pathlib import Path
import os 

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-sf@(1c_$3d=d=cu%b4)ik&1zd9&hro4c1fif7)=8vmk)v_da6="

DEBUG = True

SITE_ID = 1

# ALLOWED_HOSTS = ["13.48.45.103", "*", ""]
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']   
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles", 
    "allauth",
    "allauth.account",
    "rest_framework.authtoken",
    "allauth.socialaccount",
    "dj_rest_auth",
    "rest_framework",
    "users",  
    "catalogue",
    "basket",
    "checkout",   
    "payment", 
]
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",  
]

ROOT_URLCONF = "src.urls"
BASKET_SESSION_ID = "basket"  
LOGIN_URL = "/users/login/"  

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "src.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
    "staticfiles/",
]


MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
}

IMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(
        minutes=30
    ),  # Set the lifetime of the access token
    "REFRESH_TOKEN_LIFETIME": timedelta(
        days=1
    ),  # Set the lifetime of the refresh token
    "ROTATE_REFRESH_TOKENS": False,  # Optionally rotate refresh tokens
    "BLACKLIST_AFTER_ROTATION": True,  # Blacklist old tokens after rotation
    "UPDATE_LAST_LOGIN": False,  # Update last login field upon token refresh
}
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

AUTH_USER_MODEL = 'users.CustomUsermodel'      