from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class DatePublishedManager(models.Manager):
	def get_queryset(self):
		return super(DatePublishedManager, self).get_queryset().filter(status='published')

class Post(models.Model):
	STATUS_CHOICES = (
		('draft','Draft'),
		('published','Published'),
	)
	title = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250, unique_for_date='date_published')
	author = models.ForeignKey(User, related_name='blog_posts')
	body = models.TextField()
	date_published = models.DateTimeField(default=timezone.now)
	date_created = models.DateTimeField(auto_now_add=True)
	last_updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES)

	#default manager
	objects = models.Manager()

	#custom manager
	published = DatePublishedManager()

	class Meta:
		ordering = ('-date_published',)	

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:post_detail_view', args=[self.date_published.year, self.date_published.strftime('%m'), self.date_published.strftime('%d'), self.slug])
		
