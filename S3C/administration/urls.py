from django.urls import path
from . import views

urlpatterns = [
   path('etudiants/',views.etudiants,name='etudiants'),
   path('jerys/',views.jerys,name='jerys'),
]
