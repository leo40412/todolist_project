from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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
            if User.objects.filter(username=username):
                message = "使用者名稱已存在"
            else:
                User.objects.create_user(username=username, password=password1).save()
                message = "使用者註冊成功"

        # 使用者名稱已存在

    return render(request, "user/register.html", {"form": form, "message": message})
