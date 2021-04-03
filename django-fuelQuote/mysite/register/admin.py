from django.contrib import admin

# Register your models here.
from .models import Authentication
from .models import fuelQuote

admin.site.register(Authentication)
admin.site.register(fuelQuote)