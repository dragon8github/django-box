from django.core.paginator import Paginator # 引入分页组件
from django.http import JsonResponse
from blog.models import Blog

def blog_list(request):
	# 获取GET参数 page，默认为1
	page = request.GET.get('page', 1)

	# 获取GET参数 page_size，默认为1
	page_size = request.GET.get('page_size', 10)

	blogs_qs = Blog.objects.all()
	paginator = Paginator(blogs_qs, page_size)

	current_page = paginator.get_page(page)`
	blogs = current_page.object_list

	ctx = {
		'blog_list': [
			{ 'id': blog.article_id, 'title': blog.title } for blog in blogs 
		],
		'paginator': {
			'total_count': paginator.count,
			'num_pages': paginator.num_pages,
			'page_size': paginator.per_page,
			'page_number': current_page.number,
		}
	}

	return JsonResponse(ctx)

def blog_detail(request, id):
	# blog = Blog.objects.get(article_id=id)
	# 如果查找不到，上面的这条语句会报错，必须用try，
	# 可以用下面的filter + first 代替
	blog = Blog.objects.filter(article_id=id).first()

	# 默认输出空对象
	ctx = {}

	# 如果不为空的话
	if blog is not None:
		# 正确的内容
		ctx = {
			'blog': {
				'id': blog.article_id,
				'title': blog.title,
				'content': blog.content,
				'author': {
					'id': blog.author.id,
					'username': blog.author.username,
				}
			}
		}
	
	return JsonResponse(ctx)