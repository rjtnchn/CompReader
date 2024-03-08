from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'password1', 'password2'] 
        
        
        
from .models import Answer, Question

from django.db import models  # Needed for accessing models within forms

class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(QuizForm, self).__init__(*args, **kwargs)
        questions = kwargs.get('questions', None)
        self.user = kwargs.get('user', None)  # Retrieve user from kwargs (optional)
        if questions:
            for question in questions:
                field_name = f'question_{question.id}'
                self.fields[field_name] = forms.ModelChoiceField(
                    queryset=question.answers.all(),
                    label=question.text
                )

    def clean(self):
        cleaned_data = super(QuizForm, self).clean()
        # Access user selections for each question
        user_answers = {question_id: cleaned_data[f'question_{question_id}'] for question_id in cleaned_data.keys() if question_id.startswith('question_')}

        # Logic to calculate score based on user selections and correct answers
        score = 0
        for question_id, answer_id in user_answers.items():
            answer = Answer.objects.get(pk=answer_id)
            if answer.is_correct:
                score += 1  # Increment score for correct answers

        cleaned_data['score'] = score

        # Optionally prepare data for Score model (if user is available)
        if self.user:
            cleaned_data['user'] = self.user  # Add user to cleaned data for easier access in view
            cleaned_data['difficulty'] = ...  # Replace ... with logic to get difficulty (e.g., from poem)

        return cleaned_data
