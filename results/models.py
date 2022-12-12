from django.db import models
from main.models import Quiz
from django.contrib.auth.admin import User


class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'
