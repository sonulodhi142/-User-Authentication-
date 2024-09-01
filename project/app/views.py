
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout

def register(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')  # Use get() method to avoid KeyError
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            return redirect('home')

    return render(request, 'registration/register.html')


def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username,  password =password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'registration/login.html', {'error': 'Invalid credentials'})
    return render(request, 'registration/login.html')

def userLogout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

