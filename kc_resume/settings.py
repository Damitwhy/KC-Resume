import os
import sys
import dj_database_url
from pathlib import Path
from dotenv import load_dotenv

from decouple import config

# Imports env.py file

# Import environment variables from env.py
if os.path.isfile('env.py'):
    import env

SECRET_KEY = config('SECRET_KEY')

CLOUDINARY_URL = config('CLOUDINARY_URL')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# imports template directory

TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
 #os.environ.get('SECRET_KEY') #

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False #os.environ.get("DEBUG", "") == "1"

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.ws.codeinstitute-ide.net', '.herokuapp.com','purerarez.co.uk', 'www.purerarez.co.uk' ]

# Specify the custom user model
AUTH_USER_MODEL = 'core.User'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third-party apps
    'django_summernote',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'cloudinary_storage',
    'cloudinary',
    # Local apps
    'core',
]

# Authentication backends
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Django Allauth settings
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'none'

# Site ID for Django Allauth
SITE_ID = 1
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Custom middleware
    #'core.middleware.AdminAccessMiddleware',#restricts access to admin page to superusers and staff
    'allauth.account.middleware.AccountMiddleware',
    # 'core.middleware.AdminAccessMiddleware',
]

ROOT_URLCONF = 'kc_resume.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'kc_resume.wsgi.application'


# django summernote settings
def is_admin_or_superuser(user):
    return user.is_authenticated and (user.is_superuser or user.is_staff)


SUMMERNOTE_CONFIG = {
    # Ensure only authenticated users can upload
    'attachment_require_authentication': True,
    # Custom permission check
    'attachment_require_permissions': (is_admin_or_superuser,),
    # Enable uploads, but restrict them with the custom permission check
    'disable_upload': True,
    'summernote': {
        'toolbar': [
            ['style', ['style']],
            ['font', ['bold', 'italic', 'underline', 'clear']],
            ['fontname', ['fontname']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['height', ['height']],
            ['table', ['table']],
            ['insert', ['link']],  # Allow image and video uploads
            ['view', ['fullscreen', 'codeview', 'help']],
        ],
    },
}

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

#DATABASES = {'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))}
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'purerarez',
#        'USER': 'purerarez',
#        'PASSWORD': 'purerarez',
#        'HOST': 'localhost',  # Set to 'localhost' if PostgreSQL is on the same server
#        'PORT': '5432',
#    }
#}


if 'test' in sys.argv:
    DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'

CSRF_TRUSTED_ORIGINS = [
    "https://*.codeinstitute-ide.net",
    "https://*.herokuapp.com",
    "http://localhost:8000",
    "https://purerarez.co.uk",
    "http://purerarez.co.uk",
    "https://www.purerarez.co.uk",
    "http://www.purerarez.co.uk",
]


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'GB'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

LOGIN_REDIRECT_URL = '/'  # Fallback URL

# # Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # e.g., 'smtp.gmail.com' for Gmail
EMAIL_PORT = 587  # 587 or 465 for SSL
EMAIL_USE_TLS = True  # or EMAIL_USE_SSL = True for SSL
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")  # your email
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")  # your email password
DEFAULT_FROM_EMAIL = 'damitwhy01@gmail.com'  # your email


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#LOGGING = {
#    'version': 1,
#    'disable_existing_loggers': False,
#    'handlers': {
#        'file': {
#            'level': 'DEBUG',
#            'class': 'logging.FileHandler',
#            'filename': os.path.join(BASE_DIR, 'logs/debug.log'),  # Change log file location
#        },
#    },
#    'loggers': {
#        'django': {
#            'handlers': ['file'],
#            'level': 'DEBUG',
#            'propagate': True,
#        },
#    },
#}                                         