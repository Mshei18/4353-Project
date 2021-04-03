from django.db import models

# Create your models here.
class Authentication(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=25)

class fuelQuote(models.Model):
    gallonsRequested = models.IntegerField(default=0)
    deliveryAddress = models.CharField(max_length=40)
    suggestedPrice = models.DecimalField(decimal_places=2,max_digits=10)
    totalAmount = models.DecimalField(decimal_places=2,max_digits=10)



  