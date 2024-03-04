from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('sign-up/', views.sign_up, name='sign_up'),
    path('login/', views.login, name='login'), 
    path('logout/', views.log_out, name='log_out'), 
    path('difficulty_selection/', views.difficulty_selection, name='difficulty_selection'),
]