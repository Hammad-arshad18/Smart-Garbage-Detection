from django.urls import path
from . import views

urlpatterns = [
    path('', views.getUsers),
    path('contacts/',views.getContacts)
]