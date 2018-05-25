from django import forms
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.contrib.sessions import serializers
from django.core.serializers import json
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.auth import authenticate
import datetime
# Create your views here.
from blog import models
from blog.models import Post, BlogPost, CostInformation
from blog.news import news
from blog.OneCard import ykt_message
# import itchat
import json
from django.http import HttpResponse
import markdown


def index(request):
    # return HttpResponse("hello world!")
    print("进入index")

    # return render(request, "index.html")
    blog_list = Post.objects.all()  # 读取POST数据库中的所有文章
    print("Read the post")
    return render(request, "index.html", context={'blog_list': blog_list})

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
    # dic = news() # 爬取新闻数据
    # # sorted(dic,reverse=True)
    # for d in sorted(dic,reverse=True):
    #     nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')  # 现在
    #     flag = models.BlogPost.objects.filter(title=d[1])
    #     if flag:
    #         print("该数据已经存在")
    #     else:
    #         models.BlogPost.objects.create(title=d[1], body=d[0], timestamp=nowTime)
    post_list = BlogPost.objects.all()  # 读取数据库中的所有文章

    return render(request, "hnuer.html", context={'post_list': post_list})


class UserForm(forms.Form):
    username = forms.CharField(label='用户名：', max_length=100)
    password = forms.CharField(label='密码：', widget=forms.PasswordInput())


def login(request):
    print("进入login（）")

    return render(request, 'login.html')


def weichat_test(request):     # 请求json数据
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


def OneCard(request):
    print("访问一卡通信息")
    # 爬取一卡通消费信息
    """
    Cost = ykt_message()

    # 存入数据库

    for line in Cost:
        print("ykt_msg = ", line)
        flag = models.BlogPost.objects.filter(data=line[2])
        if flag:
            print("该数据已经存在")
        else:
            models.CostInformation.objects.create(date=line[2], place=line[3], amount=line[1], balance=line[0])
    """
    # models.CostInformation.objects.filter().delete() # 删除数据库中的数据
    # 从数据库取出信息
    Cost = CostInformation.objects.all()

    return render(request, "ykt_message.html", context={'Cost': Cost})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'detail.html', context={'post': post})