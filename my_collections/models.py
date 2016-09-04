from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.
class Tag(models.Model):
	name = models.CharField(max_length=50)
	colour = models.IntegerField(default=0)

class CollectionItem(models.Model):
	name = models.CharField(max_length=500)
	description = models.TextField(blank=True)
	price = models.FloatField(default=0)
	identifier = models.CharField(max_length=500)

class Collection(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=500)
	description = models.TextField(blank=True)
	isPrivate = models.BooleanField()
	itemCustomFields = models.TextField(blank=True)
	tags = models.ManyToManyField(Tag)
	collectionItems = models.ManyToManyField(CollectionItem)





