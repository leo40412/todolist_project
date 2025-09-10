from django.contrib import admin
from .models import Todo  # . 當前目錄 不能省略

# Register your models here.


admin.site.register(Todo)
