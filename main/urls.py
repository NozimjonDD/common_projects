from django.urls import path

from main import views

urlpatterns = [
    path('number/', views.PhoneNumerCheckerView.as_view()),
]