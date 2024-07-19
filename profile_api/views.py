from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    def get(self, request, format=None):
        an_api_view = [
            'Uses http api methods as functions (get,post,patch,put,delete)',
            'is similar to a traditional django view ',
            'gives you a most control over you application logic',
            'is mapped manually to URls',
        ]
        return Response({'an_api_view': an_api_view})

