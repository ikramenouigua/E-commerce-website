from django.db import models
from django.db.models.fields import EmailField
from django.db.models.fields import EmailField
from django.db.models.fields.files import ImageField
from phone_field import PhoneField


# Create your models here.
class person(models.Model):
    CHOICES=(
        ('Seller','Seller'),
        ('Buyer','Buyer'),
        ('Both','Both'),
    )
    name=models.CharField(max_length=50,null=True)
    email=models.EmailField(max_length=50,null=True)
    password=models.CharField(max_length=50,null=True)

    trade=models.CharField(max_length=50,null=True,choices=CHOICES)
   
  
   


   

