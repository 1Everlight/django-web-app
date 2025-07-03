from django.contrib import admin

from listings.models import Band

from listings.models import Listing


# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title','sold','year','band')

class BandAdmin(admin.ModelAdmin):
    list_display = ('name','genre','year_formed')
    
admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)