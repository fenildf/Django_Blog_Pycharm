from django.contrib import admin

# Register your models here.
from blog.models import Post, Category, Tag, BlogPost

"""
在models.py里的两个数据表注册到后台让管理员能管理这两个表，
在你新建了其它的表过后也在这里同样的注册）
"""
from django.contrib import admin

# Register your models here.

from django.db import models
from django.contrib import admin


# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category']   # , 'author'


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp']


admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(BlogPost, BlogPostAdmin)
