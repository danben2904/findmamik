from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.models import User, Group

from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm, SeekerForm, MamikForm, ChildForm
from .decorators import unauthenticated_user
from .models import Seeker

from random import uniform

@login_required(login_url="main:login")
def home(request):
    context = {}
    return render(request, "main/home.html", context)

@unauthenticated_user
def registerPage(request):

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            Seeker.objects.create(user=user, email=user.email)
            return redirect("main:login")

    context = {"form":form}
    return render(request, "main/register.html", context)

@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
    
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("main:home")
        else:
            messages.info(request, "username or passoword in incorrect")

    context = {}
    return render(request, "main/login.html", context)

def logoutUser(request):
    logout(request)
    return redirect("main:login")

def userPage(request, username):
    user = get_object_or_404(User, username=username)
    context = {"user" : user}
    return render(request, "main/user.html", context)

@login_required(login_url="main:login")
def accountSettings(request):
    seeker = request.user.seeker
    form = SeekerForm(instance=seeker)

    if request.method == "POST":
        form = SeekerForm(request.POST, request.FILES, instance=seeker)
        if form.is_valid():
            form.save()

    context = {"form" : form}
    return render(request, "main/account_settings.html", context)
    
def get_mamiks(min_age, max_age, min_salary):
    return User.objects.filter(
        seeker__is_mamik=True
    ).filter(
        seeker__is_free=True
    ).exclude(
        seeker__age__lt=min_age
    ).exclude(
        seeker__age__gt=max_age
    ).exclude(
        seeker__salary__lt=min_salary
    )

def get_children(min_age, max_age):
    return User.objects.filter(
        seeker__is_mamik=False
    ).filter(
        seeker__is_free=True
    ).exclude(
        seeker__age__lt=min_age
    ).exclude(
        seeker__age__gt=max_age
    )

@login_required(login_url="main:login")
def find(request):
    results = []
    data = []
    if request.user.seeker.is_mamik:
        form = ChildForm()
        if request.method == 'POST':
            form = ChildForm(request.POST)
            if form.is_valid():
                min_age = form.cleaned_data['min_age']
                max_age = form.cleaned_data['max_age']
                data = get_children(min_age, max_age)
    else:
        form = MamikForm()
        if request.method == 'POST':
            form = MamikForm(request.POST)
            if form.is_valid():
                min_age = form.cleaned_data['min_age']
                max_age = form.cleaned_data['max_age']
                min_salary = form.cleaned_data['min_salary']
                data = get_mamiks(min_age, max_age, min_salary)
    array = []
    for user in data:
        array.append(user)
    user_number = len(array)
    for i in range(user_number):
        for j in range(user_number - i - 1):
            if array[j].seeker.loyalty_points > array[j + 1].seeker.loyalty_points:
                if uniform(0, 1) < 9e-1:
                    array[j], array[j + 1] = array[j + 1], array[j]
    array.reverse()
    array = array[:20]
    context = {"form" : form, "data" : array}
    return render(request, "main/find.html", context)
