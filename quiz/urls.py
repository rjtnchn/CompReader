from django.urls import path
from . import views


urlpatterns = [
    path('', views.quiz, name='quiz'),
    path('poem/<int:poem_id/', views.difficulty, name='difficulty'),
    path('submit_answers/', views.submit_answers, name='submit_answers'),
]
