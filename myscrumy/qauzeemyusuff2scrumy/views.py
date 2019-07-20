from django.http import HttpResponse
from django.shortcuts import render

from .models import ScrumyGoals

# Create your views here.


def index(request):
    goal = ScrumyGoals.objects.filter(goal_name='Learn Django')
    return HttpResponse(goal)

def move_goal(request, goal_id):
    goal = ScrumyGoals.objects.filter(goal_id=goal_id)
    return HttpResponse(goal)
