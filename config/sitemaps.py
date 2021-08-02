
from django.contrib import sitemaps
from django.urls import reverse
from blog.models import Article

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ["mysite:home", "mysite:bs-home", ]
    
    def location(self, item):
        return reverse(item)

class BlogSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Article.objects.all()

    def lastmod(self, obj):
        return obj.created_at
    
    def location(self, obj):
        return reverse("blog:article", kwargs={'pk': obj.id})