# from django.db import models

# # Create your models here.
# class Registration(models.Model):
#     fname=models.CharField(max_length=50)
#     lname=models.CharField(max_length=20)
#     email=models.EmailField()
#     contact=models.IntegerField()

# class login(models.Model):
#     email=models.EmailField()
#     contact=models.IntegerField()


from django.db import models

# Create your models here.
class StudentModel(models.Model):
    stu_name = models.CharField(max_length=50)
    stu_email = models.EmailField()
    stu_city = models.CharField(max_length=50)
    stu_mobile = models.IntegerField()
    stu_password = models.CharField(max_length=25)