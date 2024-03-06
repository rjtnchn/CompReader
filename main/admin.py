from django.contrib import admin
from .models import Difficulty, Poem, Question, Answer, Result

class AnswerInline(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


admin.site.register(Difficulty)
admin.site.register(Poem)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Result)


# Register your models here.


