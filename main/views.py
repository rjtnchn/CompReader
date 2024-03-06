#views.py
import json
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
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



def poem(request, difficulty_id):
    difficulty = Difficulty.objects.get(pk=difficulty_id)
    poem = Poem.objects.filter(difficulty=difficulty).first()
    return render(request, 'quiz/poem.html', {'poem': poem})


def question(request, poem_id):
    
    poem = Poem.objects.get(pk=poem_id)
    questions = Question.objects.filter(poem=poem)
    request.session['poem_id'] = poem_id
    request.session['poem_read'] = True
    
    if request.method == 'POST':
        # Handle form submission and calculate score
        total_questions = Question.objects.filter(poem_id=poem_id).count()
        score = 0

        for i in range(1, total_questions + 1):
            question = Question.objects.get(poem_id=poem_id, id=i)
            options_json = json.dumps(question.options)  # Convert options list to JSON string
            answer_choices = json.loads(options_json) 

            user_answer = request.POST.get(f'question_form_answer{i}', '')

            # Check if user answer is present in the answer choices (case-insensitive)
            if user_answer.strip().lower() in [choice.strip().lower() for choice in answer_choices]:
                score += 1

        # Store score in session
        request.session['score'] = score
        print("hello")

        
    return render(request, 'quiz/questions.html', {'questions': questions})


def score(request):
    # Calculate total score
    total_score = sum(request.session.get('scores', {}).values())

    # Clear session
    request.session.flush()

    return render(request, 'questions/score.html', {'total_score': total_score})

