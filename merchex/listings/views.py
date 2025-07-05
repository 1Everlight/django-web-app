from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band
from listings.models import Listing


# Create your views here.


# Creating view for group detail showing
def band_detail(request, id):  # notez le paramètre id supplémentaire
    band = Band.objects.get(id=id)
    return render(request, "listings/band_detail.html", {"band": band})


# Creating view hello to affiche first testing of our code
def band_list(request):
    bands = Band.objects.all()
    return render(request, "listings/band_list.html", context={"bands": bands})


# Creating about us view which show page containing information concerning us
def about(request):
    return HttpResponse("<h1>A propos de nous</h1> <p>Nous adorons merch</p> ")


# Creating view listings to list things of our application
def listings(request):
    listings = Listing.objects.all()
    return render(request, "listings/listings.html", context={"listings": listings})

def listings_detail(request, id):
    listings = Listing.objects.get(id = id)
    return render(request, "listings/listings_detail.html", context={"listings": listings})


# Creating view contact-us to create a formular for those who want to contact us
def contact(request):
    return HttpResponse("<h1>Contactez-nous</h1> <p>Nous adorons merchex !</p> ")
