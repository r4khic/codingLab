from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import User, Profile, Professor
from .forms import SignUpForm, LoginForm


def index(request):
    return render(request, "index.html")


def home(request):
    return render(request, "base.html")


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Congratulations, you are now a registered user!")
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def log_in(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid email or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect(reverse('login'))


@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    return render(request, 'profile.html', {'profile': profile, 'user': user})


@login_required
def edit_profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    if request.method == "POST":
        new_firstname = request.POST.get('firstname')
        new_secondname = request.POST.get('secondname')
        new_email = request.POST.get('email')
        new_nickname = request.POST.get('nickname')
        new_organization = request.POST.get('organization')
        user.first_name = new_firstname
        user.second_name = new_secondname
        user.email = new_email
        profile.nickname = new_nickname
        profile.organization = new_organization
        user.save()
        profile.save()
    return render(request, 'edit_profile.html', {'profile': profile, 'user': user})


def someone_profile(request):
    return render(request, 'someone_profile.html')


@login_required
def add_profile(request):
    if request.method == "POST":
        first_name = request.POST.get('fname')
        second_name = request.POST.get('sname')
        organization = request.POST.get('organization')
        email = request.POST.get('Email')
        professor_instance = Professor.objects.create(first_name, second_name, organization, email)
    return render(request, 'add_profile.html')
