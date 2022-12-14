from django.contrib import admin
from .models import Result


class ResultAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'user')


admin.site.register(Result, ResultAdmin)
