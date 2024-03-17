from django.urls import path
from . import views

urlpatterns = [
   path('etudiants/',views.etudiants,name='etudiants'),
   path('jerys/',views.jerys,name='jerys'),
   path('add_etudiant/',views.add_etudiant,name='add_etudiant'),
   path('add_jerys/',views.add_jerys,name='add_jerys'),
]
