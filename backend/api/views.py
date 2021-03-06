from django.shortcuts import render

from rest_framework import generics
from .serializers import CompanySerializer, ContactSerializer
from contacts.models import Company, Contacts

# Create your views here.

class CreateCompanyView(generics.ListCreateAPIView):
    """
    This Class Defines the Create Behavior of the Rest API
    """

    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def perform_create(self, serializer):
        """Save the Post data when creating a new Company."""
        serializer.save()

class DetailsCompanyView(generics.RetrieveUpdateDestroyAPIView):
    """
    This Class handles GET, PUT, PATCH and DELETE requests
    """

    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CreateContactView(generics.ListCreateAPIView):
    """
    This Class Defines the Create Behavior of the Rest API
    """

    queryset = Contacts.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        """Save the Post data when creating a new Contact."""
        serializer.save()

class DetailsContactView(generics.RetrieveUpdateDestroyAPIView):
    """
    This Class handles GET, PUT, PATCH and DELETE requests
    """

    queryset = Contacts.objects.all()
    serializer_class = ContactSerializer