from django.conf.urls import url
from . import views

app_name = "blog"
urlpatterns = [
  url(r'^$', views.post_list, name='post_list'),
  url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
    views.post_detail, name='post_detail'),
]
#
#path('<year:year>,<month:month>,<day:day>,<post:post>', views.post_detail, name="post_detail"),
#url(r'^(?P<slug>[-\w\d]+),(?P<id>\d+)/$', views.post_detail, name="post_detail")
