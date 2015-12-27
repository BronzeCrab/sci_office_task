"""realto_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url


urlpatterns = [
    url(r'^$', 'guest_book.views.index', name='index'),
    url(r'^/(?P<sorting>\w+?)/$', 'guest_book.views.index', name='index'),
    url(r'^delentries', 'guest_book.views.dell_all_entries', name='delentry'),
    url(r'^sort$', 'guest_book.views.sort', name='sort'),
]
