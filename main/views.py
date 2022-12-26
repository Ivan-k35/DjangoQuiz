from django.shortcuts import render, redirect
from .models import Category, Quiz
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница'})


class CategoryListView(ListView):
    model = Category
    template_name = 'main/category.html'
    context_object_name = 'categories'
    allow_empty = False


class QuizListView(ListView):
    model = Quiz
    template_name = 'main/quiz_list.html'
    context_object_name = 'quizes'
    allow_empty = False

    def get_queryset(self):
        return Quiz.objects.filter(category_id=self.kwargs['pk'])


def quiz_view(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    context = {'obj': quiz}
    return render(request, 'main/quiz.html', context)


def quiz_date_view(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q): answers})
    return JsonResponse({'data': questions})


def save_quiz_view(request, pk):
    print(request.POST)
    return JsonResponse({'text': 'works'})
