from django.db import models
import uuid #univeral unique identifier
from django.contrib.auth.models import User
from datetime import datetime
from django_countries.fields import CountryField

# Create your models here.
class Company (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_name =models.CharField(max_length=100)
    user_id =models.ForeignKey(User, on_delete=models.CASCADE)
    company_urls =models.CharField(max_length=1000)
    
    def __str__(self) -> str:
        return self.company_name

class Company_policies (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_id=models.ForeignKey(Company, on_delete=models.CASCADE)
    business_platform=models.TextField()
    product_services=models.TextField()
    date_issued= models.DateField(default=datetime.today)

    def __str__(self):
         return self.business_platform + ' ' + str(self.id) + ' - ' + str(self.date_issued)

class Company_policy_contacts (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    company_phone_number=models.CharField(max_length=17)
    company_email=models.EmailField(max_length=100)
    company_country =CountryField(blank=True)

    def __str__(self):
        return self.owner + " "+ (self.company_phone_number)
