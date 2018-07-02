## J:creating urls.py according to Girls
## J:Girls: here we are importing Dijango function url and all of our views from the blog application

from django.conf.urls import url
from . import views

## J: There was a poblem with the character ^.
## J: there are other similar characteres that are not the same
urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
]
