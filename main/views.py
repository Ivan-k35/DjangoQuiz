from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.urls import reverse_lazy
from .models import Category, Quiz


def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница'})


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('main:login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context


def login(request):
    return render(request, 'main/login.html', {'title': 'Войти'})


class CategoryListView(ListView):
    model = Category
    template_name = 'main/category.html'
    context_object_name = 'categories'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категории тестов'
        context['cat_selected'] = 0
        return context


class QuizListView(ListView):
    model = Quiz
    template_name = 'main/category.html'
    context_object_name = 'quizes'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список тестов по выбраноой категории'
        context['cat_selected'] = self.kwargs['pk']
        return context

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
