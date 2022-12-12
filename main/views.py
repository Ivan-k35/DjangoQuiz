from django.shortcuts import render, redirect
from .models import Category, Quiz
from django.views.generic import ListView


class QuizListView(ListView):
    model = Quiz
    template_name = 'main/index.html'


def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    context = {'obj': quiz}
    return render(request, 'main/quiz.html', context)

# def index(reqeust):
#     categories = Category.objects.all()
#     contect = {
#         'categories': categories
#     }
#
#     if reqeust.GET.get('category'):
#         return redirect(f"/quiz/?category={reqeust.GET.get('category')}")
#
#     return render(reqeust, 'main/index.html', contect)
#
#
# def quiz(reqeust):
#     return render(reqeust, 'main/quiz.html')
