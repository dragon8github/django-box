from django.contrib import admin
from blog.models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
	# list_display 用来显示 column
	list_display = [
		# 普通字段
		'title', 'author',

		# 自定义字段
		'email',
	]

	# 开启搜索框，并且定义搜索的字段列表
	search_fields = [
		# 普通字段
		'title', 'content',

		# 关联字段，只能通过 __ 来书写，譬如 author
		'author__username', 'author__email'
	]


	# 模拟需求：保存的时候还要选择作者，太麻烦了。 直接变更需求为： 不需要选择作者，作者就是编辑者本身，且不可篡改文章作者。

	# 不可修改作者
	readonly_fields = ['author']

	# 定义保存回调
	def save_model(self, request, obj, form, change):
		# 如果不是修改，那就是“新建”
		if not change:
			# 保存的时候，自定设置当前作者
			obj.author = request.user

		# 调用本函数
		super(BlogAdmin, self).save_model(request, obj, form, change)