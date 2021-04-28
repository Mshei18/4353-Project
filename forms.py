from django import forms
from .models import ClientProfile, Authentication, fuelQuote, Register
from .models import PricingModule
from decimal import Decimal
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ClientForm(forms.ModelForm):

    class Meta:
        model = ClientProfile
        fields = ('fullName', 'address1',  'address2', 'city', 'state', 'zipCode',)
    
class DateInput(forms.DateInput):
    input_type = 'date'

class AuthenticationForm(forms.ModelForm):

    class Meta:
        model = Authentication
        fields = ('username', 'password',)

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "password1", "password2", )

def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        
        if commit:
            user.save()
        return user

class FuelQuoteForm(forms.ModelForm):

    class Meta:
        model = fuelQuote
        fields = ('gallonsRequested',  'deliveryAddress', 'deliveryDate', 'suggestedPrice', 'totalAmount',)
        widgets = {
        'deliveryDate': DateInput(format=('%m/%d/%Y'), attrs={ 'placeholder':'Select a date', 'type':'date', 'class': 'datepicker'}),
        }

    def clean_suggPrice(self):
        galls = self.cleaned_data['gallonsRequested']
        module = PricingModule(galls)


        sugg_price = module.margin()
        print("SUGG1", sugg_price)

        final_sugg_price = Decimal(sugg_price + 1.5)
        round_sugg_price = round(final_sugg_price, 5)
        self.fields['suggestedPrice'].initial = round_sugg_price

        print("SUGG2", round_sugg_price)
        return round_sugg_price

    def clean_total(self):
        galls = self.cleaned_data['gallonsRequested']
        module = PricingModule(galls)

        dec_total = Decimal(module.calculate())
        total = round(dec_total, 3)
        self.fields['totalAmount'].initial = total
        print("totalAmount", total)
        return total


    def __init__(self, *args, **kws):
       
        super().__init__(*args, **kws)
        
        a1 = ClientProfile.objects.latest('id').address1
        a2 = ClientProfile.objects.latest('id').address2
        city = ClientProfile.objects.latest('id').city
        state = ClientProfile.objects.latest('id').state
        zip = ClientProfile.objects.latest('id').zipCode
        latest_entry = a1 + " " + a2 + " " + city + " " + state + " " + str(zip)
        self.fields["deliveryAddress"].initial = latest_entry
        self.fields["suggestedPrice"].initial = 0.0
        self.fields["totalAmount"].initial = 0.0
        self.fields["gallonsRequested"].initial = 1.0
       
        self.fields['deliveryAddress'].disabled = True
        self.fields['suggestedPrice'].disabled = True
        self.fields['totalAmount'].disabled = True