from django.shortcuts import render
from rest_framework import views, status
from .utils import AllowAll
from rest_framework.response import Response

class KeyManagement(views.APIView):
    permission_classes = (AllowAll,)

    def get(self, request):
        print("Something")
        return Response(data="Hellow", status=status.HTTP_200_OK)

