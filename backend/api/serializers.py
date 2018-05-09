from rest_framework import serializers
from contacts.models import Company, Contacts

class CompanySerializer(serializers.ModelSerializer):
    """
    Serializer to map the Company Model Instance into JSON Format.
    """

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Company
        fields = ('id', 'name', 'linkedin_url', 'website', 'geography', 'industry', 'company_headcount', 'employees_on_linkedin', 'companyId')
        read_only_fields = ('created_at', 'updated_at')

class ContactSerializer(serializers.ModelSerializer):
    """
    Serializer to map the Contact Model Instance into JSON Format.
    """

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Contacts
        fields = ('name', 'company', 'location', 'title', 'email', 'website')
        read_only_fields = ('created_at', 'updated_at')
