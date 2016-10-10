from my_collections.forms import UploadCsvFileForm
from my_collections.models import Collection, CollectionItem 
from django.views.generic.edit import FormView
import csv
from django.shortcuts import render, redirect

class CsvUpload(FormView):
	form_class = UploadCsvFileForm

	def post(self, request, collectionId):
		form = UploadCsvFileForm(request.POST, request.FILES)
		if form.is_valid():
			add_items_to_the_collection(request.FILES['file'], collectionId)
			return redirect('/')
		else:
			print form.errors
	
	def add_items_to_the_collection(csvfile, collectionId):
		print 'Importing'
		collection = Collection.objects.get(id=int(collectionId))
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			collectionItem = CollectionItem.objects.create(name = row[0],
				description = row[1], price = int(row[2]))
			collectionItem.save()
			collection.collectionItems.add(collectionItem)
		collection.save()


