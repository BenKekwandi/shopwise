from typing import Iterable
from django.db import models
from django.contrib.auth.models import User
from app.utils import get_boravin_link_data, get_beyaz_link_data
# Create your models here.
CATEGORY_CHOICES=[
    ('LA','Laptops'),
    ('HM','Home Appliances'),
    ('PH','Phones'), 
    ('TS','Televisions and sound'),
    ('PR','Peripherials'), 
    ('GP','Gaming Products'),

]

class Link(models.Model):
    name=models.CharField(max_length=220,blank=True)
    url_boravin=models.URLField()
    url_beyaz=models.URLField()
    boravin_price=models.CharField(max_length=220,blank=True,null=False)
    beyaz_price=models.FloatField(blank=True,null=False)
    price_difference=models.FloatField(default=0)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2,null=False)
    product_image=models.ImageField(upload_to='product',null=False)

    def __str__(self):
        return str(self.name)
    class Meta:
        ordering=('name',)

    def save(self,*args,**kwargs):
        name, boravin_price = get_boravin_link_data(self.url_boravin)
        beyaz_price = get_beyaz_link_data(self.url_beyaz)
        
        # Calculate the price difference
        price_difference = abs(float(boravin_price) - beyaz_price)
        
        self.name = name
        self.boravin_price = f"{boravin_price:.2f}"  # Save formatted price
        self.beyaz_price = beyaz_price
        self.price_difference = price_difference
        
        super().save(*args, **kwargs)

class Customer(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    name= models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    mobile=models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Wish(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Link, on_delete=models.CASCADE)
    def _str_(self):
        return self.name 