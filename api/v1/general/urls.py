from django.urls import path, include

urlpatterns = [
    path('g/', include('api.v1.admin.urls')),

]
