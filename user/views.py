from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate  # 確認帳號密碼


# Create your views here.
def user_register(request):
    message = ""
    form = UserCreationForm()
    if request.method == "POST":
        print(request.POST)
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # 密碼不能少於8個字元，且兩次密碼相同
        if len(password1) < 8 or len(password2) < 8:
            message = "密碼不能少於8個字元"
        elif password1 != password2:
            message = "兩次密碼不相同"
        else:
            # 使用者名稱已存在
            if User.objects.filter(username=username):
                message = "使用者名稱已存在"
            else:
                User.objects.create_user(username=username, password=password1).save()
                message = "使用者註冊成功"
                return redirect("user_login")

    return render(request, "user/register.html", {"form": form, "message": message})


def user_login(request):
    message = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if not user:
            message = "使用者名稱或密碼錯誤!"
        else:
            login(request, user)
            message = "登陸成功"
            return redirect("todolist")

    return render(request, "user/login.html", {"message": message})
