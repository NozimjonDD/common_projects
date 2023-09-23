import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from api.v1.ws_urlpatterns import urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'marks_projects.settings')

ws_application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(urlpatterns)
})
