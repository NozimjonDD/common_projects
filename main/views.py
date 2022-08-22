from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from main.validators import PhoneNumberChecker


class PhoneNumerCheckerView(APIView):
    def post(self, request, *args, **kwargs):

        number = request.data.get("number")
        print(15, number[3:5], type(number))
        is_humans = PhoneNumberChecker.is_humans_number(number[3:5])
        print(is_humans)

        return Response({"ok"}, status=status.HTTP_200_OK)
