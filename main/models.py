from django.db import models

# Create your models here.

class Poem(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

class Question(models.Model):
    poem = models.ForeignKey(Poem, on_delete=models.CASCADE)
    difficulty = models.CharField(max_length=10) #Easy, Normal, Hard
    question_text = models.TextField()
    correct_answer = models.CharField(max_length=100)
