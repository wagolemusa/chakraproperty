from django import forms

from .models import Post

class PostForms(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={
		'class': 'form-control'
		})) 
	price = forms.IntegerField(widget=forms.NumberInput(attrs={
		'class': 'form-control'
		}))
	location = forms.CharField(widget=forms.TextInput(attrs={
		'class': 'form-control'
		}))
	category = forms.CharField(widget=forms.TextInput(attrs={
		'class': 'form-control'
		}))
	beds = forms.IntegerField(widget=forms.NumberInput(attrs={
		'class': 'form-control'
		}))
	bath = forms.IntegerField(widget=forms.NumberInput(attrs={
		'class': 'form-control'
		}))
	content = forms.CharField(widget=forms.Textarea(attrs={
		'class': 'form-control'
		}))
	publish = forms.DateField(widget=forms.SelectDateWidget)

	class Meta:
		model = Post
		fields = [
			"title",
			"price",
			"location",
			"category",
			"beds",
			"bath",
			"content",
			"image",
			"draft",
			"publish",
		]
