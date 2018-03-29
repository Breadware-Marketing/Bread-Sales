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

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(default='')
    info_url = models.URLField(null=True, blank=True, max_length=1024)
    website = models.URLField(null=True, blank=True, max_length=1024)
    address = models.CharField(null=True, blank=True, max_length=255)
    address_2 = models.CharField(null=True, blank=True, max_length=255)
    city = models.CharField(default='', max_length=255)
    country = models.CharField(default='', max_length=255)
    employees = models.IntegerField(null=True, blank=True)
    tradeshow_booth = models.CharField(default='', max_length=255)
    lead_source = models.ForeignKey(LeadSource, on_delete=models.CASCADE)

    def __str__(self):
        """Return the Company info"""
        return "{}".format(self.name)

class Contacts(ModelBase):
    """
    Individual Contacts At Companies
    """

    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255, default='')
    title = models.CharField(max_length=255, default='')
    website = models.URLField(null=True, blank=True, default='')
    email = models.CharField(max_length=255, default='', blank=True, unique=True)

    def __str__(self):
        """Return the Company info"""
        return "{}".format(self.name)
