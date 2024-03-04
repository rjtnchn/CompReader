from django.db import models

# Create your models here.

class Difficulty(models.Model):
    name = models.CharField(max_length=100)

class Poem(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE)

class Question(models.Model):
    poem = models.ForeignKey(Poem, on_delete=models.CASCADE)
    question_text = models.TextField()
    choices = models.CharField(max_length=255)  # Store choices as a comma-separated string
    correct_answer = models.CharField(max_length=255)

