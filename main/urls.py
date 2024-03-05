from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('home/', views.home, name='home'), 
    path('sign-up/', views.sign_up, name='sign_up'),
    path('login/', views.login, name='login'), 
    path('logout/', views.log_out, name='log_out'), 
    path('difficulty_selection/', views.difficulty_selection, name='difficulty_selection'),
    path('poem/<int:difficulty_id>/',views.poem, name='poem'),
    path('questions/<int:poem_id>/',views.question, name='question'),
    path('score/', views.score, name='score')
]