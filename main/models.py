from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# Create your models here.

class Difficulty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name_plural = 'Difficulties'

class Poem(models.Model):
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE, related_name='poems')
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return str(self.title)
    
    def get_questions(self):
        return self.question_set.all()

class Question(models.Model):
    poem = models.ForeignKey(Poem, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=200)

    def __str__(self):
        return str(self.text)
    
    def get_answers(self):
        return self.answer_set.all()
    
    def clean(self):
        # Check if the poem already has 10 questions
        if self.pk is None and self.poem.questions.count() >= 10:
            raise ValidationError("A poem cannot have more than 10 questions.")

    def save(self, *args, **kwargs):
        self.clean()  # Validate before saving
        super().save(*args, **kwargs)
    

class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"
    
class Result(models.Model):
    poem = models.ForeignKey(Poem, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return str(self.pk)
