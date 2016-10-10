from django.views.generic.edit import FormView
from django.views.generic import ListView
from my_collections.models import Collection, CollectionItem
from my_collections.forms import CollectionForm, ItemForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from mycollections import settings

class CollectionItemEdit(FormView):
	form_class = ItemForm
	success_url = "/"
	context_object_name = "collectionItem"
	template_name = "edit_item.html"

	def get(self, request, collectionId, itemId):
		collection = Collection.objects.get(id=int(collectionId))
		collectionItem = CollectionItem.objects.get(id=int(itemId))
		collectionItemForm = ItemForm(instance=collectionItem)
		return render(request, self.template_name, {'collection':collection, 'collectionItemForm':collectionItemForm, 
			'collectionItem':collectionItem,'itemId':itemId})

	def post(self,request,collectionId, itemId):
		success_url = '/collections/' + str(collectionId)
		collectionItemForm = ItemForm(request.POST)
		collectionItem = CollectionItem.objects.get(id=int(itemId))
		if collectionItemForm.is_valid():
			collectionItemForm = ItemForm(request.POST, instance = collectionItem)
			collectionItemForm.save()
			return HttpResponseRedirect(success_url)
		else:
			return redirect('edit_item',collectionId,itemId)