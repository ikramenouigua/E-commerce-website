from django.db import models
from django.db.models.fields.files import ImageField

class Product(models.Model):
    CATEGORY = (
			('1', 'Accessoirs'),
			('2', 'Sacs'),
            ('3', 'Chaussures'),
            ('4', 'Robes'),
			) 
    name=models.CharField(max_length=100)
    description = models.TextField()
    photo = ImageField()
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    price = models.FloatField(null=True)

    def __str__(self):
        return self.name

    def get_display_price(self):
        return "{0:.2f}".format(self.price/10)
