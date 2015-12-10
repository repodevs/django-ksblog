from __future__ import unicode_literals
from django.contrib.auth.models import User #=> for User who login
from django.template.defaultfilters import slugify
from django.db import models

# ckeditor
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Category(models.Model):
	"""
	Model untuk kategori post
	"""
	name = models.CharField(max_length=60, blank=False)
	description = models.TextField(null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'

	def __unicode__(self):
		return self.name


class Post(models.Model):
	"""
	Model untuk post
	"""

	# choices untuk status post
	STATUS_CHOICES = (
		('d', 'Draft'),
		('p', 'Publish'),
		('a', 'Archieved'),
	)

	creator = models.ForeignKey(User, related_name='user_post', default=1)
	title = models.CharField(max_length=255, blank=False)
	slug = models.SlugField(max_length=255, default='', blank=True, editable=False)	
	category = models.ForeignKey(Category, related_name='post_category', null=True)
	content = RichTextUploadingField()
	image = models.ImageField(upload_to='images/post/%Y/%m/%d/', blank=True)
	status = models.CharField(max_length=1, default='d', choices=STATUS_CHOICES)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = 'Post'
		verbose_name_plural = 'Posts'

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Post, self).save(*args, **kwargs)


			