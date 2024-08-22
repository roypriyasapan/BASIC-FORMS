from django.db import models

# Create your models here.
class Registration(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=20)
    email=models.EmailField()
    contact=models.IntegerField()