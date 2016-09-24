
from django.views.generic import ListView
from my_collections.models import Collection

class CollectionList(ListView):
	model = Collection
	template_name = 'collection_list.html'
	context_object_name = 'collections'