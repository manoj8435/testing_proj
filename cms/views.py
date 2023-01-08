from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def show(request):
    return Response("Hello World")


class ShowView(APIView):
    
    def get(self, request):
        return Response("Hello World")