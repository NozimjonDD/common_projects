from rest_framework.generics import (
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView
)
from rest_framework.permissions import AllowAny

from api.v1.site.serializers import SiteRequestCheckingCreationSeializer
from for_test.models import RequestCheckingCreation


class SiteRequestCheckingCreationView(CreateAPIView):
    permission_classes = [AllowAny, ]
    queryset = RequestCheckingCreation.objects.all()
    serializer_class = SiteRequestCheckingCreationSeializer
