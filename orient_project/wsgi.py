"""
WSGI config for orient_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

sys.path.append('')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orient_project.settings')
# os.environ["DJANGO_SETTINGS_MODULE"] = "orient_project.settings"

application = get_wsgi_application()

