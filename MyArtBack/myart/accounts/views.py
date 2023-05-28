from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UserSerializer

class UserViewSet(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

