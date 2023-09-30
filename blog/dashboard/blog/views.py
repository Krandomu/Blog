
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Group, Hashtag
from django.contrib import messages

@login_required(login_url='/accounts/login/')
def blog(request):
    groups = Group.objects.all()
    return render(request, 'dashboard/blog/index.html', {'groups': groups})

@login_required(login_url='/accounts/login/')
def add_group(request):
    if request.method == "POST":
        try:
            group_name = request.POST.get('group-name')
            if group_name:  # check if name is not empty
                group = Group(name=group_name)
                group.save()
                messages.success(request, 'Group successfully added.')
            else:
                messages.error(request, 'Group name cannot be empty.')
        except Exception as e:
            messages.error(request, f'Error adding group: {e}')
    return redirect('blog')

@login_required(login_url='/accounts/login/')
def delete_group(request):
    if request.method == "POST":
        try:
            group_id = request.POST.get('group-id')
            if Group.objects.filter(id=group_id).exists():  # check if group exists
                group = Group.objects.get(id=group_id)
                group.delete()
                messages.success(request, 'Group successfully deleted.')
            else:
                messages.error(request, 'Group does not exist.')
        except Exception as e:
            messages.error(request, f'Error deleting group: {e}')
    return redirect('blog')

@login_required(login_url='/accounts/login/')
def add_hashtag(request):
    if request.method == "POST":
        try:
            group_id = request.POST.get('group-id')
            hashtag_name = request.POST.get('hashtag-name')
            if Group.objects.filter(id=group_id).exists() and hashtag_name:  # check if group exists and hashtag name is not empty
                group = Group.objects.get(id=group_id)
                hashtag = Hashtag(name=hashtag_name, group=group)
                hashtag.save()
                messages.success(request, 'Hashtag successfully added.')
            else:
                messages.error(request, 'Invalid group or empty hashtag name.')
        except Exception as e:
            messages.error(request, f'Error adding hashtag: {e}')
    return redirect('blog')

@login_required(login_url='/accounts/login/')
def delete_hashtag(request):
    if request.method == "POST":
        try:
            hashtag_id = request.POST.get('hashtag-id')
            if Hashtag.objects.filter(id=hashtag_id).exists():  # check if hashtag exists
                hashtag = Hashtag.objects.get(id=hashtag_id)
                hashtag.delete()
                messages.success(request, 'Hashtag successfully deleted.')
            else:
                messages.error(request, 'Hashtag does not exist.')
        except Exception as e:
            messages.error(request, f'Error deleting hashtag: {e}')
    return redirect('blog')
