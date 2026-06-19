from django.db import models

class customerdetails(models.Model):
    cname=models.CharField(max_length=150)
    cphone=models.CharField(max_length=150)
    cemail=models.CharField(max_length=150)
    cpassword=models.CharField(max_length=150)

