from django.shortcuts import render, redirect
from .models import Category, Quiz
from django.views.generic import ListView


class CategoryListView(ListView):
    model = Category
    template_name = 'main/index.html'
    context_object_name = 'categories'

    def get(self, *args, **kwargs):
        if self.request.GET.get('category') and self.request.GET.get('category') != 'Choose':
            return redirect(f"/quiz/?category={self.request.GET.get('category')}")
        return super(CategoryListView, self).get(*args, **kwargs)


class QuizListView(ListView):
    model = Quiz
    template_name = 'main/quiz_list.html'
    context_object_name = 'quizes'

    def get_queryset(self):
        return Quiz.objects.filter(category__category_name=self.request.GET.get('category')).first()


def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    context = {'obj': quiz}
    return render(request, 'main/quiz.html', context)


