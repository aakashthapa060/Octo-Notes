from django import forms
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm, RegisterForm

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect("notes:index")
    else:
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username = username, password = password)
            if user != None:
                login(request, user)
                return redirect("notes:index")
        else:
            print("sorry")
            form = LoginForm()
        context = {
            "form": form
        }
        return render(request, "users/login.html",context)

def register_view(request):
    if request.user.is_authenticated:
        return redirect("notes:index")
    else: 
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("users:login")
        else:
            form = RegisterForm()
        
        context = {
            "form": form
        }
        return render(request, "users/register.html", context)

def logout_view(request):
    logout(request)
    return redirect("users:login")