"""firstdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin

from inventory import views as inventory_views
from bookstore import views as bookstore_views

urlpatterns = [
    url(r'^$',inventory_views.index,name='index'),
    url(r'^bookstore/', bookstore_views.index, name='bookstore'),
    url(r'^newbook$', bookstore_views.book_add, name='book_add'),
    url(r'^editbook/(?P<id>\d+)$', bookstore_views.book_edit, name='book_edit'),
    url(r'^deletebook/(?P<id>\d+)$', bookstore_views.book_delete, name='book_delete'),
    url(r'^book/(?P<id>\d+)/', bookstore_views.book_detail, name='book_detail'),
    url(r'^item/(?P<id>\d+)/',inventory_views.item_detail,name='item_detail'),
    url(r'^admin/', admin.site.urls),
]
