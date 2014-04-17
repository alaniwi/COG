#== LOCAL SETTINGS - CHANGE AS APPROPRIATE FOR EACH INSTALLATION ========

# default search configuration
DEFAULT_SEARCH_URL = 'http://hydra.fsl.noaa.gov/esg-search/search/'
DEFAULT_SEARCH_FACETS = { 'project':'Project',
                          'realm':'Realm',
                          'variable':'Variable',
                          'cf_variable':'CF Variable'  }

#COG_MAILING_LIST = "cog_info@list.woc.noaa.gov"

#===== SITE SPECIFIC CONFIGURATION =================

from cog.site_manager import SiteManager
siteManager = SiteManager()
SITE_ID = siteManager.get('SITE_ID')
TIME_ZONE = siteManager.get('TIME_ZONE')
COG_MAILING_LIST = siteManager.get('COG_MAILING_LIST')
SECRET_KEY = siteManager.get('SECRET_KEY')
DATABASE_USER = siteManager.get('DATABASE_USER')
DATABASE_PASSWORD = siteManager.get('DATABASE_PASSWORD')
DATABASE_PORT = siteManager.get('DATABASE_PORT')

# ESGF specific settings
ESGF = 'esgf'
ESGF_CONFIG = siteManager.hasConfig(ESGF)
if ESGF_CONFIG:
    ESGF_HOSTNAME = siteManager.get('ESGF_HOSTNAME', section=ESGF)
    ESGF_DBURL = siteManager.get('ESGF_DBURL', section=ESGF)
    IDP_WHITELIST = siteManager.get('IDP_WHITELIST', section=ESGF)

#=================== DO NOT CHANGE ANYTHING BELOW THIS LINE =============

# Django settings for COG project.
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
import os

rel = lambda *x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# DEV/PROD switch
server_type = os.environ.get("SERVER_TYPE", "DEV")

# IMPORTANT: this setting must be set to True if using COG behind a proxy server,
# otherwise redirects won't work properly
USE_X_FORWARDED_HOST = True

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    # SQLite database
    #'default': {
    #     #'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
    #     #'NAME': '',                      # Or path to database file if using sqlite3.
    #    'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
    #    'NAME': rel('./database/django.data'),
    #    'USER': '',                      # Not used with sqlite3.
    #    'PASSWORD': '',                  # Not used with sqlite3.
    #    'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
    #    'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    #}
    # Postgres
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cogdb',
        'USER': DATABASE_USER,                      # Not used with sqlite3.
        'PASSWORD': DATABASE_PASSWORD,                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': DATABASE_PORT,                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
#TIME_ZONE = 'America/Denver'
# use the system time zone, wherever the application is installed
#TIME_ZONE = None

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

#SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = rel('site_media/')

# Filebrowser directory relative to MEDIA_ROOT (IMPORTANT: must have traiing slash)
FILEBROWSER_DIRECTORY = "projects/"

# versions generated when browsing images
FILEBROWSER_VERSIONS = {
    'admin_thumbnail': {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop'},
    'thumbnail': {'verbose_name': 'Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop'},
    #'small': {'verbose_name': 'Small (2 col)', 'width': 140, 'height': '', 'opts': ''},
    #'medium': {'verbose_name': 'Medium (4col )', 'width': 300, 'height': '', 'opts': ''},
    #'big': {'verbose_name': 'Big (6 col)', 'width': 460, 'height': '', 'opts': ''},
    #'large': {'verbose_name': 'Large (8 col)', 'width': 680, 'height': '', 'opts': ''},
}

# versions selectable through admin interface
FILEBROWSER_ADMIN_VERSIONS = ['thumbnail']

# absolute path to directory containing project specific media
PROJECTS_ROOT = os.path.join(MEDIA_ROOT, FILEBROWSER_DIRECTORY)

# absolute path to root directory containing projects data
DATA_ROOT = os.path.join(MEDIA_ROOT, "data/")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
#MEDIA_URL = 'http://localhost:8000/site_media/'
MEDIA_URL = '/site_media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a trailing slash.
# Examples: "http://foo.com/media/", "/media/".
STATIC_URL = '/static/'
STATIC_ROOT = rel('static/')

# Make this unique, and don't share it with anybody.
#SECRET_KEY = 'yb@$-bub$i_mrxqe5it)v%p=^(f-h&x3%uy040x))19g^iha&#'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'cog.plugins.esgf.idp_whitelist.IdpWhitelistMiddleware',
    #'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

#ROOT_URLCONF = 'COG.urls'
ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    #os.path.join(os.path.basename(__file__), 'templates'),
    rel('templates/'),
    rel('static/'),
    #'/usr/COG/filebrowser/templates',
    #'/Users/cinquini/Documents/workspace-python/django-projects/COG/templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django_openid_auth',
    'grappelli',
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.comments',
    'django.contrib.webdesign',
    'django.contrib.staticfiles',
    'pagination',
    'south',
    'layouts',
    'cog',
)

AUTHENTICATION_BACKENDS = (
    'django_openid_auth.auth.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
)

OPENID_CREATE_USERS = True

OPENID_UPDATE_DETAILS_FROM_SREG = True

# login page URL (default: '/accounts/login')
#LOGIN_URL = '/login'

# OpenID login page
LOGIN_URL = '/openid/login/'

# page to redirect after successfull authentication, if 'next' parameter is not provided
#LOGIN_REDIRECT_URL='/cog/' # COG projects index
LOGIN_REDIRECT_URL='/' # welcome page

# Custom user profile
AUTH_PROFILE_MODULE = "cog.UserProfile"

# makes 'request' object available in templates
TEMPLATE_CONTEXT_PROCESSORS += (
     'django.core.context_processors.request',
     'cog.context_processors.cog_settings'
)

# HTTPS support: can only send cookies via SSL connections
if server_type=='PROD':
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SESSION_EXPIRE_AT_BROWSER_CLOSE = True


# CSS styles
#COLOR_DARK_TEAL = "#358C92"
#COLOR_LIGHT_TEAL = "#B9E0E3"

#COLOR_DARK_YELLOW = "#FAC2A4";
#COLOR_LIGHT_YELLOW = "#FCE79F";

#COLOR_DARK_GRAY = "#666666";