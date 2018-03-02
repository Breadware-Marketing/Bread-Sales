from rest_framework import serializers
from contacts.models import Company, Contacts

class CompanySerializer(serializers.ModelSerializer):
    """
    Serializer to map the Company Model Instance into JSON Format.
    """

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Company
        fields = ('name', 'description', 'info_url', 'website', 'address', 'address_2', 'city', 'country', 'employees')
        read_only_fields = ('created_at', 'updated_at')

class ContactSerializer(serializers.ModelSerializer):
    """
    Serializer to map the Contact Model Instance into JSON Format.
    """

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Contacts
        fields = ('name', 'company', 'location', 'title', 'email')
        read_only_fields = ('created_at', 'updated_at')