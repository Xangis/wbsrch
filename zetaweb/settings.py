# -*- coding: utf-8 -*-
# Django settings for zetaweb project.

DEBUG = False
import os
# Add this line to /etc/environment or local vars to enable debug mode:
#WBSRCH_ENVIRONMENT=debug
environment = os.getenv('DJANGO_ENVIRONMENT')
if environment == 'debug' or environment == 'development':
    DEBUG = True

ADMINS = (
    ('Jason Champion', 'jchampion@zetacentauri.com'),
)

ALLOWED_HOSTS = [
        '.wbsrch.com', # Domain and subdomains.
        '.wbsrch.com.', # Allow FQDN and subdomains.
]

MANAGERS = ADMINS

if environment != 'production':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'zetaweb',               # Or path to database file if using sqlite3.
            'USER': 'zetaweb',               # Not used with sqlite3.
            'PASSWORD': 'd9irk0kfnv,er9kd2', # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        },
        'urls': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'urls',                  # Or path to database file if using sqlite3.
            'USER': 'zetaweb',               # Not used with sqlite3.
            'PASSWORD': 'd9irk0kfnv,er9kd2', # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        },
        'indexes': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'indexes',               # Or path to database file if using sqlite3.
            'USER': 'zetaweb',               # Not used with sqlite3.
            'PASSWORD': 'd9irk0kfnv,er9kd2', # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        },
        'news': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'news',                  # Or path to database file if using sqlite3.
            'USER': 'zetaweb',               # Not used with sqlite3.
            'PASSWORD': 'd9irk0kfnv,er9kd2', # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'zetaweb',                      # Or path to database file if using sqlite3.
            'USER': 'zetaweb',                      # Not used with sqlite3.
            'PASSWORD': 'd9irk0kfnv,er9kd2',        # Not used with sqlite3.
            'HOST': 'localhost',                    # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                             # Set to empty string for default. Not used with sqlite3.
        },
        'urls': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'urls',                         # Or path to database file if using sqlite3.
            'USER': 'zetaweb',                      # Not used with sqlite3.
            'PASSWORD': 'd9irk0kfnv,er9kd2',        # Not used with sqlite3.
            'HOST': 'localhost',                    # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                             # Set to empty string for default. Not used with sqlite3.
        },
        'indexes': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'indexes',                      # Or path to database file if using sqlite3.
            'USER': 'zetaweb',                      # Not used with sqlite3.
            'PASSWORD': 'd9irk0kfnv,er9kd2',        # Not used with sqlite3.
            'HOST': 'localhost',                    # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                             # Set to empty string for default. Not used with sqlite3.
        },
        'news': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'news',                         # Or path to database file if using sqlite3.
            'USER': 'zetaweb',                      # Not used with sqlite3.
            'PASSWORD': 'd9irk0kfnv,er9kd2',        # Not used with sqlite3.
            'HOST': 'localhost',                    # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                             # Set to empty string for default. Not used with sqlite3.
        }
    }

DATABASE_ROUTERS = ['zetaweb.dbrouter.ModelDatabaseRouter',]

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

LOCALE_PATHS = (
    "/var/django/wbsrch/locale",
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/var/django/wbsrch/templates/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/admin/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'dv9z&amp;gl$+u5*kxrfgn2ajse24off-z0xge&amp;wcz75rf+8@kf^hw'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['/var/django/wbsrch/templates/',],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
                "django.core.context_processors.debug",
                "django.core.context_processors.i18n",
                "django.core.context_processors.media",
                "django.core.context_processors.tz",
                "django.contrib.messages.context_processors.messages"],
            'allowed_include_roots': ['/var/django/wbsrch/templates/',],
            #'debug': DEBUG,
        },
    },
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': ['/var/django/wbsrch/jinjatemplates/',],
        'APP_DIRS': False,
        'OPTIONS': {
            #'debug': DEBUG,
        },
    },
]


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'languagemiddleware.LanguageFromDomain',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'zetaweb.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'zetaweb.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'tagging',
    'dir',
    'blog',
    'rest_framework',
    'rest_framework.authtoken',
    'django_q',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        # This is where we log those SuspiciousOperation HTTP_HOST header violations.
        # No sense getting thousands of emails a day for something we don't care about.
        # We can always go back later and look.
        'spoof_logfile': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            # This file must be writable by the "run as" user in /etc/init.d/django-wbsrch.
            'filename': '/var/django/wbsrch/log/spoofed_requests.log',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.security.DisallowedHost': {
            'handlers': ['spoof_logfile'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}

SOUTH_TESTS_MIGRATE = False

from django.conf import global_settings

gettext_noop = lambda s: s

