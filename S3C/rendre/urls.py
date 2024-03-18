from django.urls import path
from . import views

urlpatterns = [
   path('home_etud/',views.home_etud,name='home_etud'),
   path('render_travail/',views.render_travail,name='render_travail'),
   path('cree_groupe/',views.cree_groupe,name='cree_groupe'),

]