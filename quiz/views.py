from django.shortcuts import render, redirect
from django.db.models import Count
from .models import Poem, Question

# Create your views here.

def quiz(request):
    poems = Poem.objects.all()
    return render(request, 'quiz.html' , {'poems': poems})

def difficulty(request, poem_id):
    poem = Poem.objects.get(id=poem_id)
    questions = Question.objects.filter(poem=poem)
    return render(request, 'difficulty.html', {'poem' : poem, 'questions' : questions})

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