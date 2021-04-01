from django.db import models
from django.contrib.auth.models import User
from django.db import migrations, models
#from django.db.models.fields import EmailField
#from django.db.models.fields.files import ImageField
from dataclasses import dataclass, field
from django.utils import timezone
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from datetime import datetime


# Create your models here.
class Admin(models.Model):
    
    name= models.CharField(max_length=50)
    email= models.EmailField(validators=[validate_email],max_length=254)
    #email= models.EmailField(max_length=254)
    phone = models.CharField(max_length=10)
    nb_weekly_prod_vendus=models.IntegerField() 
    nb_clients=models.IntegerField()
    nb_vendeurs=models.IntegerField()

    def __str__(self):
        return self.name





class Client(models.Model):
    
    name= models.CharField(max_length=50)
    email= models.EmailField(validators=[validate_email],max_length=254)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Seller(models.Model):
    name=models.CharField(max_length=50 )
    description=models.CharField(max_length=200 )
    photo = models.ImageField()
    genre = models.CharField(max_length=50 )
    email= models.EmailField(validators=[validate_email],max_length=254)
    phone = models.CharField(max_length=50)
    #phone = models.CharField(max_length=10)
    nbElementProd = models.PositiveBigIntegerField(blank=True )
    resteProd = models.PositiveBigIntegerField(blank=True )
    profitProd = models.FloatField(blank=True )      
    
    def __str__(self):
        return self.name


class Product(models.Model):
    idProduct=models.IntegerField()
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=200 , blank=True , null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    idSeller=models.ForeignKey(Seller,default=-1 , verbose_name='seller' , on_delete=models.CASCADE)
    image1= models.ImageField(blank=True , null=True)
    image2=models.ImageField(blank=True , null=True)
    image3= models.ImageField(blank=True , null=True)
    status =models.CharField(max_length=200 , blank=True , null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    idOrder=models.IntegerField(primary_key=True , auto_created=True)
    idClient=models.ForeignKey(Client, default=-1 , verbose_name='client' ,on_delete=models.CASCADE)
    idSeller=models.ForeignKey(Seller, default=-1 , verbose_name='seller' , on_delete=models.CASCADE)
    idProduct=models.ForeignKey(Product,  default=-1 , verbose_name='product' , on_delete=models.CASCADE)
    status=models.CharField(max_length=200 , blank=True , null=True)
    qty=models.IntegerField(blank=True , null=True)
    due_amount=models.IntegerField(blank=True , null=True)
    dateCreated=models.DateTimeField("date ceated" , default=datetime)

    def __str__(self):
        return self.idOrder

    
