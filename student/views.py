from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from student.models import Registration

from student.serializers import Registrationserializer


class RegistrationList(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format = None):
        registration = Registration.objects.all()
        serializer = Registrationserializer(registration, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Registrationserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

