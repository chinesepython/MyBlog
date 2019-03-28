from django.contrib import admin
from .models import Article, Category, Tag


# 定制admin后台
class ArticleAdmin(admin.ModelAdmin):
    # 显示的字段
    list_display = ['title', 'created_time', 'last_mod_time', 'category', 'author']
    pass


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)
