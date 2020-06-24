"""
Django settings for djangoStudy project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# 配置项目根目录路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("根目录路径:", BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# 签名加密
SECRET_KEY = ')$7gfv)^+0^sohss!&wels8dm32^v%q$ewhd-xt(1ncu1r!vuf'

# SECURITY WARNING: don't run with debug turned on in production!
# 调试模式
DEBUG = True
# 允许的主机列表
ALLOWED_HOSTS = ['localhost', '192.168.31.10', '10.195.106.43', '127.0.0.1']

# Application definition
# 安装应用
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 加入commdapp的自定义数据库表
    'common.apps.CommonConfig',
    'App'  # 把自己的应用进行安装
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 接口测试临时关掉 中间件
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 自己添加的中间件
    # 'utils.csrfTokenMiddleware.CsrfTokenMiddleware'
]
# 根路由
ROOT_URLCONF = 'djangoStudy.urls'

# 模板配置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 模板目录
        #'DIRS': [],
        'APP_DIRS': True,  #是否在应用下放模板引擎
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
print('templates目录:', TEMPLATES[0]["DIRS"])
# 项目入口
WSGI_APPLICATION = 'djangoStudy.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
# 数据库配置
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '10.195.106.43',
        'PORT': '3306',
        'USER': 'djangoStudy',
        'PASSWORD': 'protoss',
        'NAME': 'djangoStudy',
        # 避免映射数据库时出现警告
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators
# 验证
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/
# 语言配置

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True
# 是否使用国际标准时间 不使用 不改数据库时间是错的
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
# 静态资源请求路径
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
print("静态目录:", STATICFILES_DIRS)
