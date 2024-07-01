from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.searchPage, name='search_page'),
    path('', views.landing, name='landing'),
    path('home', views.landing, name='landing'),
    path('register', views.registerUser, name='registerUser'),
    path('all_teachers', views.ReadAllTeachers, name='allTeachers'),
    path('eval_teacher/<teacher_id>', views.EvaluateTeacher, name='EvaluateTeacher'),
    path('eval_tag/<EvalID>', views.EvaluateTags, name='EvalTag'),
    path('login', views.UserLogin, name='UserLogin'),
    path('logout', views.UserLogout, name='UserLogout')
]