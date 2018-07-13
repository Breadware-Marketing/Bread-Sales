from django.db import models

# Create your models here.

class ModelBase(models.Model):
    """
    Base Model for all Models
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class LeadSource(ModelBase):
    """
    LeadSource
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        """Return the Lead Source info"""
        return "{}".format(self.name)

class Company(ModelBase):
    """
    Companies
    """

    name = models.CharField(max_length=255, unique=False, default='')
    linkedin_url = models.CharField(max_length=1024, unique=True, default='')
    website = models.CharField(max_length=1024, unique=False, default='')
    geography = models.CharField(max_length=255, unique=False, default='')
    industry = models.CharField(max_length=255, unique=False, default='')
    company_headcount = models.CharField(max_length=255, unique=False, default='')
    employees_on_linkedin = models.CharField(max_length=255, unique=False, default='')
    companyId = models.CharField(max_length=255, unique=False, default='')
    employee_first_name = models.CharField(max_length=255, unique=False, default='')
    employee_last_name = models.CharField(max_length=255, unique=False, default='')
    employee_email = models.CharField(max_length=255, unique=False, default='')
    employee_position = models.CharField(max_length=255, unique=False, default='')

    def __str__(self):
        """Return the Company info"""
        return "{}".format(self.name)

class Contacts(ModelBase):
    """
    Individual Contacts At Companies
    """

    name = models.CharField(max_length=255, unique=True)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255, default='')
    title = models.CharField(max_length=255, default='')
    website = models.URLField(null=True, blank=True, default='')
    email = models.CharField(max_length=255, default='', blank=True, null=True)

    def __str__(self):
        """Return the Company info"""
        return "{}".format(self.name)
