from django import forms
from main.models import Équipe

class ÉquipeForm(forms.ModelForm):
    class Meta:
        model = Équipe
        fields = ['nomEquipe', 'leadID', 'adjointID']
