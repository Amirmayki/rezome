from django.shortcuts import render, redirect

from django.contrib.auth import login

from .forms import RegisterForm


def register_view(request):

    form = RegisterForm()

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect("dashboard")

    return render(

        request,

        "accounts/register.html",

        {

            "form": form

        }

    )


def login_view(request):

    return render(

        request,

        "accounts/login.html"

    )


def dashboard(request):

    return render(

        request,

        "accounts/dashboard.html"

    )


def profile(request):

    return render(

        request,

        "accounts/profile.html"

    )