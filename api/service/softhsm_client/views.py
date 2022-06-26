from django.shortcuts import render
from rest_framework import views, status
from .utils import AllowAll
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
from rest_framework import viewsets, status, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Key
from .serializers import KeySerializer
from knox.views import LoginView as KnoxLoginView
from knox.auth import TokenAuthentication

import logging

logger = logging.getLogger(__name__)


class LoginView(KnoxLoginView):
    authentication_classes = [BasicAuthentication]


class KeyManagement(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = (AllowAll,)
    serializer_class = KeySerializer
    queryset = Key.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        return super().get_queryset()

    def list(self, request, *args, **kwargs):
        logger.info("Hynbnbnb")
        return super().list(request, *args, **kwargs)


class Test(views.APIView):
    authentication_classes = [BasicAuthentication]

    permission_classes = [
        AllowAll,
    ]

    def get(self, request):
        print("Test Authentication")
        return Response(data="Hellow", status=status.HTTP_200_OK)
