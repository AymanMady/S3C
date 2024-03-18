from django.urls import path
from . import views

urlpatterns = [
   path('etudiants/',views.etudiants,name='etudiants'),
   path('jerys/',views.jerys,name='jerys'),
   path('add_etudiant/',views.add_etudiant,name='add_etudiant'),
   path('add_jerys/',views.add_jerys,name='add_jerys'),
   path('affectation/',views.affectation,name='affectation'),
   path('liste_affectations/',views.liste_affectations,name='liste_affectations'),
   path('modifier_affectation/<int:id>',views.modifier_affectation,name='modifier_affectation'),
   path('supprimer_affectation/<int:id>',views.supprimer_affectation,name='supprimer_affectation'),
   # path('noter_equipes_pour_defis/',views.noter_equipes_pour_defis,name='noter_equipes_pour_defis'),
]
