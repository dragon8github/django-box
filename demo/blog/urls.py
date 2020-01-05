from django.urls import path
import blog.views as V

urlpatterns = [
	path('list/', V.blog_list),
	path('detail/<int:id>/', V.blog_detail),
]