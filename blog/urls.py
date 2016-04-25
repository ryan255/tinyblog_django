from django.conf.urls import *
from blog.views import index
from mysite import settings
urlpatterns = patterns('',
                      url(r'^$',index),
                        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': settings.STATIC_URL}),
                      )