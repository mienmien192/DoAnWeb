# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
# Create your views here.


def show(request):
    queryset = User.objects.all()
    user = User.objects.get()


