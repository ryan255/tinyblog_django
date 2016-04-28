from django.conf.urls import *
from blog.views import *
from mysite import settings
urlpatterns = patterns('',
                      url(r'^$',index),
                       url(r'^comment/$', comment),
                        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': settings.STATIC_URL}),
                      )