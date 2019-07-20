from random import randrange

from django.http import HttpResponse
from django.shortcuts import render

from .models import ScrumyGoals, GoalStatus, User

# Create your views here.


def index(request):
    goal = ScrumyGoals.objects.filter(goal_name='Learn Django')
    return HttpResponse(goal)

def move_goal(request, goal_id):
    goal = ScrumyGoals.objects.filter(goal_id=goal_id)
    return HttpResponse(goal)

def add_goal(request):
    '''
      Adds a new ScrumyGoals object to the database
    '''
    # Get the existing goals
    existing_goals = ScrumyGoals.objects.all()
    # Get the list of existing ids from the existing goals
    existing_goal_ids = [goal.goal_id for goal in existing_goals]
    # Generate a random id between 1000 and 9999
    random_goal_id = randrange(1000, 9999)
    # Generate a new id if the previous id is already taken
    while random_goal_id in existing_goal_ids:
        random_goal_id = randrange(1000, 9999)
    
    # Get the weekly goal status
    weekly_goal_status = GoalStatus.objects.get(status_name='Weekly Goal')
    user = User.objects.get(username='Louis')
    new_goal = ScrumyGoals(goal_name='Keep Learning Django', goal_id=random_goal_id,
      created_by='Louis', owner='Louis', goal_status=weekly_goal_status, user=user)
    new_goal.save()

    return HttpResponse(':) New goal created successfully')

def home(request):
    '''
      Fetches records of ScrumyGoals with goal_name 'Keep Learning Django'
    '''
    # Get goals with name = 'Keep Learning Django'
    goals = ScrumyGoals.objects.filter(goal_name='Keep Learning Django')
    # response is the comma-separated names if goals are more than one
    if len(goals) > 1:
        response = ', '.join([goal.goal_name for goal in goals])
    # If there's only one record response is just the name of that one goal
    elif goals:
        response = goals[0].goal_name
    # If nothing at all, set a message notifying of empty record
    else:
        response = ":( Sorry, but there's goal here yet."

    return HttpResponse(response)