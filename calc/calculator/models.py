from django.db import models

# Create your models here.

class Calculator(models.Model):
    numbers = models.JSONField(max_length=10)
    

