from django.shortcuts import get_object_or_404, render, redirect
from .forms import RegisterForm, QuizForm
from django.contrib.auth import login, logout
from .models import *



# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
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



def dashboard(request):
    selected_difficulty = request.GET.get('difficulty')

    if selected_difficulty:
        redirect('poem', difficulty=selected_difficulty) # Redirect immediately if difficulty is chosen

    difficulties = Difficulty.objects.all()
    context = {'difficulties': difficulties}
    return render(request, 'quiz/dashboard.html', context)

def poem(request, difficulty=None):
  # Use the difficulty parameter passed in the URL
  if difficulty:
    # Get all poems with the selected difficulty
    poems = Poem.objects.filter(difficulty__name=difficulty)

    # If there are poems for the chosen difficulty
    if poems:
      # Pick a random poem from the filtered set
      random_poem = poems.order_by('?').first()
      context = {'poem': random_poem}
      return render(request, 'quiz/poem.html', context)
    else:
      # Handle situation where no poems exist for the difficulty
      message = "No poems found for that difficulty yet!"
      context = {'message': message}
      return render(request, 'quiz/poem.html', context)
  else:
    # User might have accessed directly or difficulty not found, redirect to dashboard
    return redirect('dashboard')

    
    
from django.db import transaction  # For atomic database operations

def quiz(request, poem_id):
    poem = get_object_or_404(Poem, pk=poem_id)
    questions = poem.questions.all()

    if request.method == 'POST':
        # Handle form submission
        form = QuizForm(request.POST, questions=questions, user=request.user)  # Pass user (optional)
        if form.is_valid():
            score = form.cleaned_data['score']
            difficulty = poem.difficulty  # Assuming difficulty is associated with the poem

            with transaction.atomic():  # Wrap score creation in a transaction
                new_score = Score.objects.create(user=form.cleaned_data['user'],
                                                 difficulty=difficulty,
                                                 score=score)

            # Additional logic for handling score, e.g., displaying score message

            context = {'poem': poem, 'questions': questions, 'score': score}
            return render(request, 'quiz/quiz.html', context)
    else:
        # Initial form for the first render
        form = QuizForm()

    context = {'poem': poem, 'questions': questions, 'form': form}
    return render(request, 'quiz/quiz.html', context)
