"""
URL configuration for merchex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('bands/', views.band_list, name='band-list'),
    path('bands/<int:id>/', views.band_detail, name='band-detail'),
    path("about-us/", views.about),
    path("listings/", views.listings, name='listings-list'),
    path("listings/<int:id>/", views.listings_detail, name="listings-detail"),
    path("contact-us/", views.contact),
    path("email-sent/", views.Email_envoyer, name='email-sent'),
    path("bands/add/", views.band_create, name='band-create'),
    path("bands/<int:id>/update", views.band_update, name='band-update'),
    path("bands/<int:id>/delete", views.banf_delete, name='band-delete')
]
