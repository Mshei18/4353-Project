from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm  
from .models import fuelQuote, ClientProfile, PricingModule
from .forms import RegisterForm, ClientForm, FuelQuoteForm, Authentication
import datetime

from django.test.client import Client


class Test_login(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='username', password='password')

    def test_loginSuccess(self):
        response = self.client.post('/login/', {'username': 'username', 'password': 'password'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/client/')

    def test_loginUnsuccess(self):
        response = self.client.post('/login/', {'username': 'username2', 'password': 'password2'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertContains(response, 'username OR password is not correct')
        form = AuthenticationForm()
        self.assertFalse(form.is_valid())

class Test_login_route(TestCase):

    def test_statuscode(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        response = self.client.get('/login/')
        self.assertTemplateUsed(response, 'login.html')


class Test_register(TestCase):


    def test_get(self):
        response = self.client.get('/sign-up/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_RegisterSuccess(self):
        response = self.client.post('/sign-up/', {'username': 'testuser2',
        'password1': '1X<ISRUkw+tuK',
        'password2': '1X<ISRUkw+tuK'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/')

    def test_RegisterUnsuccess(self):
        response = self.client.post('/sign-up/', {'username':'testuser2',
        'password1':'1X<ISRUkw+tuK',
        'password2': 'wrongpassword' })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')
        self.assertContains(response, 'The two password fields didn’t match.')

        form = RegisterForm()
        self.assertFalse(form.is_valid())

class Test_logout(TestCase):

    def test_statuscode(self):
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 302)

    def test_template(self):
        response = self.client.get('/logout/')
        self.assertRedirects(response, '/login/')


class Test_home(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='user', password='test')

    def test_call_view_load(self):
        self.client.login(username='user', password='test')  # defined in fixture or with factory in setUp()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        
        
    def test_redirectCorrectly(self):
        response = self.client.get('/')
        self.assertRedirects(response, '/login/?next=/')

class Test_client(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='user', password='test')
        
        
    def test_redirectCorrectly(self):
        response = self.client.get('/client/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/client/')

    def test_call_view_load(self):
        self.client.login(username='user', password='test')  # defined in fixture or with factory in setUp()
        response = self.client.get('/client/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'client.html')

    def test_call_view_load_two(self): # test user fail?
        self.client.login(username='user', password='test2')  # defined in fixture or with factory in setUp()
        response = self.client.get('/client/')
        self.assertEqual(response.status_code, 302)
        
        form = AuthenticationForm()
        self.assertFalse(form.is_valid())

    def test_form(self):
        self.client.login(username='user', password='test')  # defined in fixture or with factory in setUp()
        form_data = {'fullName' : 'Jodie', 'address1' : '1234 Fawn Lane',  'address2' : 'Mailbox 23', 'city' : 'Frankfurt', 'state' : 'AL', 'zipCode': '12345'}
        form = ClientForm(data=form_data)
        self.assertTrue(form.is_valid())
        response = self.client.post('/client/', form_data)
        self.assertRedirects(response, '/fuelquoteform/')
        # ... # other tests relating forms, for example checking the form data
      

class Test_fqf(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='user', password='test')
        ClientProfile.objects.create(fullName = 'Jodie', address1 = '1234 Fawn Lane',  address2 = 'Mailbox 23', city = 'Frankfurt', state = 'AL', zipCode = 12345)
        
    def test_not_logged_in(self): 
        response = self.client.get('/fuelquoteform/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/fuelquoteform/')

    def test_form(self):
        self.client.login(username='user', password='test')
        form_data = {'gallonsRequested':'200',  'deliveryAddress':'1234 Fawn Lane', 'deliveryDate':'01/01/2001', 'suggestedPrice':'200', 'totalAmount':'200'}
        form = FuelQuoteForm(data=form_data)
        self.assertTrue(form.is_valid())
        response = self.client.post('/fuelquoteform/', form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fuelquoteform.html')

class Test_price_module(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='user', password='test')
        ClientProfile.objects.create(fullName = 'Jodie', address1 = '1234 Fawn Lane',  address2 = 'Mailbox 23', city = 'Frankfurt', state = 'TX', zipCode = 12345)
        fuelQuote.objects.create(gallonsRequested = 1500,  deliveryAddress ='1234 Fawn Lane', deliveryDate = '2001-01-01', suggestedPrice = 200, totalAmount =200)
        
    def test_price_module(self):
        self.client.login(username='user', password='test')
        res = PricingModule.state_factor('TX')
        self.assertEqual(res, 0.02)

        p = PricingModule(1500)

        history_true = p.rate_history_factor()
        self.assertEqual(history_true, 0.01)
        
        galls = p.galls_requested_factor()
        self.assertEqual(galls, 0.02)

        margin = p.margin()
        self.assertEqual(margin, 0.195)

        calculate = p.calculate()
        self.assertEqual(calculate, 2542.50)

class Test_fqh(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='user', password='test')
        
    def test_redirectCorrectly(self):
        response = self.client.get('/fuelquotehistory/')
        self.assertRedirects(response, '/login/?next=/fuelquotehistory/')

    def test_call_view_load(self): #test html used
        self.client.login(username='user', password='test')  # defined in fixture or with factory in setUp()
        response = self.client.get('/fuelquotehistory/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fuelquotehistory.html')

    
   