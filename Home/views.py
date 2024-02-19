from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact
from .models import About


# Create your views here.

# Home Page
def home(request):
    # HTML can be added here as shown, but not recommended.
    '''
    return HttpResponse ("<h1>Hey I am a Django server.</h1>") '''

    people = [
        {'name' : 'Akash Saha', 'age' : 30},
        {'name' : 'Riya Sharma', 'age' : 14},
        {'name' : 'Karan Singh', 'age' : 28},
        {'name' : 'Priya Patel', 'age' : 25},
        {'name' : 'Rajesh Kumar', 'age' : 17},
    ]

    vegetables = ['Pumpkin','Tomato','Potato']
    
    text = '''Lorem ipsum, dolor sit amet consectetur adipisicing elit. 
    Amet, repellat alias vel quod quaerat pariatur et culpa illum exercitationem illo veritatis nulla vitae ea nam in voluptas, 
    iusto eos quidem!'''

    # This is the proper way to add HTML
    return render(request, 'main/home.html', context = {'page_name': 'Django | Home','people': people, 'text': text, 'vegetables': vegetables}) # context is used to send data from backend to frontend


# Success Page
def success(request):
    '''
    print('x'*10) # Print output can be seen within cmd, isn't visible on webpage
    return HttpResponse("<h2>Hey this is the Success Page</h2>") # return output is directly visible on webpage'''

    return render(request, 'main/success.html', context = {'page_name': 'Django | Success'}) # context is used to send data from backend to frontend


# About Page
def about(request):

    FName = None
    LName = None
    Email = None
    Address = None
    City = None
    State = None
    Zip = None
    File = None

    if request.method == 'POST':
        data = request.POST
        FName = data.get('FName')
        LName = data.get('LName')
        Email = data.get('Email')
        Address = data.get('Address')
        City = data.get('City')
        State = data.get('State')
        Zip = data.get('Zip')
        File = request.FILES.get('Attachment')

        About.objects.create(
            FName = FName,
            LName = LName,
            Email = Email,
            Address = Address,
            City = City,
            State = State,
            Zip = Zip,
            File = File
            )
        
        return redirect('/about')

    return render(request, 'main/about.html',context = {'page_name': 'Django | About'}) # context is used to send data from backend to frontend


# Contact Page
def contact(request):
    name = None
    email = None
    message = None
    file = None

    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')
        file = request.FILES.get('attachment')

        Contact.objects.create(
            name = name,
            email = email,
            message = message,
            file = file,
        )

        return redirect('/contact')

    return render(request, 'main/contact.html',context = {'page_name': 'Django | Contact'}) # context is used to send data from backend to frontend