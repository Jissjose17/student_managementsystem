from django.db import models
from datetime import datetime

# Create your models here.
class studentform(models.Model):
    studentfname=models.CharField(max_length=50)
    studentlname=models.CharField(max_length=50)
    studentnumber=models.IntegerField()
    studentemail=models.EmailField()
    studentgender=models.CharField(max_length=50)
    studentdob=models.DateField()
    studentusername=models.CharField(max_length=50)
    studentpassword=models.IntegerField()
    studentaddress=models.CharField(max_length=50)
    studentcourse=models.CharField(max_length=50)
    studentimage=models.ImageField(upload_to='image/')

