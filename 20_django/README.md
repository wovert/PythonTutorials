# Django 
## Django 版本 Python 版本
- 1.5.x         2.6.5/2.7/3.2/3.3
- 1.6.x         2.6/2.7/3.2/3.3
- 1.7.x         2.7/3.2/3.3/3.4
- 1.8.x          2.7/3.2/3.3/3.4/3.5 LTS
- 1.9.x         2.7/3.4/3.5    
- 1.10.x     2.7/3.4/3.5
- 1.11.x     2.7/3.4/3.5/3.6 LTS
- 2.0.x          3.4/3.5/3.6
- 2.1.x          3.5/3.6/3.7


## django 项目结构
`$ django-admin startproject 项目名`
- manager.py
- 项目名
   + `__init__.py` 标识模块
   + settings.py 项目配置文件
   + urls.py 
   + wsgi.py 动态网管接口
`$ python manage.py help`
`$ python manage.py startapp blog`
`$ cd blog`
   + `__init__.py`
   + migrations 数据库版本管理 v1.7+
      * `__init__.py`
   + admin.py
   + models.py
   + views.py
   + tests.py

- 启动服务
`$ python3 manage.py runserer`

- 数据同步
`$ python3 manage.py migrate`

- 创建数据库
`$ python3 manage.py makemigrations`
