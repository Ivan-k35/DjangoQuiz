from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.QuizListView, name='home' ),
    path('quiz/', views.quiz_view, name='quiz')
]
