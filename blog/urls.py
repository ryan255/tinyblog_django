from django.conf.urls import *
from blog.views import *
from mysite import settings
urlpatterns = patterns('',
                      url(r'^$',index),
                       url(r'^comment/$', comment),
                        url(r'^detail/(?P<BlogPost_id>[0-9]+)/', get_detail, name='detail'),
                      )