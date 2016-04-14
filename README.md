# tinyblog_django
版本：django1.9 python2.7 <br>
参考了 Growth 实战篇 Django版 http://phodal.github.io/growth-in-action-django/
搭建的极简的blog系统<br>

教程使用是django1.7之前的版本 在1.7之后 dajngo取消了 syncdb 命令
在django1.9版本中 对应的命令换为 migrate <br>
增加url的时候如果用到include 要记得导入include即：<br>
from django.conf.urls import patterns, include, url
