from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band
from listings.models import Listing


# Create your views here.


# Creating view hello to affiche first testing of our code
def hello(request):
    bands = Band.objects.all()
    return render(request,'listings/hello.html',context = {'bands':bands})


# Creating about us view which show page containing information concerning us
def about(request):
    return HttpResponse("<h1>A propos de nous</h1> <p>Nous adorons merch</p> ")


# Creating view listings to list things of our application
def listings(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listings.html', context = {'listings':listings})

# Creating view contact-us to create a formular for those who want to contact us
def contact(request):
    return HttpResponse("<h1>Contactez-nous</h1> <p>Nous adorons merchex !</p> ")
