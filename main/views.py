from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .models import Poem, Question, Difficulty, Result
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return redirect('/difficulty_select')
    return render(request, 'main/home.html')


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('/difficulty')  # Redirect if already logged in

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/difficulty')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})



def log_out(request):
     print(f"Signing out the {request.user}")
     if request.user.is_authenticated:
          logout(request)
     return redirect('/home')


@login_required
def difficulty_select(request):
    difficulties = Difficulty.objects.all()
    return render(request, 'quiz/difficulty_selection.html', {'difficulties': difficulties})


@login_required
def display_poem(request, difficulty_id):
    if difficulty_id is None:
        # Handle the case where difficulty_id is None
        # Redirect the user to an appropriate page or show an error message
        return HttpResponse("Invalid difficulty")

    difficulty = get_object_or_404(Difficulty, pk=difficulty_id)
    poem = Poem.objects.filter(difficulty=difficulty).first()
    if poem is None:
        # Handle the case where there are no poems for the given difficulty
        # Redirect the user to an appropriate page or show an error message
        return HttpResponse("No poem found for this difficulty")

    questions = poem.questions.all()
    return render(request, 'quiz/poem.html', {'poem': poem, 'questions': questions})



@login_required
def display_questions(request, poem_id):
    poem = get_object_or_404(Poem, pk=poem_id)
    difficulty_id = poem.difficulty.id 
    questions = Question.objects.filter(poem=poem)
    return render(request, 'quiz/questions.html', {'questions': questions, 'poem_id': poem_id, 'difficulty_id': difficulty_id})


@login_required
def calculate_score(request):
    if request.method == 'POST':
        poem_id = request.POST.get('poem_id')
        poem = Poem.objects.get(pk=poem_id)
        questions = Question.objects.filter(poem=poem)
        total_questions = questions.count()
        score = 0

        for question in questions:
            user_answer = request.POST.get(f'question_{question.id}_answer', '')  # Get user's answer for this question

            if user_answer == question.correct_answer:
                score += 1

        # Save the result to the database
        Result.objects.create(poem=poem, user=request.user, score=score)

        return redirect('score')  # Redirect to the score page after calculation


@login_required
def display_score(request):
    # Retrieve the user's results
    user_results = Result.objects.filter(user=request.user)

    return render(request, 'quiz/score.html', {'user_results': user_results})
