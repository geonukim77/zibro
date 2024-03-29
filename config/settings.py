"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-hzdd47c)rf_$8nnom-s_d05u28^$(17kxstb5mo10rf=e#-!n5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1",".zibro.club"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',  
    'django.contrib.staticfiles',
    'zips',
    'accounts',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
         # 앱안이 아닌 프로젝트 안에 탬플릿을 만들게 하는 법
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        
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

WSGI_APPLICATION = 'config.wsgi.application'


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

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# 배포시
# STATIC_ROOT = os.path.join(BASE_DIR, "static")

# STATIC_ROOT

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# 각 static 파일들은 각자 다른 경로에 나눠져 있습니다. 왜냐하면 프로젝트 전반적으로 사용하는 파일들은 STATICFILES_DIRS 에 담겨 있고, 
# 각자의 app 안에는 app 에서 사용되는 파일들이 따로 모여있습니다. 배포를 하기 위해서는 이들을 하나의 디렉토리에 모아야 하는데 
# 아래 명령어로 한 번에 모을 수 있습니다.

# python manage.py collectstatic
# 하지만 어디로 모을지는 따로 지정을 해줘야하고 그 경로가 바로 STATIC_ROOT 입니다.

# static 폴더를 따로 만들지 않더라도 지정한 경로에 만들어주고 그 안에 복사하여 담아줍니다.

# 개발중일때
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")] 

# STATICFILES_DIRS

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'config', 'static')
# ]
# 개발자가 추가로 지정을 해주셔야 하는 부분입니다. 프로젝트 전반적으로 사용되는 static 경로가 어딘지 설정합니다. 
# config 내에 static 폴더를 추가로 만들어주었습니다.

# config 가 무엇인가요?

# django-admin startproject 'project 이름'
# 다음과 같은 명령어로 project 를 생성하면 project 이름 폴더 안에 똑같은 폴더가 또 있어서 혼란을 야기 합니다. 
# 따라서 config 라고 project 를 생성한 후 최상단의 폴더 이름을 바꿈으로서 이를 예방할 수 있습니다.


MEDIA_URL = "/media/"
#MEDIA_DIRS = [os.path.join(BASE_DIR, "media")]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') #urls.py에서 MEDIA_ROOT 언급해서 이부분 필요
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
