from django.urls import path
from . import views

urlpatterns = [
   path('creation_user/',views.creation_user,name='creation_user'),
   path('import_etudiantsl/',views.import_etudiantsl,name='import_etudiantsl'),
]