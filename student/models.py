from django.db import models

class student(models.Model):
    first_name =models.CharField(max_length=30)
    second_name=models.CharField(max_length=30)
    last_name= models.CharField(max_length=30)
    reg_no =models.CharField(max_length=10)
    email =models.EmailField(max_length=100)

