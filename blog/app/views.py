from django.shortcuts import render, redirect
from dashboard.blog.models import Categories

def index(request):

    categories = Categories.objects.all()

    data = {
        'categories' : categories
    }
    return render(request, 'app/index.html', data)
