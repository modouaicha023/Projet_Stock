from django.contrib import admin
from .models import Boutique, Produit,Client
# Register your models here.
class ProduitAdmin(admin.ModelAdmin):
    list_display=("id","nom","desciption","prix","boutique")
admin.site.register(Boutique)
admin.site.register(Produit,ProduitAdmin)
admin.site.register(Client)