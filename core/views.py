from typing import Any

from django.contrib.auth import login
from django.shortcuts import render
from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from core.models import User
from core.serializers import UserCreateSerializer, UserLoginSerializer


class UserCreateView(generics.CreateAPIView):
    model = User
    serializer_class = UserCreateSerializer


class UserLoginView(generics.CreateAPIView):
    model = User
    serializer_class = UserLoginSerializer

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        login(request=request, user=serializer.save())
        return Response(serializer.data)
