from django import forms
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.contrib.sessions import serializers
from django.core.serializers import json
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate
import datetime
# Create your views here.
from blog import models
from blog.models import Post, BlogPost
from blog.news import news
# import itchat
import json
from django.http import HttpResponse


def index(request):
    # return HttpResponse("hello world!")
    print("进入index()，下面是爬虫操作")
    dic = news()
    # print("dic", dic)
    # posts = User.objects.all()

    for d in dic:
        # print(d)
        # time = d[2].split('/')
        # timestamp = "2018-"+time[0]+"-"+time[1]+

        nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')  # 现在
        flag = models.BlogPost.objects.filter(title=d[1])
        if flag:
            print("该数据已经存在")

        else:

            models.BlogPost.objects.create(title=d[1], body=d[0], timestamp=nowTime)

    return render(request, "index.html")


user_list = [
    {"user": "jack", "pwd": "abc"},
    {"user": "tom", "pwd": "ABC"},
]


def hnuer(request):
    print("进入hnuer（）")
    # if request.method == 'POST':
    #     print("进入huner-POST（）")
    #     uf = UserForm(request.POST)
    #     print("uf = ", uf)
    #     if uf.is_valid():
    #         # 获取表单用户密码
    #         print("获取表单用户密码 = ")
    #         username = uf.cleaned_data['username']
    #         password = uf.cleaned_data['password']
    #         print("u&p = ", username, password)
    #         # pwd = make_password(password)   # , 'm*m2$v)cwpg8%x036$y*8n_a*oq8v^sys2s+c^i3&ma_xdflz', 'pbkdf2_sha1'
    #         print("pwd = ")
    #         # 获取的表单数据与数据库进行比较
    #
    #         users = User.objects.all()
    #
    #         for user in users:
    #             print("test", user.username, user.password)
    #             if user.username == username:   # and check_password(password, user.password):
    #                 # user_list = user.objects.all()
    #                 # context = {'user_list': user_list}
    #                 print("登录成功")
    #
    #                 print(username, password)
    #                 # return render_to_response('hnuer.html', {'username': username})
    #                 return render(request, "hnuer.html", {'username': username})

    # models.BlogPost.objects.create(d)

    post_list = BlogPost.objects.all()  # 读取数据库中的所有文章
    print(post_list)
    return render(request, "hnuer.html", context={'post_list': post_list})


# 定义表单模型


class UserForm(forms.Form):
    username = forms.CharField(label='用户名：', max_length=100)
    password = forms.CharField(label='密码：', widget=forms.PasswordInput())


#  登录


def login(request):
    print("进入login（）")

    return render(request, 'login.html')


def weichat_test(request):
    if request.method == 'GET':
        # news = models.BlogPost.objects.all()  # 读取数据库中的所有文章
        # news = serializers.serialize('json', news)
        # print(news)
        # return JsonResponse(list(news), safe=False)
        print("get")

        news = [
            {"title": "标题1", "body": "文章", "time": "时间"},
            {"title": "标题1", "body": "文章", "time": "时间"},
            {"title": "标题1", "body": "文章", "time": "时间"}
                ]
        # news = serializers.serialize('json', news)
        print('news=', news)
        return HttpResponse(json.dumps(news), content_type="application/json")
    else:
        print("else")
        news = [
            {'title': '标题', 'body': '文章', 'time': '时间'},
            {'title': '标题', 'body': '文章', 'time': '时间'},
            {'title': '标题', 'body': '文章', 'time': '时间'}
        ]

        print('news=', news)
        return HttpResponse(json.dumps(news), content_type="application/json")

