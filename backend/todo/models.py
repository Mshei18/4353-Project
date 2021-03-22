from django.db import models
# from django.core.exceptions import MinValueValidator, MaxValueValidator
from django.core.validators import MinLengthValidator


# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title


class ClientProfile(models.Model):
    fullName = models.CharField(max_length=50,blank=False )
    address1 = models.CharField(max_length=100, blank=False)
    address2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=False)
    state = models.CharField(max_length=2, blank=False)
    zipCode = models.CharField(max_length =9, blank=False, validators=[MinLengthValidator(5)])

    def _str_(self):
        return self.fullName