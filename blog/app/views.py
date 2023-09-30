from django.shortcuts import render, redirect
from dashboard.blog.models import Group

def index(request):

    groups = Group.objects.all()

    data = {
        'groups' : groups
    }
    return render(request, 'app/index.html', data)
