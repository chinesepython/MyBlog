from django.conf.urls import url
from . import views

# 通过 app_name='blog' 告诉 Django 这个 urls.py 模块是属于 blog 应用的，
# 这种技术叫做视图函数命名空间。我们看到 blog\urls.py 目前有两个视图函数，
# 并且通过 name 属性给这些视图函数取了个别名，分别是 index、detail。
# 但是一个复杂的 Django 项目可能不止这些视图函数，例如一些第三方应用中也可能有叫 index、detail 的视图函数，
# 那么怎么把它们区分开来，防止冲突呢？方法就是通过 app_name 来指定命名空间，命名空间具体如何使用将在下面介绍。
# 如果你忘了在 blog\urls.py 中添加这一句，接下来你可能会得到一个 NoMatchReversed 异常。
app_name = 'blog'
urlpatterns = [
    url(r'hello/', views.index_test, name='index_test'),
    url(r'index/', views.index, name='index'),
    # 正则表达式表示的意思是以post开头，后面至少跟一个数字，并且以/结尾
    # 如 post/1/、 post/255/ 等都是符合规则的，[0-9]+ 表示一位或者多位数
    # (?P<pk>[0-9]+) 表示命名捕获组，其作用是从用户访问的 URL 里把括号内匹配的字符串
    #  捕获并作为关键字参数传给其对应的视图函数 detail
    #  如当用户访问 post/255/ 时，被括起来的部分 (?P<pk>[0-9]+) 匹配 255，那么这个 255 会在调用视图函数 detail 时被传递进去，
    #  实际上视图函数的调用就是这个样子：detail(request, pk=255)
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
]
