from django.shortcuts import render
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from blogs.models import Blogger
from blogs.serializers import BloggerSerializer


class BloggerViewSet(
    CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet
):
    queryset = Blogger.objects.all()
    serializer_class = BloggerSerializer
