from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from dashboard.blog.models import Categories


@login_required(login_url='/accounts/login/')
def index(request):
    categories = Categories.objects.all()
    data = {
        'categories' : categories
    }
    return render(request, 'dashboard/general/index.html', data)
