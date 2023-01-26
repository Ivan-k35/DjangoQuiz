from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'main'

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('category/', views.CategoryListView.as_view(), name='category'),
    path('category/<int:pk>/', views.QuizListView.as_view(), name='quiz-list'),
    path('quiz/<int:pk>/', views.quiz_view, name='quiz'),
    path('quiz/<int:pk>/data/', views.quiz_date_view, name='quiz-data'),
    path('quiz/<int:pk>/save/', views.save_quiz_view, name='quiz-save'),
]
