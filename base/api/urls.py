from django.urls import path
from . import views

urlpatterns = [
    path('', views.getUsers, name='API'),
    path('contacts/',views.getContacts),
    path('blogs/',views.getBlogs),
]
