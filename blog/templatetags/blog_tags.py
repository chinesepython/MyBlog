from ..models import Article, Category
from django import template


register = template.Library()
# 这个函数的功能是获取数据库中前 num 篇文章，这里 num 默认为 5。
# 函数就这么简单，但目前它还只是一个纯 Python 函数，Django 在模板中还不知道该如何使用它。
# 为了能够通过 {% get_recent_posts %} 的语法在模板中调用这个函数，必须按照 Django
# 的规定注册这个函数为模板标签


# 定义最新文章模板标签
@register.simple_tag
def get_recent_articles(num=5):
    return Article.objects.all().order_by('-created_time')[:num]


# 定义归档模板标签
# 和最新文章标签一样，先写好函数，然后注册为模板标签即可
@register.simple_tag
def archives():
    # dates 方法会返回一个列表，列表中的元素为每一篇文章（Post）的创建时间，且是 Python 的 date 对象
    # created_time ，即 Post 的创建时间，month 是精度，order='DESC' 表明降序排列（即离当前越近的时间越排在前面）
    return Article.objects.dates('created_time', 'month', order='DESC')


# 定义分类模板标签
@register.simple_tag
def get_categories():
    return Category.objects.all()

