# from typing_extensions import Required
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=50,unique=True)
    phone_no = models.CharField(max_length=12,blank=True)

    def __str__(self):
        return self.username

class Restaurant(models.Model):
    name= models.CharField(max_length=50)
    contact= models.CharField(max_length=15)
    address= models.CharField(max_length=100)


    def __str__(self):  
        return self.name

class Menu(models.Model):
    restaurant_name= models.ForeignKey(Restaurant, on_delete= CASCADE)
    items= models.CharField(max_length=50)
    price= models.IntegerField()

class Order(models.Model):
    user_name= models.CharField( max_length=60)
    user_contact= models.CharField(max_length=20)
    user_email= models.EmailField(max_length=30)
    user_address=models.CharField(max_length=100)
    item_name= models.CharField(max_length=50, default= None)
    restaurant_name= models.CharField(max_length=50)

    

