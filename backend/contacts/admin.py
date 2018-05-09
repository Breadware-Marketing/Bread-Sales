from django.contrib import admin

from .models import LeadSource, Company, Contacts
# Register your models here.

admin.site.register(LeadSource)
admin.site.register(Company)
admin.site.register(Contacts)