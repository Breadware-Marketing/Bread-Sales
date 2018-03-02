from django.test import TestCase
from .models import Company, Contacts

# Create your tests here.

class SampleData():
    """
    Create all sample Data
    """

    def create_company(self, 
        name="Breadware", 
        description ="""Breadware provides a complete IoT product development solution for businesses at 
        a speed and reliability unmatched in the industry. Our expertise includes PCB development, firmware 
        and cloud integrations. We have built IoT electronics for our clients who have been successful in 
        the medical, industrial, wearable, robotics and agricultural markets and do everything from small 
        prototype runs to large production runs. """,
        info_url='https://www.linkedin.com/sales/company/6651289/people', 
        website='https://breadware.com/',
        address='450 Sinclair St',
        address_2='', 
        city='Reno', 
        country='United States', 
        employees=20):

        return Company.objects.create(
            name=name, 
            description=description,
            info_url=info_url,
            website=website,
            address=address,
            address_2=address_2,
            city=city,
            country=country,
            employees=employees
        )
    
    def create_contact(self,
        name = "Eduardo Morales",
        location = "Reno, Nevada",
        title = "Marketing Manager",
        email = "emorales@breadware.com"):

        return Contacts.objects.create(
            name=name, 
            company=self.create_company(),
            location=location,
            title=title,
            email=email
        )

class CompanyModelTestCase(SampleData, TestCase):
    """
    This class defines the test suite for the Company model.
    """

    def test_model_can_create_a_company(self):
        """Test the Company Model can Create a Model"""
        old_count = Company.objects.count()
        self.create_company()
        new_count = Company.objects.count()
        self.assertNotEqual(old_count, new_count)

class ContactModelTestCase(SampleData, TestCase):
    """
    This class defines the test suite for the Contacts model.
    """

    def test_model_can_create_a_contact(self):
        """Test the Contact Model can Create a Model"""
        old_count = Contacts.objects.count()
        self.create_contact()
        new_count = Contacts.objects.count()
        self.assertNotEqual(old_count, new_count)