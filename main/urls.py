from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.CategoryListView.as_view(), name='home'),
    path('quiz/', views.QuizListView.as_view(), name='quiz_list'),
    path('quiz/<pk>/', views.quiz_view, name='quiz'),
]
