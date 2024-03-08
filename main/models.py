# models.py

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import Sum


class Difficulty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Poem(models.Model):
    difficulty = models.ForeignKey(
        Difficulty, on_delete=models.CASCADE, related_name='poems')
    title = models.CharField(max_length=50)
    content = models.TextField()




class Answer(models.Model):
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)


class Question(models.Model):
    poem = models.ForeignKey(
        Poem, on_delete=models.CASCADE, related_name='questions'
    )
    text = models.CharField(max_length=200)
    answers = models.ManyToManyField(Answer, related_name='questions')


class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()  # Ensure non-negative score
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Enforce unique user-difficulty combination for accurate tracking
        unique_together = (('user', 'difficulty'),)

    def __str__(self):
        return f"{self.user.username} - {self.difficulty.name}: {self.score}"
    
    def get_user_total_score(user):

        total_score = Score.objects.filter(user=user).aggregate(Sum('score'))['score__sum']
        return total_score or 0  # Handle cases where no scores exist