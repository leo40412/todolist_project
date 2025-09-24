from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from .models import Todo
from .forms import TodoForm, CreateTodoForm
from datetime import datetime

# Create your views here.


def create_todo(request):
    message = ""  # 提示錯誤
    form = CreateTodoForm()

    if request.method == "POST":
        form = CreateTodoForm(request.POST)
        # 缺少綁定user
        todo = form.save(commit=False)  # 站存
        todo.user = request.user
        todo.save()

        message = "建立成功"
        return redirect("todolist")  # 跳轉到首頁
    return render(request, "todo/create_todo.html", {"message": message, "form": form})


def delete_todo(request, id):
    try:
        todo = Todo.objects.get(id=id)  # .get 唯一
        todo.delete()
    except Exception as e:
        print(e)

    return redirect("todolist")


def view_todo(request, id):
    # todo = None  # 寫錯的話也要回傳
    message = ""
    try:
        todo = Todo.objects.get(id=id)  # .get 唯一
        form = TodoForm(instance=todo)  # 實際物件->instance
    except Exception as e:
        print(e)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)  # 把修改的資料抓出來
        todo = form.save(commit=False)  # 暫存

        if todo.completed:
            todo.date_completed = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            todo.date_completed = None

        form.save()
        message = "更新成功"
        return redirect("todolist")
    return render(
        request, "todo/view_todo.html", {"todo": todo, "form": form, "message": message}
    )


def todolist(request):
    # todos = Todo.objects.all().order_by("-created")
    # order_by -> 排序
    # - 降序
    # all() todo資料庫全部資料
    todos = None
    if request.user.is_authenticated:
        todos = Todo.objects.filter(user=request.user)
    return render(request, "todo/todolist.html", {"todos": todos})


def index(request):
    return HttpResponse("<h1>Hello django!</h1>")


def books(request):
    my_books = {1: "python", 2: "java", 3: "C#book"}
    return HttpResponse(json.dumps(my_books), content_type="application/json")
