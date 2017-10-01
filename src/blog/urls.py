from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$',  views.post_list , name='post_list'),
        url(r'^(?P<slug>[\w-]+)/$', views.post_detail, name="detail"),
        url(r'^category/(?P<hierarchy>.+)/$', views.show_category, name='category'),
        ]
