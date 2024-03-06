from django.db import models

# Create your models here.

class Difficulty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Poem(models.Model):
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE, related_name='poems')
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self) -> str:
        return self.title

class Question(models.Model):
    poem = models.ForeignKey(Poem, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    correct_answer = models.CharField(max_length=255)  # Now stores the correct answer directly
    options = models.JSONField(default=list)

    def __str__(self) -> str:
        return self.text