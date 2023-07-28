from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("<int:produit_id>",views.produit,name="produit"),
    path("<int:produit_id>/book",views.book,name="book")
    
]