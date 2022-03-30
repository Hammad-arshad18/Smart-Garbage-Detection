from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index,name="Index"),
    path('home/', views.Home, name="Homepage"),
    path('live/', views.livecam, name="LiveCameras"),
    path('services/', views.services, name="Services"),
    path('about/', views.about, name="About"),
    path('faq/', views.faq, name="Faq"),
    path('register/',views.Register,name="Register"),
    path('logout/',views.Logout,name="Logout"),
    path('profile/',views.Profile,name="Profile"),
    path('updatePersonal/',views.UpdatePersonal,name="UpdatePersonal"),
    path('dashboard/',views.Dashboard,name="Dashboard"),
]
