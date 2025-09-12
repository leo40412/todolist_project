from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Todo

# Create your views here.


def create_todo(request):
    # GET(網址的部分是get)
    # POST(表單送出)
    message = ""  # 提示錯誤
    if request.method == "POST":
        print(request.POST)
        title = request.POST.get("title")
        if title == "":
            print("標題欄位不能為空")
            message = "標題欄位不能為空"
        else:
            text = request.POST.get("text")
            important = request.POST.get("important")

            important = True if important == "on" else False

            # 建立資料
            todo = Todo.objects.create(title=title, text=text, important=important)
            todo.save()  # commit
            message = "建立成功"
    return render(request, "todo/create_todo.html", {"message": message})


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
