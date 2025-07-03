from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band
from listings.models import Listing


# Create your views here.


# Creating view hello to affiche first testing of our code
def hello(request):
    bands = Band.objects.all()
    return render(request,'listings/hello.html', {'bands':bands})


# Creating about us view which show page containing information concerning us
def about(request):
    return HttpResponse("<h1>A propos de nous</h1> <p>Nous adorons merch</p> ")


# Creating view listings to list things of our application
def listings(request):
    listings = Listing.objects.all()
    return HttpResponse(
                        f"""<html>
                            <head>
                                <title>merchex</title>
                            </head>
                            <body>
                                <h1>Voici la liste !</h1>
                                <p>
                                concentrez vous,je suis sur le point de vous presenter l'inoubliable !
                                </p>
                                <ul>
                                <li>{listings[0].title}</li>
                                <li>{listings[1].title}</li>
                                <li>{listings[2].title}</li>
                                </ul>
                            </body>
                            </html>
                            """
    )


# Creating view contact-us to create a formular for those who want to contact us
def contact(request):
    return HttpResponse("<h1>Contactez-nous</h1> <p>Nous adorons merchex !</p> ")
