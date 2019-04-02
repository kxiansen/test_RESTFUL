django+rest framework实现api接口  网站源码
=================
[![Docker Stars](https://img.shields.io/docker/stars/billvsme/vmaig_blog.svg)](https://hub.docker.com/r/kxiansen/test_RESTFUL/)
# 有问题欢迎加我
我的qq: 1289834599  

[使用Docker部署vmaig_blog](http://xxx/article/test_RESTFUL.html)

# 更新日志
1.8
2.1


# 概述
vmaig\_blog 是一个基于  **Django1.8**  跟  **Bootstrap3**  开发的 **博客系统** ，实现了一个博客完整的功能。https://vmaig.com 就是基于vmaig\_blog 搭建的。
# 功能
...未完善


# Demo
https://xxx.com   

# 预览
![首页](http://xxx.01.jpg)
![头像](http://xxx.02.jpg)
![评论](http://xxx.3.jpg)
![新闻](http://xxx.news.jpg)

# 安装运行
安装virtualenv :

    sudo pip install virtualenv

创建并激活虚拟环境 :

    virtualenv www
    cd www
    source bin/active

下载代码,切换目录 :
    
    git clone https://github.com/kxiansen/test_RESTFUL
    cd test_RESTFUL



    pip install -r requirements.txt

配置setting.py :


初始化数据库 :

    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    
运行 :
    
    python manage.py runserver 0.0.0.0:80
    
    
# 生产环境部署
	
使用docker部署，首先pull下来image或者自己使用项目中Dockerfile或者Dockerfile_cn build。
	
	sudo docker pull kxiansen/test_RESTFUL
然后运行image  
	例子:
	
	sudo docker run -d -p 80:80 --name test_RESTFUL \
                            -e WEBSITE_TITLE='test_RESTFUL'\
                            -e SECRET_KEY='django secret key'\
                            -e WEBSITE_WELCOME='欢迎来到vmaig'\
                            -e EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend' \
                            -e EMAIL_HOST='smtp.163.com'\
                            -e EMAIL_PORT='25'\
                            -e EMAIL_HOST_USER='yourname@163.com'\
                            -e EMAIL_SUBJECT_PREFIX='vmaig'\
                            -e EMAIL_HOST_PASSWORD='yourpassword'\
                            -e QINIU_ACCESS_KEY='your_as_key'\
                            -e QINIU_SECRET_KEY='your_sr_key'\
                            -e QINIU_URL='your_url'\
                            -e QINIU_BUCKET_NAME='your_bucket_name'\
                            kxiansen/test_RESTFUL
    
**环境变量**:  
	

# 接下来该干什么？
在浏览器中输入 http://127.0.0.1/api  

