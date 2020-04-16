from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
# from .models import Post 
from .forms import PostForms

def home(request):
	return render(request, "home.html")


def post(request):
	form = PostForms(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully Created")
		# return HttpResponseRedirect(instance.get_obsolute_url())
	content = {
		"form": form
	}

	return render (request, "post.html", content)

def show(request):
	return render(request, "show.html")

def update(request):
	return render(request, "update_post.html")


def property_view(request):
	return render(request, "properies.html")

def about(request):
	return render(request, "about.html")
	