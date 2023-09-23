from django.urls import path, include

# from user.token import MyTokenObtainPairView

urlpatterns = [
    path('admin/', include('api.v1.admin.urls')),
    path('general/', include('api.v1.general.urls')),
    path('site/', include('api.v1.site.urls')),
    path('for_test/', include('api.v1.for_test.urls')),
    # path('auth/token/', MyTokenObtainPairView.as_view()),
]
