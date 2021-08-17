"""
Django settings for boutique_ado project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-n3)pa_1u(kq99&htx=-o8(!%6osp72m^n8kci)wrs(=9jin*74'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Used by socialaccount app to create the proper callback
    # URLs when connecting via social media accounts
    # Used in conjunction with SITE_ID setting added below
    'django.contrib.sites',
    'allauth',
    # Allauth app which allows for basic user account stuff
    # like logging in/out, user registration, password reset
    'allauth.account',
    # Specifically handles logging in via social media providers
    'allauth.socialaccount',
    'home',
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

ROOT_URLCONF = 'boutique_ado.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # root templates directory
            os.path.join(BASE_DIR, 'templates'),
            # custom allauth directory
            os.path.join(BASE_DIR, 'templates', 'allauth')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                # Allows django and allauth to access to access HTTP requests
                # in templates. REQUIRED BY ALLAUTH
                # For, example, if we wanted to use request.user in our
                # templates, we will be able with this context precessor
                # Allauth templates use request frequently
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    # Handles superusers loggin into the admin. Allauth doesn't handle
    # this, so we defer to the default django code
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    # Users can log in with their email address
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

# Allauth will send confirmation emails to any new account by default,
# so we need to temporarily log those emails to the console to get the
# confirmation links
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Tell Allauth to allow authentication using either usernames or emails
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
# Email is required to register for the site
ACCOUNT_EMAIL_REQUIRED = True
# Verifing email is mandatory, ensuring users are using real email
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# Email must be entered twice to ensure no typos
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
# Usernames must be at least 4 characters
ACCOUNT_USERNAME_MIN_LENGTH = 4
# Specify login URL
LOGIN_URL = '/accounts/login/'
# Specify URL to redirect back to after loggin in
# which is the Home Page of the store
LOGIN_REDIRECT_URL = '/'

WSGI_APPLICATION = 'boutique_ado.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
