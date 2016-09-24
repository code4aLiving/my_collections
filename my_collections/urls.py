from django.conf.urls import url
from . import views
from class_views.CollectionList import *
from class_views.CollectionEdit import *
from class_views.CollectionCreate import *
from class_views.CollectionItemList import *
from class_views.CollectionItemCreate import *
from class_views.CollectionItemEdit import *

# We are adding a URL called /home
urlpatterns = [
    
    url(r'^collections$', login_required(CollectionList.as_view()), name='collections'),
    
    url(r'^$', login_required(CollectionList.as_view()), name='home'),
    
    url(r'^collections/create$', login_required(CollectionCreate.as_view()), name='create_collection'),
    
    url(r'^collections/edit/(?P<id>[0-9]+)$', login_required(CollectionEdit.as_view()), name='edit_collection'),

    url(r'^collections/(?P<collectionId>[0-9]+)/create_item$', login_required(CollectionItemCreate.as_view()), name='create_item'),
    
    url(r'^collections/(?P<id>[0-9]+)$', login_required(CollectionItemList.as_view()), name='list_collection_items'),
    
    url(r'^collections/(?P<collectionId>[0-9]+)/edit_item/(?P<itemId>[0-9]+)$', login_required(CollectionItemEdit.as_view()),
     name='edit_item'),
]