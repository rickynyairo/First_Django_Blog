from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
	fieldsets = [
		('Blog Post', {'fields':['title', 'slug','author', 'body']}),('Date Information', {'fields':['date_published', 'status']}),
	]
	list_display = ('title', 'slug', 'date_published', 'status')
	list_filter = ['status','author','date_published']
	search_fields = ['title','author']
	prepopulated_fields = {'slug':('title',)}
	raw_id_fields = ('author',)
	date_hierarchy = 'date_published'
	ordering = ['status', 'date_published']

admin.site.register(Post, PostAdmin)