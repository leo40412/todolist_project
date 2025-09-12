from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from .models import Todo
from .forms import TodoForm

# Create your views here.


def create_todo(request):
    message = ""  # 提示錯誤
    form = TodoForm()

    if request.method == "POST":
        form = TodoForm(request.POST)
        form.save()
        message = "建立成功"
        return redirect("todolist")  # 跳轉到首頁
    return render(request, "todo/create_todo.html", {"message": message, "form": form})


def view_todo(request, id):
    todo = None  # 寫錯的話也要回傳
    try:
        todo = Todo.objects.get(id=id)  # .get 唯一
    except Exception as e:
        print(e)

    return render(request, "todo/view_todo.html", {"todo": todo})


def todolist(request):
    todos = Todo.objects.all().order_by("-created")
    # order_by -> 排序
    # - 降序
    # all() todo資料庫全部資料
    return render(request, "todo/todolist.html", {"todos": todos})


def index(request):
    return HttpResponse("<h1>Hello django!</h1>")


def books(request):
    my_books = {1: "python", 2: "java", 3: "C#book"}
    return HttpResponse(json.dumps(my_books), content_type="application/json")
