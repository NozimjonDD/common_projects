"""
ASGI config for marks_projects project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'marks_projects.settings')

# application = get_asgi_application()

# ------------------------new------------------

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from api.v1.ws_urlpatterns import urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'marks_projects.settings')

ws_application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(urlpatterns)
})
