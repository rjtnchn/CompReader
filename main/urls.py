from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('home/', views.home, name='home' ),
    path('sign-up/', views.sign_up, name='sign_up' ),
    path('quiz/', views.quiz, name='quiz'),
    path('poem/<int:poem_id/', views.difficulty, name='difficulty'),
    path('submit_answers/', views.submit_answers, name='submit_answers'),
    path('logout/', views.user_logout, name='user_logout'),
    path('register/', views.register, name='register'),
]