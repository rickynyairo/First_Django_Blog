from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post

class PostsFeeds(Feed):
	title = "Ricky's Django Blog Feeds"
	link = "/blog/"
	description = "Our latest posts"

	def items(self):
		return Post.published.all()[:5]

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		return truncatewords(item.body, 20)
