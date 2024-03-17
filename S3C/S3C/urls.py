
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("main.urls")),
    path('', include('tach3.urls')),  # Include app-specific URLs
    path("", include("rendre.urls")),
    path('', include('tach1.urls')),
    path('', include('administration.urls')),

]

