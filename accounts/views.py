from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.models import User
# @unauthenticated_user
from django.contrib.auth.hashers import make_password


def signin(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username)
            user = authenticate(request, username=username, password=password)
            if user is None:
                messages.error(request, "User not found or not activated!")
                return render(request, 'accounts/login.html')
            else:
                login(request, user)
                return redirect('index')
        else:
            print("This is not POST method")

        return render(request, 'accounts/login.html')
    except Exception:
        print(Exception)
    return render(request, 'login.html')


def register(request):

    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            if password == confirm_password:
                customer = User.objects.create(
                    username=username, email=email)
                # customer.set_password(self.cleaned_data["password"])
                print("Hereeee......................")
                customer.save()
                return render(request, 'accounts/login.html')
            else:
                return redirect('register')
        else:
            print("This is not POST method")

    except Exception as ex:
        print(ex)
    return render(request, 'accounts/register.html')


def logout_user(request):
    logout(request)
    return redirect('index')
