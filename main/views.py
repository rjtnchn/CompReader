from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.views.decorators.http import require_POST
from django.contrib.auth import login, logout, authenticate
from django.db.models import Count
from .models import Poem, Question

# Create your views here.


def home(request):
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


@require_POST
def log_out(request):
     print(f"Signing out the {request.user}")
     if request.user.is_authenticated:
          logout(request)

     return redirect('/home')

def difficulty_selection(request):
    return render(request, 'quiz/difficulty_selection.html')
