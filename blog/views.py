from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import *
# Create your views here.

def index(request):
	"""
	Tampilakan semua post di index
	"""
	list_post = Post.objects.filter(status='p').order_by('-created_at')
	paginator = Paginator(list_post, 10)
	page = request.GET.get('page')

	try:
		pages = paginator.page(page)
	except PageNotAnInteger:
		pages = paginator.page(1)
	except:
		pages = paginator.page(paginator.num_pages)

	data = {
		'posts' : pages
	}

	return render(request, 'index.html', data)


def post_show(request, slug):
	"""
	Tampilkan post detail dengan slug
	"""
	data_post = Post.objects.get(slug=slug)

	data = {
		'post' : data_post
	}
	return render(request, 'detail.html', data)


def category_list(request, cat):
	"""
	Tampilkan semua data berdasarkan kategori
	Jika kategori tidak ada kita redirect ke halaman depan
	"""
	try:
		cat = Category.objects.get(name=cat)
	except Category.DoesNotExist:
		return redirect('index')

	cat_list = Post.objects.filter(status='p', category=cat.pk).order_by('-created_at')

	paginator = Paginator(cat_list, 10)
	page = request.GET.get('page')

	try:
		pages = paginator.page(page)
	except PageNotAnInteger:
		pages = paginator.page(1)
	except:
		pages = paginator.page(paginator.num_pages)

	data = {
		'posts' : pages,
		'category' : cat.name
	}

	return render(request, 'category_list.html', data)


def author_list(request, author):
	"""
	Tampilkan semua post berdasarkan author
	Jika author tidak ada maka di redirect ke halaman depan
	"""
	try:
		usr = User.objects.get(username=author)
	except User.DoesNotExist:
		return redirect('index')

	post = Post.objects.filter(status='p', creator=usr.pk).order_by('-created_at')

	paginator = Paginator(post, 10)

	page = request.GET.get('page')

	try:
		pages = paginator.page(page)
	except PageNotAnInteger:
		pages = paginator.page(1)
	except:
		pages = paginator.page(paginator.num_pages)

	data = {
		'posts' : post,
		'author' : author
	}

	return render(request, 'author_list.html', data)

