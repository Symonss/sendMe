# Here we are simply desghning how our database tables will look like
# class names translates to table names while fields become columns.
# functions inside classes give  actions that can be undertakent on these tables
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.html import escape, mark_safe

#oberriding the user class
class User(AbstractUser):
    is_employer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    is_regional_admin = models.BooleanField(default=False)
    is_admin =models.BooleanField(default=False)
    first_name= models.CharField(max_length=50, default='Peterson')
    last_name= models.CharField(max_length=50, default='Peterson')
    phone = models.IntegerField(default='0792799958')
    email= models.CharField(max_length=50, default='yourmail@gmail.com')


class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name= models.CharField(max_length=50, default='Peterson')
    last_name= models.CharField(max_length=50, default='Peterson')
    phone = models.IntegerField(default='0792799958')
    email= models.CharField(max_length=50, default='yourmail@gmail.com')
    #oder = models.ForeignKey(Order, on_delete=models.CASCADE, primary_key=True)
class RegionalAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name= models.CharField(max_length=50, default='Peterson')
    last_name= models.CharField(max_length=50, default='Peterson')
    phone = models.IntegerField(default='0792799958')
    email= models.CharField(max_length=50, default='yourmail@gmail.com')

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name= models.CharField(max_length=50, default='Peterson')
    last_name= models.CharField(max_length=50, default='Peterson')
    phone = models.IntegerField(default='0792799958')
    email= models.CharField(max_length=50, default='yourmail@gmail.com')
