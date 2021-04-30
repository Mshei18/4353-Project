from django.db import models
import datetime
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from decimal import *


STATE_CHOICES = (('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'))

class ClientProfile(models.Model):
    fullName = models.CharField('Full Name', max_length=50,blank=False )
    address1 = models.CharField('Address 1', max_length=100, blank=False, null=True)
    address2 = models.CharField('Address 2', max_length=100, blank=True, null=True, default='')
    city = models.CharField('City', max_length=100, blank=False)
    state = models.CharField('State', max_length=21, choices=STATE_CHOICES, default='')
    zipCode = models.CharField('Zip Code', max_length =9, validators=[MinLengthValidator(5)], default='')

class Authentication(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=25)

class Register(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=25)
    verify_password = models.CharField(max_length=25)

class fuelQuote(models.Model):
    gallonsRequested = models.IntegerField('Gallons Requested', default=0, )
    deliveryAddress = models.CharField('Delivery Address', max_length=100, default='', blank= True)
    deliveryDate =  models.DateField('Delivery Date')
    suggestedPrice = models.DecimalField('Suggested Price per Gallon',decimal_places=7, max_digits=100, default=Decimal('0.00000'))
    totalAmount = models.DecimalField('Total Amount', decimal_places=7, max_digits=100, default=Decimal('0.00000'))
    # username = models.ForeignKey(Authentication, on_delete=models.CASCADE, null=True, blank=False)
    username = models.CharField(max_length=20, null=True, blank=False)

    # user = models.CharField('user', max_length=20, default ="")


class PricingModule:
    def __init__(self, galls_req):
        self.current_price = 1.50
        self.galls_requested = galls_req
        # self.user = ClientProfile.objects.latest('id') 
        # u = ClientProfile.objects.latest('id') 


    def state_factor(self):
        if ClientProfile.objects.latest('id').state == 'TX':
            return 0.02
        else:
            return 0.04

    def rate_history_factor(self):
        all_entries = fuelQuote.objects.all()
        if not all_entries:
            doesHistoryExist = False
        else:
            doesHistoryExist = True

        if doesHistoryExist:
            return 0.01 
        else:
            return 0.0

    def galls_requested_factor(self):
        if int(self.galls_requested) > 1000:
            return 0.02
        else:
            return 0.03

    def margin(self):
        location_factor = self.state_factor()
        rate_history_factor = self.rate_history_factor()
        galls_requested_factor = self.galls_requested_factor()

        company_profit_factor = .10

        margin = round((self.current_price * (location_factor - rate_history_factor + galls_requested_factor + company_profit_factor)),3)

        print("location_factor", location_factor)
        print("ratehistory_factor", rate_history_factor)
        print("gallrequested_factor", galls_requested_factor)

        rounded_margin = round(margin, 3)
        print("margin", margin)
        print("rounded margin", rounded_margin)

        return rounded_margin
    
    def calculate(self):
        
        result = (self.margin() + self.current_price) * self.galls_requested
        print("result", result)
        return result
