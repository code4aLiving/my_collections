from django.views.generic.edit import FormView
from django.views.generic import ListView
from my_collections.models import Collection
from my_collections.forms import CollectionForm
from django.shortcuts import render, redirect
from mycollections import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.utils.decorators import method_decorator

@method_decorator(login_required,name='get')
@method_decorator(login_required,name='post')
class CollectionCreate(FormView):
	form_class = CollectionForm
	success_url = "/"
	context_object_name = "collectionForm"
	template_name = "create_collection.html"

	def get(self,request):
		collectionForm = CollectionForm()
		return render(request,self.template_name,{'collectionForm':collectionForm})

	def post(self,request):
		collectionForm = CollectionForm(request.POST)
		if collectionForm.is_valid():
			collection = Collection.objects.create(user = request.user, name = collectionForm.cleaned_data['name'],
				description = collectionForm.cleaned_data['description'],
				isPrivate = collectionForm.cleaned_data['isPrivate'])
			return HttpResponseRedirect(self.success_url)
		else:
			return render(request,self.template_name,{'collectionForm':collectionForm})
