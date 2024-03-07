from django.contrib import admin
from .models import Difficulty, Poem, Question, Answer

class AnswerInline(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


admin.site.register(Difficulty)
admin.site.register(Poem)
admin.site.register(Question)
admin.site.register(Answer)



# Register your models here.


