from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def index_test(request):
    return HttpResponse("hello world")


# def index(request):
#
#     return render(request, 'blog/index.html', context={
#         "title": "我的博客首页",
#         "welcome": "欢迎访问我的博客首页",
#     })

def index(request):
    article_list = Article.objects.all()
    return render(request, 'blog/index.html', context={'article_list': article_list})
