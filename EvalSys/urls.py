from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('home', views.landing, name='landing'),
    path('register', views.registerUser, name='registerUser'),
    path('all-teachers', views.ReadAllTeachers, name='allTeachers')
]