from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ClientProfile, fuelQuote, Authentication
from .forms import ClientForm, AuthenticationForm, FuelQuoteForm, RegisterForm
from django.contrib.auth.models import User


from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required


# register
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)       
        if form.is_valid():
            form.save()  
            user = form.cleaned_data.get('username')
            messages.success(request, "the account was created for " + user) 
            return redirect('/login/')  

    else:
        form = RegisterForm()
    return render(request, 'signup.html', {'form': form})

# login
def loginPage(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)       
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            

            if user is not None:
                login(request, user)
                # post = form.save()
                # post.save() 
                form.save()
                return redirect('client') 
            else:
                messages.error(request,'username OR password is not correct')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# logout
def logoutUser(request):
    logout(request)
    return redirect('login')

# home
@login_required(login_url = 'login')
def home(request):
    return render(request, 'home.html')

#client
@login_required(login_url = 'login')
def client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)       
        if form.is_valid():
            post = form.save()
            post.save()  
            return redirect('/fuelquoteform/')    
    else:
        form = ClientForm()
    return render(request, 'client.html', {'form': form})

# fuel quote form
@login_required(login_url = 'login')
def fuelquoteform(request):
    a1 = ClientProfile.objects.latest('id').address1
    a2 = ClientProfile.objects.latest('id').address2
    city = ClientProfile.objects.latest('id').city
    state = ClientProfile.objects.latest('id').state
    zip = ClientProfile.objects.latest('id').zipCode
    
    
    latest_entry = a1 + " " + a2 + " " + city + " " + state + " " + str(zip)
            
    if request.method == "POST":
        form = FuelQuoteForm(request.POST) 
        if form.is_valid():
            if 'Get_Quote' in request.POST:
                form.clean_suggPrice()
                form.clean_total()
                return render(request, 'fuelquoteform.html', context={"form": form})

            elif 'Submit_Quote' in request.POST:
                
                post = form.save()
                post.suggestedPrice = form.clean_suggPrice()
                post.totalAmount = form.clean_total() 
                current_user = request.user
                latest_user = Authentication.objects.latest('id').username
                post.username = latest_user
                post.save()
                return redirect('/fuelquotehistory/')
    else:
        form = FuelQuoteForm()
    
    return render(request, 'fuelquoteform.html', {'form': form, })



# fuel quote history
@login_required(login_url = 'login')
def fuelquotehistory(request):
    current_user = request.user
    all_entries = fuelQuote.objects.filter(username=current_user).values()
    context= {'all_entries': all_entries}
    
    return render(request, 'fuelquotehistory.html', context)


