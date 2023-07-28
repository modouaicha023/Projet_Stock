from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Produit,Client 
# Create your views here.

def index(request):
    return render(request,"sama_stock/index.html",{
        "produits": Produit.objects.all()
    })

def produit(request,produit_id):
    produit=Produit.objects.get(id=produit_id)
    return render(request,"sama_stock/produit.html",{
        "produit":produit,
        "clients": produit.clients.all(),
        "no_clients": Client.objects.exclude(produits=produit).all()
    })

def book(request,produit_id):
    if request.method == "POST":
        produit=Produit.objects.get(pk=produit_id)
        client=Client.objects.get(pk=int(request.POST["client"]))
        client.produits.add(produit)
        return HttpResponseRedirect(reverse("produit",args=(produit_id,)))
        