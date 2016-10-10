from django.views.generic.edit import FormView
from django.views.generic import ListView
from my_collections.models import Collection, CollectionItem
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from mycollections import settings

@method_decorator(login_required,name='get')
class CollectionItemList(ListView):
	model = CollectionItem
	template_name = 'list_collection_items.html'
	context_object_name = 'collectionItems'

	def get(self, request, id):
		collection = Collection.objects.get(id=int(id))
		collectionItems = list(collection.collectionItems.all())
		return render(request, self.template_name,{'collection':collection, "collectionItems":collectionItems})