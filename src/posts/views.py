from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, "home.html")


def post(request):

	return render (request, "post.html")

def show(request):
	return render(request, "show.html")

def update(request):
	return render(request, "update_post.html")


def property_view(request):
	return render(request, "properies.html")

def about(request):
	return render(request, "about.html")
	