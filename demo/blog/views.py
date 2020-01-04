from django.http import JsonResponse
from blog.models import Blog

def blog_list(request):
	blogs = Blog.objects.all()

	print(blogs)

	ctx = {
		'blog_list': [
			{ 
				'id': blog.article_id, 
				'title': blog.title 
			} for blog in blogs
		]
	}

	return JsonResponse(ctx)

def blog_detail(request, article_id):
	blog = Blog.objects.get(id=article_id)

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

	return JSONResponse(ctx)