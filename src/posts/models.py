from django.db import models

# Create your models here.


def upload_location(instance, filename):
	return "%s/%s" %(instance.id, filename)


class Post(models.Model):
	title = models.CharField(max_length=120)
	height_field = models.IntegerField(default=0)
	width_field  = models.IntegerField(default=0)
	content = models.TextField()
	image = models.ImageField(upload_to="upload_location",
		null=True,
		blank=True,
		width_field="width_field",
		height_field="height_field")
	price = models.IntegerField()
	location = models.CharField(max_length=120)
	category = models.CharField(max_length=120)
	beds = models.IntegerField()
	bath = models.IntegerField()
	draft = models.BooleanField(default=0)
	publish = models.DateField(auto_now=False, auto_now_add=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title
