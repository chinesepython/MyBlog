import markdown
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article, Category

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


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.body = markdown.markdown(article.body,
                                     extensions=[
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                         'markdown.extensions.toc',
                                     ])
    return render(request, 'blog/detail.html', context={'article': article})


# 归档
def archives(request, year, month):
    article_list = Article.objects.filter(created_time__year=year,
                                          created_time__month=month,
                                          ).order_by('-created_time')
    # 返回需要的文章
    return render(request, 'blog/index.html', context={"article_list": article_list})


# 分类
def category(request, pk):
    # 根据id获取分类名
    cate = get_object_or_404(Category, pk=pk)
    # 根据分类名查找该分类下的所有文章
    article_list = Article.objects.filter(category=cate).order_by('-created_time')
    print(article_list)
    return render(request, 'blog/index.html', context={"article_list": article_list})
