from django.urls import path
from . import views

urlpatterns = [

    # path('', views.acceuil_principale, name='acceuil_principale'),
    path('creer_equipe/', views.creer_equipe, name='creer_equipe'),

     path('equipes/', views.liste_equipes, name='liste_equipes'),
     path('equipeg/<int:equipe_id>/', views.detail_equipe, name='detail_equipe'),
    path('jery_view/', views.jery_view, name='jery_view'),
    path('etudient_view/', views.etudient_view, name='etudient_view'),
    path('admin_view/', views.admin_view, name='admin_view'),
    path('login/', views.login, name='login'),
    path('', views.login, name='login'),


]
