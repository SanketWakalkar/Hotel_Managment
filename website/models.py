from django.db import models

# Create your models here.

class Client(models.Model):
    name=models.CharField(max_length=200)
    Photo=models.CharField(max_length=200)
    review=models.IntegerField()
    is_active=models.BooleanField(default=False)
