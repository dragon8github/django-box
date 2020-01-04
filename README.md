# install

https://www.djangoproject.com/download/

3.x 版本有问题。而且市场上大部分的教程都是2.x，建议从 2.x 入手再说。

如果你真的入手了，那么升级肯定不是大问题了。因为你已经有经验和信心了。

```bash
pip install Django==2.2
```

```bash
django-admin startproject demo
```

```bash
python manage.py startapp blog
```

models.py

```python
from django.db import models

class Blog(models.Model):

	# id
	article_id = models.AutoField(primary_key=True)

	# 作者
	author = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, verbose_name='作者')

	# 标题
	title = models.CharField(u'标题', max_length=50)

	# 摘要
	brief_content = models.TextField(u'摘要', max_length=100)

	# 内容
	content = models.TextField(u'内容')

	# 发布时间
	publish_date = models.DateTimeField(auto_now=True)

	# 定义 admin 列表标题
	def __str__(self):
		return self.title
```

admin.py

```python
from django.contrib import admin
from blog.models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
	# list_display 用来显示 column
	list_display = ['title', 'author']

	# 开启搜索框，并且定义搜索的字段列表
	search_fields = ['title', 'content']
```


```bash
python manage.py makemigrations --empty blog

python manage.py makemigrations blog
```

```bash
python manage.py migrate blog --fake  

python manage.py migrate
```

```bash
python manage.py createsuperuser
```

```bash
python manage.py runserver 8000
```

```bash
python manage.py shell
```