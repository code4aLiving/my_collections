from django.shortcuts import render, redirect
from mycollections import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.urlresolvers import reverse
from models import *
import logging
import pdb
import uuid

# Create your views here.
# this login required decorator is to not allow to any  
# view without authenticating
# @login_required(login_url="login/")
# def home(request):
# 	return render(request,"home.html")

def register(request, template_name, success_url='/'):
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('home'))
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		#form.username = request.POST['email']
		if form.is_valid():
			email = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = User.objects.create_user(username=email, email=email,password=password)
			user = authenticate(username=email,password=password)
			login(request, user)
			#return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
			return HttpResponseRedirect(reverse('home'))
		else:
			return render(request,template_name,{'form':form})
	else:
		form = UserCreationForm()
		return render(request, template_name, {'form': form})

def customLogin(request, template_name, authentication_form):
	if request.method == 'GET':
		if request.user.is_authenticated():
			return HttpResponseRedirect(reverse('home'))
		else:
			return render(request,template_name,{'authentication_form':authentication_form})
	else:
		return login(request)

def add_custom_fields(customFields, collection):
	collectionFields = get_collection_fields(collection)

	newFields = {}
	for k in customFields:
		if collectionFields.has_key(k):
			continue
		newFields[k] = customFields[k]
	#print newFields
	if len(newFields) == 0:
		return
	arr = []
	for k in newFields:
		arr.append(k)
		arr.append(newFields[k])

	if len(collection.itemCustomFields) > 0:
		collection.itemCustomFields += "," + ",".join(arr)
	else:
		collection.itemCustomFields += ",".join(arr)

	collection.save()

def get_collection_fields(collection):
	collectionFields = {}
	if len(collection.itemCustomFields.strip()) > 0:
		cfArr = collection.itemCustomFields.split(',')
 		for i in range(0,len(cfArr),2):
			collectionFields[cfArr[i]] = cfArr[i+1]
	return collectionFields

def field_type_value_to_field_type_name(fieldTypeValue):
	if fieldTypeValue == 1:
		return 'Number'
	elif fieldTypeValue == 2:
		return 'Date'
	else:
		return 'Text'
