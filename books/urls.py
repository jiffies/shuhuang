from django.conf.urls import patterns,url
from books import views

urlpatterns = patterns('',
			url(r'^s/?$',views.all_books,name='index'),
			url(r'^/(?P<book_id>\d+)/?$',views.detail,name='detail'),
		)
