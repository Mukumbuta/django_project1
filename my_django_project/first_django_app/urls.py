from django.urls import path

from first_django_app import views

urlpatterns = [
    path('', views.index, name = 'first_django_app'),
]