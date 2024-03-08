#urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('home/', views.home, name='home'), 
    path('sign-up/', views.sign_up, name='sign_up'),
    path('login/', views.login, name='login'), 
    path('logout/', views.log_out, name='log_out'), 
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('poem/<str:difficulty>/', views.poem, name='poem'),
    path('quiz/<int:poem_id>/', views.quiz, name='quiz'),
]