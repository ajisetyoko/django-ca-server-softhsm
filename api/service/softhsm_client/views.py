from django.shortcuts import render
from rest_framework import views, status
from .utils import AllowAll
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, status, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Key

import logging

logger = logging.getLogger(__name__)


class KeyManagement(viewsets.ModelViewSet):
    permission_classes = (AllowAll,)
    queryset = Key.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        return super().get_queryset()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    # def l (self, request):

    #     logger.info("Something")
    #     return Response(data="Hellow", status=status.HTTP_200_OK)


class TestAuthentication(views.APIView):
    permission_classes = IsAuthenticated

    def get(self):
        print("Test Authentication")
        return Response(data="Hellow", status=status.HTTP_200_OK)
