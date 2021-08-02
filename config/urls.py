"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.contrib.sitemaps.views import sitemap
from config.sitemaps import StaticViewSitemap, BlogSitemap

sitemaps = {
    "static": StaticViewSitemap,
    "blog": BlogSitemap,
}


urlpatterns = [
    path('nl/', include('_no_lecture.urls')), # こちらはレクチャーには含まれないので追加する必要はありません
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', include('mysite.urls')),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
        name="django.contrib.sitemaps.views.sitemap")
]





