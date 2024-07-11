from django.urls import path
from . import views

urlpatterns = [
    path('', views.SearchProf, name='landing'),
    path('Privacy Policy', views.PPolicy, name='PPolicy'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('home', views.SearchProf, name='home'),
    path('register', views.registerUser, name='registerUser'),
    path('eval_teacher/<teacher_id>', views.EvaluateTeacher, name='EvaluateTeacher'),
    path('eval_tag/<EvalID>', views.EvaluateTags, name='EvalTag'),
    path('login', views.UserLogin, name='UserLogin'),
    path('logout', views.UserLogout, name='UserLogout'),
    path('search_prof', views.SearchProf, name='SearchProf'),
    path('teacher/<teacher_id>', views.TeacherInfo, name='TeacherInfo'),
    path('edit_eval/<evalID>', views.EditTeacherEval, name='EditEval'),
    path('delete_eval/<evalID>', views.DeleteEval, name='DeleteEval'),
    path('bookmark', views.showBookmark, name='Bookmark'),
    path('bookmark_add/<ProfID>', views.ProfPage_AddBookmark, name='AddBM'),
    path('bookmark_del/<ProfID>', views.ProfPage_DelBookmark, name='DelBM'),
]