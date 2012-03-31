import os

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

if 'ckeditor' in settings.INSTALLED_APPS:
    # Confirm CKEDITOR_MEDIA_PREFIX setting has been specified.
    try:
        settings.CKEDITOR_MEDIA_PREFIX
    except AttributeError:
        raise ImproperlyConfigured("django-ckeditor requires \
                CKEDITOR_MEDIA_PREFIX setting. This setting specifies a URL \
                prefix to the ckeditor JS and CSS media (not uploaded media). \
                Make sure to use a trailing slash: CKEDITOR_MEDIA_PREFIX = \
                '/media/ckeditor/'")

