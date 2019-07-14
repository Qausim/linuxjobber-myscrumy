from django.contrib import admin
from django.contrib.admin import register

from .models import GoalStatus, ScrumyGoals, ScrumyHistory

# Register your models here.


admin.site.register(GoalStatus)
admin.site.register(ScrumyGoals)
admin.site.register(ScrumyHistory)
