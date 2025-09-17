from django.forms import ModelForm
from .models import Todo


class CreateTodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "text", "important"]
        # fields = "__all__"  # 全部資料庫資料欄


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "text", "important", "completed"]
        # fields = "__all__"  # 全部資料庫資料欄
