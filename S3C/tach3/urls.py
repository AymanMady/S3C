from django.urls import path
from . import views

urlpatterns = [
    path('verification_Email/', views.verification_Email, name='verification_Email'), 
    path('create_defi/', views.create_defi, name='create_defi'),  
    path('get_all_defis/', views.get_all_defis, name='get_all_defis'),  
    path('', views.get_all_defis, name='get_all_defis'),  
    path('delete_defi/<int:id>', views.delete_defi, name='delete_defi'),  
    path('update_defi/<int:defi_id>', views.update_defi, name='update_defi'),  
]