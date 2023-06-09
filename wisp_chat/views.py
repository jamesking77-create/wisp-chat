from http.client import HTTPResponse

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response

from rest_framework.views import APIView

from wisp_chat.serializers import UserSerializer


class Register(APIView):
    def post(self, request):
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
        return Response(serializers.data)
