"""
Django settings for club_managment project in production mode

This fill will be automatically used when using a dedicated application server.
See `base.py` for basic settings.

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""


from .base import *


DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-0e^e$qdgsnot)i=p(no-((jli@8@tu(^5=_$88abfmfjuii@0i"

# remember to set this to your expected hostnames
ALLOWED_HOSTS = []
