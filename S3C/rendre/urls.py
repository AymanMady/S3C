from django.urls import path
from . import views

urlpatterns = [
   path('home/',views.home,name='home'),
   # path('render_travail/',views.render_travail,name='render_travail'),
   # path('cree_groupe/',views.cree_groupe,name='cree_groupe'),

]