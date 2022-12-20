from django.urls import path, include

from api.v1.site import views

urlpatterns = [
    # Description
    path('create/', views.SiteRequestCheckingCreationView.as_view()),

]