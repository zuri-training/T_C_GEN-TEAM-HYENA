from django.contrib import admin
from .models import  Company, Company_policies ,Company_policy_contacts

# Register your models here.
admin.site.register(Company_policies )
admin.site.register(Company)
admin.site.register(Company_policy_contacts)