from django.test import TestCase
from contacts.models import Company, Contacts
from contacts.tests import SampleData

from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

# Create your tests here.

class ViewCompanyTestCase(TestCase):
    """
    Test Suite for the Company API Views
    """
    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.company_data = {
            "name":"Breadware", 
            "description":"Breadware provides a complete IoT product development solution for businesses at a speed and reliability unmatched in the industry. Our expertise includes PCB development, firmware and cloud integrations. We have built IoT electronics for our clients who have been successful in the medical, industrial, wearable, robotics and agricultural markets and do everything from small prototype runs to large production runs.",
            "info_url":"https://www.linkedin.com/sales/company/6651289/people", 
            "website":"https://breadware.com/",
            "address":"450 Sinclair St",
            "address_2":"", 
            "city":"Reno", 
            "country":"United States", 
            "employees":20
        }
        self.response = self.client.post(
            reverse("create"),
            self.company_data,
            format="json"
        )
    
    def test_api_can_create_a_company(self):
        """Test the api can create a company."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

class ViewContactsTestCase(TestCase, SampleData):
    """
    Test Suite for the Contacts API Views
    """
    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.contact_data = {
            "name":"Eduardo Morales",
            "company": 1,
            "location":"Reno, Nevada",
            "title":"Marketing Manager",
            "email":"emorales@breadware.com"
        }
        self.response = self.client.post(
            reverse("create"),
            self.contact_data,
            format="json"
        )
    
    def test_api_can_create_a_contact(self):
        """Test the api can create a company."""
        import pdb; pdb.set_trace()
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)