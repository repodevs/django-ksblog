from django.contrib import admin

from .models import *
# Register your models here.

''' POST ADMIN '''

def make_published(self, request, queryset):
	queryset.update(status='p')
make_published.short_description = 'Publish Post yang ditandai'

def make_draft(self, request, queryset):
	queryset.update(status='d')
make_draft.short_description = 'Draft Post yang ditandai'

def make_archive(self, request, queryset):
	queryset.update(status='a')
make_archive.short_description = 'Archive Post yang ditandai'

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'creator', 'status', 'created_at')
	list_filter = ['creator', 'status']
	actions =[make_published, make_draft, make_archive]
	search_fields = ('title', 'content')

''' POST CATEGORY '''

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'created_at')

# register to admin page
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)