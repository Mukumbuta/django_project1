from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('first_django_app', include('first_django_app.urls')),
    path('admin/', admin.site.urls)
]
