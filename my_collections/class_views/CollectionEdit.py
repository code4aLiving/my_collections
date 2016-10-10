from django.views.generic.edit import FormView
from django.views.generic import ListView
from my_collections.models import Collection
from my_collections.forms import CollectionForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from mycollections import settings

@method_decorator(login_required,name='get')
@method_decorator(login_required,name='post')
class CollectionEdit(FormView):
	form_class = CollectionForm
	success_url = "collections/edit/{0}"
	context_object_name = "collection"
	template_name = "edit_collection.html"

	def get(self, request, id):
		print 'Gettt',id
		collection = Collection.objects.get(id=int(id))
		collectionForm = CollectionForm(instance=collection)
		print collectionForm
		return render(request, self.template_name, {'collectionForm':collectionForm})

	def post(self, request, id):
		collection = Collection.objects.get(id=int(id))
		collectionForm = CollectionForm(request.POST)
		if collectionForm.is_valid():
			collectionForm = CollectionForm(request.POST, instance = collection)
			collectionForm.save()
			return HttpResponseRedirect(id)
		else:
			return redirect('edit_collection',id)