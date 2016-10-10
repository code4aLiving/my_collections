from django.views.generic.edit import FormView
from my_collections.models import Collection, CollectionItem
from my_collections.forms import CollectionForm, ItemForm
from django.shortcuts import render, redirect
from mycollections import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.utils.decorators import method_decorator

@method_decorator(login_required,name='get')
@method_decorator(login_required,name='post')
class CollectionItemCreate(FormView):
	form_class = ItemForm
	success_url = "/"
	context_object_name = "itemForm"
	template_name = "create_item.html"

	def get(self, request, collectionId):
		collection = Collection.objects.get(id=int(collectionId))
		collectionItemForm = ItemForm()
		return render(request, self.template_name, {'collectionItemForm':collectionItemForm, 'collection':collection})

	def post(self,request, collectionId):
		collection = Collection.objects.get(id=int(collectionId))
		collectionItemForm = ItemForm(request.POST)
		print collectionItemForm.is_valid()
		if collectionItemForm.is_valid():
			print 'valid'
			collectionItem = CollectionItem.objects.create(name = collectionItemForm.cleaned_data['name'],
				description = collectionItemForm.cleaned_data['description'],
				price = collectionItemForm.cleaned_data['price'])
			collectionItem.save()
			collection.collectionItems.add(collectionItem)
			collection.save()
			return HttpResponseRedirect(self.success_url)
		else:
			return render(request,self.template_name,{'collection':collection,'collectionItemForm':collectionItemForm})
