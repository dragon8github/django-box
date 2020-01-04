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

	# 自定义 column
	def email(self):
		return '%s' % self.author.email

	# 定义 column
	email.short_description = '电子邮箱'