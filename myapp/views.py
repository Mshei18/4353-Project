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
    try:
        existing_profile = request.user.profile
    except ClientProfile.DoesNotExist:
        existing_profile = None

    if request.method == "POST":
        form = ClientForm(request.POST, instance=existing_profile)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('/fuelquoteform/')
    else:
        form = ClientForm(instance=existing_profile)
    return render(request, 'client.html', {'form': form})

# fuel quote form
@login_required(login_url = 'login')
def fuelquoteform(request):
    try:
        request.user.profile
    except ClientProfile.DoesNotExist:
        messages.error(request, 'Please complete your profile first.')
        return redirect('/client/')

    if request.method == "POST":
        form = FuelQuoteForm(request.POST, user=request.user)
        if form.is_valid():
            if 'Get_Quote' in request.POST:
                form.clean_suggPrice()
                form.clean_total()
                return render(request, 'fuelquoteform.html', context={"form": form})

            elif 'Submit_Quote' in request.POST:
                post = form.save(commit=False)
                post.suggestedPrice = form.clean_suggPrice()
                post.totalAmount = form.clean_total()
                post.username = request.user.username
                post.save()
                return redirect('/fuelquotehistory/')
    else:
        form = FuelQuoteForm(user=request.user)

    return render(request, 'fuelquoteform.html', {'form': form})



# fuel quote history
@login_required(login_url = 'login')
def fuelquotehistory(request):
    current_user = request.user
    all_entries = fuelQuote.objects.filter(username=current_user.username).values()
    context= {'all_entries': all_entries}

    return render(request, 'fuelquotehistory.html', context)
