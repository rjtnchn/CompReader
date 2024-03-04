from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from django.db.models import Count
from .models import Poem, Question, Difficulty

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/difficulty_selection')
    return render(request, 'main/home.html')

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/difficulty_selection')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})


def log_out(request):
     print(f"Signing out the {request.user}")
     if request.user.is_authenticated:
          logout(request)
     return redirect('/home')


def difficulty_selection(request):
    difficulties = Difficulty.objects.all()
    return render(request, 'quiz/difficulty_selection.html', {'difficulties': difficulties})


# # def start_quiz(request, difficulty_id):
# #     # Assuming user selects a difficulty
# #     difficulty = Difficulty.objects.get(pk=difficulty_id)
# #     poems = Poem.objects.filter(difficulty=difficulty)
# #     return render(request, 'quiz/quiz.html', {'poems': poems})


# # def score(request):
# #     # Logic to calculate and display score
# #     return render(request, 'quiz/score.html')
