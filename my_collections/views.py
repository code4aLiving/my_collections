from django.shortcuts import render, redirect
from mycollections import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.urlresolvers import reverse
from models import *
import pdb

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

@login_required(login_url="login/")
def get_collections(request):
	collections = list(Collection.objects.filter(user_id=request.user.id))
	return render(request, 'home.html', {'collections': collections})

@login_required(login_url="login/")
def create_collection(request, template_name, success_url):
	create = True
	if request.method == 'POST':
		collectionForm = CollectionForm(request.POST)
		if collectionForm.is_valid():
			collection = Collection.objects.create(user = request.user, name = collectionForm.cleaned_data['name'],
				description = collectionForm.cleaned_data['description'],
				isPrivate = collectionForm.cleaned_data['isPrivate'])
			#collection.save()
			return HttpResponseRedirect(success_url)
		else:
			pdb.set_trace()
			return render(request,template_name,{'collectionForm':collectionForm})
	else:
		collectionForm = CollectionForm()
		return render(request,template_name,{'collectionForm':collectionForm})

@login_required(login_url="login/")
def edit_collection(request, template_name, success_url, id):
	collection = Collection.objects.get(id=int(id))
	create = False
	if request.method == 'POST':
		collectionForm = CollectionForm(request.POST)
		#pdb.set_trace()
		if collectionForm.is_valid():
			collectionForm = CollectionForm(request.POST, instance = collection)
			collectionForm.save()
			#pdb.set_trace()
			return HttpResponseRedirect(success_url)
		else:
			#pdb.set_trace()
			return redirect(edit_collection,id)
	else:
		collectionForm = CollectionForm(instance=collection)
		#pdb.set_trace()
		return render(request, template_name, {'collectionForm':collectionForm})

def list_collection_items(request, template_name, id):
	collection = Collection.objects.get(id=int(id))
	return render(request, template_name,{'collection':collection})

@login_required(login_url="login/")
def add_collection_item(request, template_name, success_url, id):
	collection = Collection.objects.get(id=int(id))
	if request.method == 'POST':
		pass
	else:
		return render(request, template_name, {'collection':collection})

@login_required(login_url="login/")
def delete(request):
	pass
	
	