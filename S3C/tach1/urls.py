from django.urls import path
from . import views

urlpatterns = [
   path('creation_user/',views.creation_user,name='creation_user'),
]