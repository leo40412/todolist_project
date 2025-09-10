from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Todo

# Create your views here.


def view_todo(request, id):
    todo = None  # 寫錯的話也要回傳
    try:
        todo = Todo.objects.get(id=id)  # .get 唯一
    except Exception as e:
        print(e)

    return render(request, "todo/view_todo.html", {"todo": todo})


def todolist(request):
    todos = Todo.objects.all()  # todo資料庫全部資料
    return render(request, "todo/todolist.html", {"todos": todos})


def index(request):
    return HttpResponse("<h1>Hello django!</h1>")


def books(request):
    my_books = {1: "python", 2: "java", 3: "C#book"}
    return HttpResponse(json.dumps(my_books), content_type="application/json")
