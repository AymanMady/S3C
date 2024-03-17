from django.urls import path
from . import views

urlpatterns = [
   # _________________________________ETUDIANTS_____________________________________________________________________

   path('creation_etudiant/',views.creation_etudiant,name='creation_etudiant'),
   path('verification_etudiant/',views.verification_etudiant,name='verification_etudiant'),
   path('liste_etudiants/',views.liste_etudiants,name='liste_etudiants'),
   path('supprimer_etudiant/<int:id_etudiant>',views.supprimer_etudiant,name="supprimer_etudiant"),
   path('modifier_etudiant/<int:id_etudiant>',views.modifier_etudiant,name="modifier_etudiant"),
   
   # _________________________________FIN ETUDIANTS_____________________________________________________________________
  
   # _________________________________JURY______________________________________________________________
   path('creation_jury/',views.creation_jury,name='creation_jury'),
   path('verification_jury/',views.verification_jury,name='verification_jury'),
   path('liste_jury/',views.liste_jury,name='liste_jury'),
   path('supprimer_jury/<int:id_jury>',views.supprimer_jury,name="supprimer_jury"),
   path('modifier_jury/<int:id_jury>',views.modifier_jury,name="modifier_jury"),
   # _________________________________FIN JURY_____________________________________________________________________
   
   
      # _________________________________ADMIN______________________________________________________________
   path('creation_admin/',views.creation_admin,name='creation_admin'),
   path('verification_admin/',views.verification_admin,name='verification_admin'),
   path('liste_admin/',views.liste_admin,name='liste_admin'),
   path('supprimer_admin/<int:id_admin>',views.supprimer_admin,name="supprimer_admin"),
   path('modifier_admin/<int:id_admin>',views.modifier_admin,name="modifier_admin"),
   # _________________________________FIN ADMIN_____________________________________________________________________

]