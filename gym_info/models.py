from django.db import models

# Create your models here.

class Login(models.Model):
    email = models.EmailField(max_length=100, null=True)
    password = models.CharField(max_length=50,null=True)
class Signup(models.Model):
    name = models.CharField(max_length=50,null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=10,null=True)
    number = models.IntegerField(null=True)
    #email = models.EmailField(null=True)
    password = models.CharField(max_length=50,null=True)
