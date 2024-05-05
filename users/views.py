from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, update_session_auth_hash, login, logout
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    SetPasswordForm,
)
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def profile(request):
    return render(request, "users/profile.html")


def register_user(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Register Successfully")
    else:
        form = CreateUserForm()
    return render(request, "users/form.html", {"form": form, "type": "Sign Up"})


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                messages.success(request, "Logged In Successfully")
                login(request, user)
                return redirect("profile")
            else:
                messages.error(request, "Username or password wrong")
    else:
        form = AuthenticationForm()
    return render(request, "users/form.html", {"form": form, "type": "Login"})


def logout_user(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully')
    return redirect("login")


def change_user_pass(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Password change successfully")
            update_session_auth_hash(request, form.user)
            return redirect("profile")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "users/form.html", {"form": form, "type": "Change Password"})


def change_pass_without_pass(request):
    if request.method == "POST":
        form = SetPasswordForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Password change successfully")
            update_session_auth_hash(request, form.user)
            return redirect("profile")
    else:
        form = SetPasswordForm(request.user)
    return render(
        request,
        "users/form.html",
        {"form": form, "type": "Change Password With Old Password"},
    )
