from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .models import User
from .forms import MyUserCreationForm
from invoice.forms import SettingsForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def front_page(request):
    return render(request, 'base/front_page.html')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('base:front-page')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('invoice:invoices')
        else:
            messages.error(request, 'Username OR password does not exit')

    # context = {'page': page}
    return render(request, 'base/login.html')


def logoutUser(request):
    logout(request)
    return redirect('base:front-page')


def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('base:front-page')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'base/registration.html', {'form': form})

@login_required(login_url='login')
def home(request, user_id):
    user = User.objects.get(id = user_id)
    
    if user != request.user:
        raise Http404
    
    context = {"user": user}
    return render(request, 'base/home.html', context)

@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = SettingsForm(instance=user)

    if request.method == 'POST':
        form = SettingsForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('invoice:dashboard', user_id=user.id)

    return render(request, 'base/update-user.html', {'form': form})


