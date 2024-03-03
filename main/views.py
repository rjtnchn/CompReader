from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
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
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})

@login_required
def quiz(request):
    poems = Poem.objects.all()
    return render(request, 'quiz/quiz.html' , {'poems': poems})

@login_required
def difficulty(request, poem_id):
    poem = Poem.objects.get(id=poem_id)
    questions = Question.objects.filter(poem=poem)
    return render(request, 'difficulty.html', {'poem' : poem, 'questions' : questions})

@login_required
def submit_answers(request):
    if request.method == 'POST':

            total_questions = 0
            correct_answers = 0
            for question_id, answer in request.POST.items():
                 if question_id.isdigit():
                      question = Question.objects.get(id=int(question_id))
                      total_question += 1
                      if answer == question.correct_answer:
                           correct_answers +=1 
            
            score = (correct_answers / total_questions) * 100 if total_questions > 0 else 0
           # Get the next poem for the redirect
            next_poem = None
            current_poem_id = int(request.POST.get('poem_id', 0))
            current_poem = Poem.objects.get(id=current_poem_id)
            next_poems = Poem.objects.filter(id__gt=current_poem_id).order_by('id')
            if next_poems.exists():
                next_poem = next_poems.first()

            return render(request, 'score.html', {'score': score, 'next_poem': next_poem})
    else:
            return redirect('quiz')
    

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('quiz')
        else:
            # Invalid login
            return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
    else:
        return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect('quiz')
    else:
        return render(request, 'register.html')