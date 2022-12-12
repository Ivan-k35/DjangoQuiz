from django.contrib import admin
from .models import Category, Quiz


class QuizAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')


admin.site.register(Category)
admin.site.register(Quiz, QuizAdmin)