LANGUAGES = (
('ak', gettext_noop('Akan')),
('ca', gettext_noop('Catalan')),
('cs', gettext_noop('Czech')),
('da', gettext_noop('Danish')),
('de', gettext_noop('German')),
('el', gettext_noop('Greek')),
('en', gettext_noop('English')),
('es', gettext_noop('Spanish')),
('et', gettext_noop('Estonian')),
('fi', gettext_noop('Finnish')),
('fr', gettext_noop('French')),
('ha', gettext_noop('Hausa')),
('hr', gettext_noop('Croation')),
('hu', gettext_noop('Hungarian')),
('ig', gettext_noop('Igbo')),
('is', gettext_noop('Icelandic')),
('it', gettext_noop('Italian')),
('kg', gettext_noop('Kongo')),
('ln', gettext_noop('Lingala')),
('lt', gettext_noop('Lituanian')),
('lv', gettext_noop('Latvian')),
('nl', gettext_noop('Dutch')),
('nb', gettext_noop('Norwegian')),
('pl', gettext_noop('Polish')),
('pt', gettext_noop('Portuguese')),
('ro', gettext_noop('Romanian')),
('rw', gettext_noop('Rwanda')),
('sk', gettext_noop('Slovakian')),
('sl', gettext_noop('Slovene')),
('sn', gettext_noop('Shona')),
('so', gettext_noop('Somali')),
('sv', gettext_noop('Swedish')),
('sw', gettext_noop('Swahili')),
('tr', gettext_noop('Turkish')),
('wo', gettext_noop('Wolof')),
('yo', gettext_noop('Yoruba')),
('zu', gettext_noop('Zulu'))
)

EXTRA_LANG_INFO = {
    'ak': {
        'bidi': False,
        'code': 'ak',
        'name': 'Akan',
        'name_local': u'Akan'
    },
    'bm': {
        'bidi': False,
        'code': 'bm',
        'name': 'Bambara',
        'name_local': u'Bamanankan'
    },
    'ff': {
        'bidi': False,
        'code': 'ff',
        'name': 'Fulani',
        'name_local': u'Fufulde'
    },
    'fo': {
        'bidi': False,
        'code': 'fo',
        'name': 'Faroese',
        'name_local': u'Føroyskt'
    },
    'ha': {
        'bidi': False,
        'code': 'ha',
        'name': 'Hausa',
        'name_local': u'Hausa'
    },
    'ig': {
        'bidi': False,
        'code': 'ig',
        'name': 'Igbo',
        'name_local': u'Asụsụ Igbo'
    },
    'kg': {
        'bidi': False,
        'code': 'kg',
        'name': 'Kongo',
        'name_local': u'Kikongo'
    },
    'ki': {
        'bidi': False,
        'code': 'ki',
        'name': 'Kikuyu',
        'name_local': u'Gikuyu'
    },
    'la': {
        'bidi': False,
        'code': 'la',
        'name': 'Latin',
        'name_local': u'Latina'
    },
    'lg': {
        'bidi': False,
        'code': 'lg',
        'name': 'Luganda',
        'name_local': u'Oluganda'
    },
    'ln': {
        'bidi': False,
        'code': 'ln',
        'name': 'Lingala',
        'name_local': u'Ngala'
    },
    'ny': {
        'bidi': False,
        'code': 'ny',
        'name': 'Nyanja',
        'name_local': u'Chinyanja'
    },
    'om': {
        'bidi': False,
        'code': 'om',
        'name': 'Oromo',
        'name_local': u'Afaan Oromoo'
    },
    'rw': {
        'bidi': False,
        'code': 'rw',
        'name': 'Rwanda',
        'name_local': u'Kinyarwanda'
    },
    'sc': {
        'bidi': False,
        'code': 'sc',
        'name': 'Sardinian',
        'name_local': u'Sardinian'
    },
    'scn': {
        'bidi': False,
        'code': 'scn',
        'name': 'Sicilian',
        'name_local': u'Sicilianu'
    },
    'sn': {
        'bidi': False,
        'code': 'sn',
        'name': 'Shona',
        'name_local': u'chiShona'
    },
    'so': {
        'bidi': False,
        'code': 'so',
        'name': 'Somali',
        'name_local': u'Af-Soomaali'
    },
    'ss': {
        'bidi': False,
        'code': 'ss',
        'name': 'Swazi',
        'name_local': u'SiSwati'
    },
    'tn': {
        'bidi': False,
        'code': 'tn',
        'name': 'Tswana',
        'name_local': u'Setswana'
    },
    'ts': {
        'bidi': False,
        'code': 'ts',
        'name': 'Tsonga',
        'name_local': u'Xitsonga'
    },
    've': {
        'bidi': False,
        'code': 've',
        'name': 'Venda',
        'name_local': u'Tshivenda'
    },
    'wo': {
        'bidi': False,
        'code': 'wo',
        'name': 'Wolof',
        'name_local': u'Wolof'
    },
    'xh': {
        'bidi': False,
        'code': 'xh',
        'name': 'Xhosa',
        'name_local': u'isiXhosa'
    },
    'yo': {
        'bidi': False,
        'code': 'yo',
        'name': 'Yoruba',
        'name_local': u'èdè Yorùbá'
    },
    'zu': {
        'bidi': False,
        'code': 'zu',
        'name': 'Zulu',
        'name_local': u'isiZulu'
    },
}

import django.conf.locale
LANG_INFO = dict(django.conf.locale.LANG_INFO.items() + EXTRA_LANG_INFO.items())
django.conf.locale.LANG_INFO = LANG_INFO

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_FUNCTION': 'memcachedkeys.make_key',
    }
}

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

GEOIP_PATH = '/var/django/wbsrch/geoip/'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}

Q_CLUSTER = {
    'name': 'wbsrch',
    'workers': 8,
    'compress': True,
    'label': 'Django Q',
    'redis': {
        'host': '127.0.0.1',
        'port': 6379,
        'db': 1, }
}
