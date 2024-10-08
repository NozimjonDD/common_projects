"""marks_projects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from api.v1.for_test.views import home
from marks_projects import settings
from marks_projects.settings import DEBUG
from django.urls import path, include

urlpatterns = [
    path('mark/', admin.site.urls),
    path('api/v1/', include('api.v1.urls')),
    path('api/main/', include('main.urls')),
    path('websocket/', include('api.v1.ws_urlpatterns')),
    path('', home, name="home"),

]
if DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
