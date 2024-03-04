from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('home/', views.home, name='home' ),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('quiz/', views.quiz, name='quiz'),
    path('poem/<int:poem_id>/', views.difficulty, name='difficulty'),
    path('submit_answers/', views.submit_answers, name='submit_answers'),
    path('login/', LoginView.as_view(redirect_authenticated_user=True), name='login'), 
    path('logout/', views.log_out, name = 'log_out'), 
    path('difficulty-selection/', views.difficulty_selection, name='difficulty_selection'),
    path('easy_quiz/', views.easy_quiz, name='easy_quiz'),
    path('normal_quiz/', views.normal_quiz, name='normal_quiz'),
    path('hard_quiz/', views.hard_quiz, name='hard_quiz'),
]