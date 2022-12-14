from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='home'),
    path('category/', views.CategoryListView.as_view(), name='category'),
    path('quiz/', views.QuizListView.as_view(), name='quiz-list'),
    path('quiz/<pk>/', views.quiz_view, name='quiz'),
    path('quiz/<pk>/data/', views.quiz_date_view, name='quiz-data'),
    path('quiz/<pk>/save/', views.save_quiz_view, name='quiz-save'),
]
