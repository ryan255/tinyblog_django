# tinyblog_django
>  - 极简的blog系统
>  - 版本：django1.9 python2.7 
>  - 评论模块使用多说社会化评论

![cmd-markdown-logo](example.png)

###tips：<br>
1. 教程使用是django1.7之前的版本 在1.7之后 dajngo取消了 syncdb 命令
2. 在django1.9版本中 对应的命令换为 migrate <br>
3. 增加url的时候如果用到include 要记得导入include即：<br>
   from django.conf.urls import patterns, include, url <br>
4. 使用多说的时候，如果想直接使用不配置站点,那么settings中使用如下配置<br>
   DUOSHUO_SECRET = 'xxxxx' <br>
   DUOSHUO_SHORT_NAME = 'xxxxx'


###参考资料： <br>
- Growth 实战篇 Django版 http://phodal.github.io/growth-in-action-django/ <br>
- Django:快速搭建简单的Blog http://my.oschina.net/matrixchan/blog/184445?fromerr=4SM241Ah <br>
- 多说for python sdk  http://dev.duoshuo.com/python-sdk <br>
