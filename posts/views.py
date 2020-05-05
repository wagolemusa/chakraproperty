from urllib.parse import quote_plus 
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import modelformset_factory
from django.shortcuts import render, get_object_or_404, redirect, Http404
from django.db.models import Q
from django.core.paginator import Paginator 
from django.utils import timezone

# Create your views here.
from .models import Post, Images 
from .forms import PostForms, ImageForm

def home(request):
	queryset_list = Post.objects.order_by("-timestamp")
	if request.user.is_staff or request.user.is_superuser:
		queryset_list = Post.objects.all()
	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
			Q(title__icontains=query) | 
			Q(content__icontains=query)|
			Q(price__icontains=query)|
			Q(location__icontains=query)
			).distinct()
	paginator = Paginator(queryset_list, 8)
	page = request.GET.get('page')
	querySet = paginator.get_page(page)

	content = {
		"object_list": querySet,
	}
	return render(request, "home.html", content)


def post(request):
	ImageFormSet = modelformset_factory(Images, form=ImageForm, extra=3)
	form = PostForms(request.POST or None, request.FILES or None)
	formset = ImageFormSet(request.POST or None, request.FILES or None,
													queryset=Images.objects.none())
	if form.is_valid() and formset.is_valid():
		instance = form.save(commit=False)
		instance.save()

		for fx in formset.cleaned_data:
			image = fx['image']
			photo = Images(post=instance, image=image)
			photo.save()
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_obsolute_url())
	else:
		messages.error(request, "Not Successfully Created")
		form = PostForms()
	content = {
		"form": form,
		"formset":formset
	}
	return render (request, "post.html", content)

def show(request, id=None):
	instance = get_object_or_404(Post, id=id)

	qureyset_list = Post.objects.order_by("-timestamp")
	if request.user.is_staff or request.user.is_superuser:
		qureyset_list = Post.objects.all()
	paginator = Paginator(qureyset_list, 4)
	page = request.GET.get('page')
	querySet = paginator.get_page(page)

	content = {
	"title":instance.title,
	'instance': instance,
	"object_list": querySet
	}

	return render(request, "show.html", content)

def update(request, id=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, id=id)
	form = PostForms(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#'>Updated </a>Successfully", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_obsolute_url())
	content = {
	"title": instance.title,
	"instance": instance,
	"form":form,
	}
	return render(request, "post.html", content)


def property_view(request):
	queryset_list = Post.objects.order_by("-timestamp")
	if request.user.is_staff or request.user.is_superuser:
		queryset_list = Post.objects.all()

	query = request.GET.get("q")
	if query:
		qureyset_list = qureyset_list.filter(
			Q(title__icontains=query) | 
			Q(content__icontains=query) 
			# Q(price__icontains=query)|
			# Q(location__icontains=query)
			).distinct()
	paginator = Paginator(queryset_list, 8)
	page = request.GET.get('page')
	querySet = paginator.get_page(page)

	content = {
		"object_list": querySet
	}
	return render(request, "properies.html", content)

def about(request):
	return render(request, "about.html")
	

def more(request):
	return render(request, "more.html")

def latest(request):
	qureyset_list = Post.objects.order_by("-timestamp")
	if request.user.is_staff or request.user.is_superuser:
		queryset_list = Post.objects.all()
	paginator = Paginator(queryset_list, 4)
	page = request.GET.get('page')
	querySet = paginator.get_page(page)
	content = {
		"object_list": querySet,
	}
	return render(request, "latest.html", content)

def post_delete(request, id=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request, "Successfully Deleted")
	return redirect("posts:home")