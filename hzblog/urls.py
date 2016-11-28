from django.conf.urls import url
from . import views

app_name = 'hzblog'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_view, name='post_view'),
    url(r'^drafts/$', views.post_drafts, name='post_drafts'),
    url(r'^post/create/$', views.post_create, name='post_create'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/publish/$',views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>[0-9]+)/delete/$', views.post_delete, name='post_delete'),
]
