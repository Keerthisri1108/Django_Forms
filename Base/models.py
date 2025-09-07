from django.db import models

# Create your models here.
class Unemployment(models.Model):
     name=models.CharField(max_length=100)
     designation=models.CharField(max_length=100)
     experience=models.FloatField()
     current_ctc=models.FloatField()
     email=models.EmailField()
     phone=models.CharField(max_length=10)
     address=models.CharField(max_length=200)
