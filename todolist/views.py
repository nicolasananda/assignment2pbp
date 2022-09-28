from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from todolist.models import Task
import datetime

# Create your views here.


@login_required(login_url="/todolist/login/")
def show_todolist(request):
    # u = User.objects.get(username=request.user)
    todolist_objects = Task.objects.filter(user=request.user)
    context = {"todolist": todolist_objects, "username": request.user}
    return render(request, "todolist.html", context)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account succesfully created!")
            return redirect("todolist:login")

    context = {"form": form}
    return render(request, "register.html", context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(
                reverse("todolist:show_todolist")
            )
            response.set_cookie(
                "last_login", str(datetime.datetime.now())
            )
            return response
        else:
            messages.info(request, 'Wrong Username or Password!')
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse("todolist:login"))
    response.delete_cookie("last_login")
    return response


@login_required(login_url="/todolist/login/")
def create_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            date=datetime.datetime.today(),
        )
        return HttpResponseRedirect(reverse("todolist:show_todolist"))
    return render(request, "create_task.html")


@login_required(login_url="/todolist/login/")
def delete_task(request, id):
    task = Task.objects.get(user=request.user, id=id)
    task.delete()
    return HttpResponseRedirect(reverse("todolist:show_todolist"))


@login_required(login_url="/todolist/login/")
def update_finished(request, id):
    task = Task.objects.get(user=request.user, id=id)
    task.is_finished = not task.is_finished
    task.save(update_fields=["is_finished"])
    return HttpResponseRedirect(reverse("todolist:show_todolist"))