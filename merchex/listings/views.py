from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band
from listings.models import Listing
from listings import forms
from django.core.mail import send_mail
from django.shortcuts import redirect


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
    return render(request, "listings/listings.html",{"listings": listings})

def listings_detail(request, id):
    listing = Listing.objects.get(id = id)
    return render(request, "listings/listings_detail.html",{"listing": listing})


# Creating view contact-us to create a formular for those who want to let message for us
def contact(request):
    
    if request.method == 'POST':
        # dans le cas où la methode utiliser est post on remplie le formulaire avec les données POST
        form = forms.ContactUsForm(request.POST)
        
        if form.is_valid():
            send_mail(
                subject=f"message from {form.cleaned_data['name'] or 'anonymous'} via merchex contact us form",
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz']
            )
            return redirect('email-sent')
            # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
            # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).
    else:
        # au cas contraire c'est donc get alors on laisse les champs vide
        form = forms.ContactUsForm()
        
     
        
    return render(request, 'listings/contact.html', {'form':form})


def Email_envoyer(request):
    return render(request, 'listings/Email.html')


def band_create(request):
    if request.method == 'POST':
        form = forms.BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)

    else:
        form = forms.BandForm()

    return render(request,
            'listings/band_create.html',
            {'form': form})