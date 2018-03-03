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

    name = models.CharField(max_length=255)
    description = models.TextField(default='')
    info_url = models.URLField(max_length=1024, unique=True)
    website = models.URLField(default='', max_length=1024, unique=True)
    address = models.CharField(default='', max_length=255)
    address_2 = models.CharField(default='', blank='true', max_length=255)
    city = models.CharField(default='', max_length=255)
    country = models.CharField(default='', max_length=255)
    employees = models.IntegerField(null=True, blank=True)
    lead_source = models.ForeignKey(LeadSource, on_delete=models.CASCADE)

    def __str__(self):
        """Return the Company info"""
        return "{}".format(self.name)

class Contacts(ModelBase):
    """
    Individual Contacts At Companies
    """

    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    location = models.CharField(max_length=255, default='', )
    title = models.CharField(max_length=255, default='', )
    email = models.EmailField(default='', unique=True)

    def __str__(self):
        """Return the Company info"""
        return "{}".format(self.name)
