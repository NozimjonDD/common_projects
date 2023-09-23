from django.urls import path

from api.v1.for_test import views

urlpatterns = [
    # Description
    path('teacher/create/', views.TeacherCreateAPIView.as_view()),
    path('teacher/<int:pk>/update/', views.TeacherUpdateAPIView.as_view()),

]
