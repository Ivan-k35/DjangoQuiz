from django.shortcuts import render, redirect
from .models import Category, Quiz
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


class CategoryListView(ListView):
    model = Category
    template_name = 'main/index.html'
    context_object_name = 'categories'
    allow_empty = False

    def get(self, *args, **kwargs):
        if self.request.GET.get('category') and self.request.GET.get('category') != 'Choose':
            return redirect(f"/quiz/?category={self.request.GET.get('category')}")
        return super(CategoryListView, self).get(*args, **kwargs)


class QuizListView(ListView):
    model = Quiz
    template_name = 'main/quiz_list.html'
    context_object_name = 'quizes'
    allow_empty = False

    def get_queryset(self):
        return Quiz.objects.filter(category__category_name=self.request.GET.get('category'))


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
    return JsonResponse({
        'data': questions
    })
