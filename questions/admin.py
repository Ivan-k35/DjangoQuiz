from django.contrib import admin
from .models import Question, Answer


class AnswerInLine(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine]
    list_display = ('quiz', 'text')


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'text', 'is_correct')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
