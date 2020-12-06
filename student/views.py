from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from .models import Registration

from .serializers import Registrationserializer


class RegistrationSerializer(object):
    pass


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

class Registrationdetail(APIView):
        authentication_classes = []
        permission_classes = []

        def get_object(self, pk):
            return Registration.objects.get(id=pk)


        def get(self, request, pk, format=None):
            Registration = self.get_object(pk)
            serializer = Registrationserializer(Registration)
            return Response(serializer.data)

        def put(self, request, pk, format=None):
            Registration = self.get_object(pk)
            serializer = Registrationserializer(Registration, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, pk, format=None):
            Registration = self.get_object(pk)
            Registration.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)




