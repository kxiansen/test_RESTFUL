from django.contrib import admin

# Register your models here.
from api import models  # 记得导包


@admin.register(models.Student)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # 在后台列表下显示的字段

# admin.site.register(models.Student)