"""mycollections URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.contrib.auth import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from my_collections.forms import LoginForm, RegistrationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from my_collections.views import *

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('my_collections.urls')),
    url(r'^[accounts/]?login/$', customLogin, {'template_name': 'registration/login.html', 'authentication_form': LoginForm}),
    url(r'^register/$', register, {'template_name': 'registration/register.html'}, name='register'),
    url(r'^accounts/logout/$', views.logout, {'next_page': '/login'}),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
