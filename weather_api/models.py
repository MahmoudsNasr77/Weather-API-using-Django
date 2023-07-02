from django.db import models

# Create your models here.
class city_info(models.Model):
    city=models.CharField(max_length=250)
    contery=models.CharField(max_length=250)
    temperature=models.DecimalField(max_digits=4, decimal_places=2)
    decription=models.TextField(max_length=250)
