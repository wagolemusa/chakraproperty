from django.urls import path
from django.conf.urls import url

from .views import (
	home,
	post,
	update,
	property_view,
	about,
	show,
	more,
	latest,
	post_delete,

)

app_name = 'posts'

urlpatterns = [
	path('', home, name='home'),
	path('create/', post),
	path('<int:id>/', show, name="detail"),
	path('<int:id>/edit/', update, name='update'),
	path('about/', about, name="about"),
	path('all/', property_view, name="all"),
	path('<int:id>/delete/', post_delete),
	path('more/', more, name="more"),
	path('latest', latest, name='latest')



]