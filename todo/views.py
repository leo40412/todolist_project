from django.shortcuts import render
from django.http import HttpResponse
import json


# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello django!</h1>")


def books(request):
    my_books = {1: "python", 2: "java", 3: "C#book"}
    return HttpResponse(json.dumps(my_books), content_type="application/json")
