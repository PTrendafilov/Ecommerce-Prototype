from django.db import models
from numpy import number
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=30)
    details = models.TextField()
    image = models.ImageField(upload_to='pics')
    price = models.FloatField()
    old_price = models.FloatField()
    discount = models.BooleanField(default=False)

class Menu(models.Model):
    logo = models.ImageField(upload_to='pics')
    page1 = models.CharField(max_length=20)
    page2 = models.CharField(max_length=20)
    page3 = models.CharField(max_length=20)
    page4 = models.CharField(max_length=20)
    cart=models.BooleanField(default=True)
    search=models.BooleanField(default=True)
    sign_up=models.BooleanField(default=True)

class Notice(models.Model):
    red_head=models.TextField()
    black_head=models.TextField()
    details=models.TextField()

class Site(models.Model):
    logo = models.ImageField(upload_to='pics')
    notice_image=models.ImageField(upload_to='pics')

class Order(models.Model):
    user = models.CharField(max_length=100)
    adress = models.TextField()
    email=models.EmailField(max_length = 128)
    phone_number=models.CharField(max_length=30)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    details = models.TextField()
    price = models.FloatField()
    is_ready=models.BooleanField(default=False)
    
    