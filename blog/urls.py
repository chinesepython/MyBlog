from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'hello/', views.index_test, name='index_test'),
    url(r'index/', views.index, name='index')

]