from operator import mod
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_tenant = models.BooleanField(default=False)
    is_landlord = models.BooleanField(default=False)

class Tenant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Rent(models.Model):
    name = models.CharField(default="Please enter your name", max_length=100)
    house_no = models.CharField(default="Please enter your house number", max_length=100)
    amount_paid = models.IntegerField()
    

class RentDetails(models.Model):
    pass


# Create your models here.
class Payment(models.Model):
    pass