from django.conf.urls import url
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.get_collections, name='home'),
    url(r'^collections$', views.get_collections, name='collections'),
    url(r'^collections/create$', views.create_collection, {'template_name':'create_collection.html', 
    	'success_url':'/'}, name='create_collection'),
    url(r'^collections/edit/(?P<id>[0-9]+)$', views.edit_collection, {'template_name':'edit_collection.html', 
    	'success_url':'/'}, name='edit_collection'),
    url(r'collections/(?P<id>[0-9]+)/add_item$', views.add_collection_item, {'template_name':'add_item.html',
    	'success_url':'/'}, name='add_item'),
    url(r'collections/(?P<id>[0-9]+)$', views.list_collection_items, {'template_name':'list_collection_items.html'},
    	name='list_collection_items'),
    url(r'^collections/(?P<collectionId>[0-9]+)/edit_item/(?P<itemId>[0-9]+)$', views.edit_item, 
    	{'template_name':'add_item.html', 'success_url':'/'},name='edit_item')
]