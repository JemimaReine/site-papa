from django import forms
from .models import Commande

class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['nom', 'prenoms', 'telephone', 'email', 'quantite']