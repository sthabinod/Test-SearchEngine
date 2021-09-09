from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.models import User


def index(request):
    users = User.objects.all()
    data = {
        'users': users
    }
    return render(request, 'index.html', data)


def search(request):
    if request.method == 'POST':
        word_to_search = request.POST.get('text')
        users = User.objects.filter(username__startswith=word_to_search)
        user_count = User.objects.filter(
            username__startswith=word_to_search).count

        data = {
            'users': users,
            'user_count': user_count,
        }
        return render(request, 'index.html', data)
    else:
        return redirect('index')


def search_(request):
    if request.method == 'POST':
        staff = request.POST.get('staff')
        user = request.POST.get('normal')
        print(staff, user)
        users = User.objects.filter(is_staff=staff)
        user_count = User.objects.filter(
            is_staff=staff).count

        data = {
            'users': users,
            'user_count': user_count,
        }
        return render(request, 'index.html', data)
    else:
        return redirect('index')
