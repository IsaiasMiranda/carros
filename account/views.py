from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import CreateView

class Register(CreateView):
    model = UserCreationForm
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = '/login/'

def LoginAuth(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('cars_list')
        else:
            loginForm = AuthenticationForm()
    else:
        loginForm = AuthenticationForm()
    return render(
        request,
        'login.html',
        {
            'loginForm': loginForm,
        }
    )

def LogoutAuth(request):
    logout(request)
    return redirect('cars_list')