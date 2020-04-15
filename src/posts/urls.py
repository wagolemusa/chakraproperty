from django.urls import path
from django.conf.urls import url

from .views import (
	home,
	post,
	update,
	property_view,
	about,
	show,
)

app_name = 'posts'

urlpatterns = [
	path('', home, name='home'),
	path('create/', post),
	path('details/', show),
	path('about/', about),
	path('update/', update),
	path('all/', property_view),


]