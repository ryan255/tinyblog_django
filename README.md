# tinyblog_django
#极简的blog系统<br>
##版本：django1.9 python2.7 <br>
##评论模块使用多说社会化评论
##完成效果：<br>
![demo](/屏幕快照 2016-04-28 下午6.54.09.png)
tips：
教程使用是django1.7之前的版本 在1.7之后 dajngo取消了 syncdb 命令
在django1.9版本中 对应的命令换为 migrate <br>
增加url的时候如果用到include 要记得导入include即：<br>
from django.conf.urls import patterns, include, url

参考资料： <br>
1. Growth 实战篇 Django版 http://phodal.github.io/growth-in-action-django/ <br>
2. Django:快速搭建简单的Blog http://my.oschina.net/matrixchan/blog/184445?fromerr=4SM241Ah <br>
3. 多说for python sdk http://dev.duoshuo.com/python-sdk <br>
