from django.conf.urls import url

from . import views

# Konfigurasi untuk url blog

urlpatterns = [
	url(r'^$/', views.index, name='blog_index'),
	url(r'^(?P<slug>[\w-]+)$', views.post_show, name='post_show'),
	url(r'^kategori/(?P<cat>[\w-]+)$', views.category_list, name='category_list'),
	url(r'^author/(?P<author>[\w-]+)$', views.author_list, name='author_list'),
]