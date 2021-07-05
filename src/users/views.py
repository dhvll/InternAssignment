from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,get_user_model,login,logout

from .forms import UserLoginForm, UserRegisterForm

@login_required
def home(request):
    context = {}
    return render(request, 'users/home.html', context)

def loginUser(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('home')

    context = {'form': form}
    return render(request, 'users/login.html', context)

def registerUser(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('login')

    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')