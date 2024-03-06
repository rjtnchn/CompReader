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
        total_questions = questions.count()
        score = 0

        for i in range(1, total_questions + 1):
            question = Question.objects.get(poem_id=poem_id, id=i)
            user_answer = request.POST.get(f'question_form_answer{i}', '')

            print(f"User answer: {user_answer}")
            print(f"Correct answer: {question.correct_answer}")
            if user_answer== question.correct_answer:
                score += 1
                print("sekai: " + score)
            else:
                print("wrong asnwer")
        request.session['score'] = score

        # Create a context dictionary **including the score**
        context = {'questions': questions, 'score': score, 'poem_id': poem_id}

        return render(request, 'quiz/questions.html', context)

    else:
        context = {'questions': questions}  # Only questions for GET request
        return render(request, 'quiz/questions.html', context)


def score(request):
    # Calculate total score
    total_score = sum(request.session.get('scores', {}).values())

    # Clear session
    request.session.flush()

    return render(request, 'questions/score.html', {'total_score': total_score})

