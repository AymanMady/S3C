from django.urls import path
from . import views

urlpatterns = [
    path('verification_Email/', views.verification_Email, name='verification_Email'), 
    path('create_defi/', views.create_defi, name='create_defi'),  
    path('list_defis/', views.get_all_defis, name='list_defis'),  
    path('delete_defi/<int:id>', views.delete_defi, name='delete_defi'),  
    path('update_defi/<int:defi_id>', views.update_defi, name='update_defi'),
      
    # path('upload/', views.upload_file, name='upload_file'), 
    path('download/<int:file_id>/', views.download_or_view_file, name='download_or_view_file'),
       path('home_jery/',views.home_jery,name='home_jery'),

]