#urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('home/', views.home, name='home'), 
    path('sign-up/', views.sign_up, name='sign_up'),
    path('login/', views.login, name='login'), 
    path('logout/', views.log_out, name='log_out'), 
    path('difficulty_select/', views.difficulty_select, name='difficulty_select'),
    path('poem/<int:difficulty_id>/', views.display_poem, name='display_poem'),
    path('questions/<int:poem_id>/', views.display_questions, name='display_questions'),
    path('calculate_score/', views.calculate_score, name='calculate_score'),
    path('score/', views.display_score, name='score'),
]