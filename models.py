from django.db import models

def fuelQuoteHistory():
    GallonsRequested = 100
    DeliveryAddress = "111 happy road"
    DeliveryDate = "11/11/1111"
    PricePerG = 1.98
    TotalPrice = PricePerG * GallonsRequested

    #supposed to grab from form when backend is complete rn it is hard coded.

    print(GallonsRequested + " " + DeliveryAddress + " " + DeliveryDate + " " + PricePerG + " " + TotalPrice)



class Pricing(models.Model):
    GallonsRequested = models.floatField(max_length=120)
    DeliveryAddress = models.charField(max_length=120)
    DeliveryDate = models.dateField(max_length=120)
    PricePerG = models.floatField(max_length=120)
    TotalPrice = models.floatField(max_length=120)

   

    def _str_(self):
        return self.title