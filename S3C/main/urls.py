from django.urls import path
from . import views

urlpatterns = [
    path('equipe/creer/', views.creer_equipe, name='creer_equipe'),
    path('equipes/', views.liste_equipes, name='liste_equipes'),
    path('equipeg/<int:equipe_id>/', views.detail_equipe, name='detail_equipe'),
    path('', views.acceuil_principale, name='acceuil_principale'),
]
