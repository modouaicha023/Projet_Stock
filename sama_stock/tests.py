from django.db.models import Max
from django.test import TestCase,Client as HtppClient

from .models import Client,Produit,Boutique
# Create your tests here.

class ProduitTestCase(TestCase):
    def setUp(self):
        #SetUp est une fonction qui permet de créer une base de donnéé de test
        #Create Boutique
        b1 = Boutique.objects.create(nom="Boutique 1",lieu="Pikine")
        b2 = Boutique.objects.create(nom="Boutique 2",lieu="Keur Massar")
        b3 = Boutique.objects.create(nom="Boutique 3",lieu="Dakar")
        


        # Create Produits
        p1 = Produit.objects.create(nom="Mentos",desciption="Soit fraiche dans la bouche",prix=2000,boutique=b1)
        p2 = Produit.objects.create(nom="Boisson",desciption="Boisoon bou nekh",prix=600,boutique=b2)
        p3 = Produit.objects.create(nom="Tampiko",desciption="Jus pour xalei yi",prix=200,boutique=b2)
        p4 = Produit.objects.create(nom="Eau",desciption="Ndokh pour nane",prix=50,boutique=b1)
        p5 = Produit.objects.create(nom="Soblé",desciption="Soblé Mbaye bi",prix=1200,boutique=b3)

    def test_categories_count(self):
        a=Boutique.objects.get(nom="Boutique 1")
        self.assertEqual(a.categories.count(),2)
        
    def test_valid_produit(self):
        b = Boutique.objects.create(nom="Boutique 2",lieu="Keur Massar")
        p = Produit.objects.create(nom="King",desciption="Gang",prix=2000,boutique=b)
        self.assertTrue(p.is_valid_produit())

    def test_invalid_produit_prix(self):
        b = Boutique.objects.create(nom="Boutique 2",lieu="Keur Massar")
        p = Produit.objects.create(nom="King",desciption="Gang",prix=0,boutique=b)
        self.assertTrue(p.is_valid_produit())
    
    def test_invalid_produit_nom(self):
        b = Boutique.objects.create(nom="Boutique 2",lieu="Keur Massar")
        p = Produit.objects.create(nom="",desciption="Gang",prix=200,boutique=b)
        self.assertTrue(p.is_valid_produit())
        
    def test_index(self):
        c = HtppClient()
        response=c.get("/sama_stock/")
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.context["produits"].count(),5)

    def test_valid_produit_page(self):
        b = Boutique.objects.create(nom="Boutique 4", lieu="GediaWaye")
        p = Produit.objects.create(nom="MAD", desciption="Gfdkfvang", prix=300, boutique=b)

        c = HtppClient()
        response = c.get(f"/sama_stock/{p.id}")
        self.assertEqual(response.status_code, 200)

    def test_invalid_produit_page(self):
        max_id = Produit.objects.all().aggregate(Max("id"))["id__max"] # le plus grand id dans la base
        c = HtppClient()
        
        if max_id is not None:
            response = c.get(f"/sama_stock/{max_id + 1}")
            self.assertEqual(response.status_code, 404)
        else:
            response = c.get("/sama_stock/9999")  # Utilisez un ID qui n'existe pas
            self.assertEqual(response.status_code, 404)
    
    def test_produit_page_clients(self):
        p = Produit.objects.get(pk=1)
        c = Client.objects.create(fullname="hehe")
        p.clients.add(c)

        c1= HtppClient()
        response = c1.get(f"/sama_stock/{p.id}")
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.context["clients"].count(),1)
