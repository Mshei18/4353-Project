from django.shortcuts import render
from django.http import HttpResponse

from myapp.models import Category
from django.template import RequestContext

from .models import ClientProfile


# Create your views here.
def index2(request):
    # Obtain the context from the HTTP request.
    # context = RequestContext(request)

    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    category_list = Category.objects.order_by('id')[:5]
    context_dict = {'categories': category_list}
    context = {'categories': category_list}

    client = ClientProfile.objects.create(fullName='test', city='test')
    # if statement to run if button pressed?

    return render(request, 'index.html', context)


def index(request):
    if request.method == "POST":
        ClientProfile.objects.update_or_create(fullName=request.POST['name'], address1=request.POST['address1'], address2=request.POST['address2'], city=request.POST['city'])

    return render(request, 'index.html')

def index2(request):
    # return HttpResponse('Hello World')
    if request.method == "POST":
        ClientProfile.objects.update_or_create(fullName=request.POST['name'], address1=request.POST['address1'], address2=request.POST['address2'], city=request.POST['city'])

    # c = {'first_name': 'John', 'last_name': 'Doe'}
    return render(request, 'client.html') #, context=c)

# def new_page(request):
  #  data = request.GET[‘fulltextarea’]
   # return render(request, 'newpage.html', {'data':data})

#def index2(request):
    # return HttpResponse('Hello World')
#    c = {'first_name': 'Jay', 'last_name': 'Rock'}
#    return render(request, 'client.html', context=c)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)