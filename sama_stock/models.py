from django.db import models

# Create your models here.

class Boutique(models.Model):
    nom=models.CharField(max_length=64)
    lieu=models.CharField(max_length=64)
    
    def __str__(self):
        return f"\n Nom: {self.nom} \n Lieu: {self.lieu} \n"


class Produit(models.Model):
    nom=models.CharField(max_length=64)
    desciption=models.CharField(max_length=64)
    prix=models.IntegerField()
    boutique=models.ForeignKey(Boutique,on_delete=models.CASCADE, related_name="categories")


    def __str__(self):
        return f"\n Nom: {self.nom} \n Description: {self.desciption} \n Prix: {self.prix}"
    
    def is_valid_produit(self):
        return self.nom != "" and self.prix > 0


class Client(models.Model):
    fullname = models.CharField(max_length=64)
    produits = models.ManyToManyField(Produit,blank=True,related_name="clients")

    def __str__(self):
        return f"\n Nom: {self.fullname} \n"