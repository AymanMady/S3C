from django import forms
from .models import Utilisateur


class InscriptionJuryForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['email', 'motDePasse', 'role']
        widgets = {
            'role': forms.HiddenInput(attrs={'value': 'jury'}),  # Définit automatiquement le rôle à 'jury'
            'motDePasse': forms.PasswordInput(),  # Champ de mot de passe affiché comme type "password"
        }
class EtudiantForm(forms.ModelForm):
    role = forms.CharField(widget=forms.HiddenInput(), initial='étudiant')
    
    class Meta:
        model = Utilisateur
        fields = ['email', 'motDePasse', 'role']
        labels = {
            'email': 'Adresse email',
            'motDePasse': 'Mot de passe',
            'role': 'role',
        }
def inscription_etudiant(request):
    if request.method == 'POST':
        form = EtudiantForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            mot_de_passe = form.cleaned_data['motDePasse']
            role = form.cleaned_data['role']
            
            # Hasher le mot de passe
            mot_de_passe_hashe = make_password(mot_de_passe)
            
            try:
                # Enregistrer l'utilisateur
                utilisateur = Utilisateur.objects.create(email=email, motDePasse=mot_de_passe_hashe, role=role)
                # Redirection vers une page de succès ou une autre vue
                return redirect('login.html')
            except Exception as e:
                # Gestion des erreurs lors de l'enregistrement de l'utilisateur
                # Affichez un message d'erreur ou effectuez d'autres actions nécessaires
                print(f"Erreur lors de l'enregistrement de l'utilisateur : {e}")
    else:
        form = EtudiantForm()
        
    return render(request, 'inscription_etudiant.html', {'form': form})
