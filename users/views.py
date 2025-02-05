from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from users.models import CustomUser


def signin_view(request):
    return render(request, 'signin.html')


def authenticate_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('Invalid username or password')
            # return render(request, 'signin.html', {'error': 'Invalid username or password'})

    return redirect('index')


def signup_view(request):
    return render(request, 'signup.html')


def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            messages.error(request, 'Passwords must match')
            return redirect('register_user')

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return redirect('register_user')

        user = CustomUser.objects.create_user(username=username, password=password,)
        user.save()

        messages.success(request, 'Account created')
        return redirect('signin')


@login_required(login_url='signin')
def logout_view(request):
    logout(request)
    return redirect('signin')
