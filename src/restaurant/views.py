# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#import random
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

#forms 
from .forms import (
	RestaurantLocationCreateForm,
	# RestaurantCreateForm, for sample wrong way in creating a form
	)
#models
from .models import RestaurantLocation

# Create your views here.

#forms

class RestaurantCreateView(CreateView):
	form_class = RestaurantLocationCreateForm
	template_name = 'restaurant/form/html'

def restaurant_createview(request):
	form = RestaurantLocationCreateForm(request.POST or None)
	errors = None
	if form.is_valid():
		form.save()
		return HttpResponseRedirect("/restaurant/")
	if form.errors:
		print(form.errors)
		errors = form.errors
	template_name = 'restaurant/form.html'
	context = {
		"form" : form,
		"errors" : errors,
	}
	return render(request, template_name, context)


class RestaurantListView(ListView):
	def get_queryset(self):
		print(self.kwargs)
		slug = self.kwargs.get("slug")
		if slug:
			queryset = RestaurantLocation.objects.filter(
					Q(category__iexact=slug) |
					Q(category__icontains=slug)
				)
		else:
			queryset = RestaurantLocation.objects.all()
		return queryset

class RestaurantDetailView(DetailView):
	queryset = RestaurantLocation.objects.all()

	# def get_context_data(self, *args, **kwargs):
	# 	print(self.kwargs)
	# 	context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)
	# 	print(context)
	# 	return context

	# def get_object(self, *args, **kwargs):
	# 	res_id = self.kwargs.get('res_id')
	# 	obj = get_object_or_404(RestaurantLocation, id=res_id) # pk = rest_id
	# 	return obj

	



























#wrong way in creating a form

# def restaurant_createview(request):
# 	# if request.method == "GET":
# 	# 	print("get data")
# 	if request.method == "POST":
# 		# print("post data")
# 		# print(request.POST)
# 		title = request.POST.get("title") # request.POST["title"]
# 		location = request.POST.get("location")
# 		category = request.POST.get("category")
# 		obj = RestaurantLocation.objects.create(
# 				name = title,
# 				location = location,
# 				category = category,
# 			)
# 		return HttpResponseRedirect("/restaurant/")
# 	template_name = 'restaurant/form.html'
# 	context = {}
# 	return render(request, template_name, context)

# def restaurant_createview(request):
# 	form = RestaurantCreateForm(request.POST or None)
# 	errors = None
# 	if form.is_valid():
# 		obj = RestaurantLocation.objects.create(
# 				name = form.cleaned_data.get('name'),
# 				location = form.cleaned_data.get('location'),
# 				category = form.cleaned_data.get('category'),
# 			)
# 		return HttpResponseRedirect("/restaurant/")
# 	if form.errors:
# 		print(form.errors)
# 		errors = form.errors
# 	template_name = 'restaurant/form.html'
# 	context = {
# 		"form" : form,
# 		"errors" : errors,
# 	}
# 	return render(request, template_name, context)



# def restaurant_listview(request):
# 	template_name = 'restaurant/restaurant-list.html'
# 	ResLoc = RestaurantLocation.objects.all()
# 	context = {
# 		"object_list" : ResLoc
# 	}
# 	return render(request, template_name, context)




# class SearchRestaurantListView(ListView):
# 	template_name = 'restaurant/restaurant-list.html'

# 	def get_queryset(self):
# 		print(self.kwargs)
# 		slug = self.kwargs.get("slug")
# 		if slug:
# 			queryset = RestaurantLocation.objects.filter(
# 					Q(category__iexact=slug) |
# 					Q(category__icontains=slug)
# 				)
# 		else:
# 			queryset = RestaurantLocation.objects.none()
# 		return queryset
# class SearchRestaurantListView(ListView):
# 	template_name = 'restaurant/restaurant-list.html'

# 	def get_queryset(self):
# 		print(self.kwargs)
# 		slug = self.kwargs.get("slug")
# 		if slug:
# 			queryset = RestaurantLocation.objects.filter(
# 					Q(category__iexact=slug) |
# 					Q(category__icontains=slug)
# 				)
# 		else:
# 			queryset = RestaurantLocation.objects.none()
# 		return queryset






# class MexicanRestaurantListView(ListView):
# 	queryset = RestaurantLocation.objects.filter(category__iexact='mexican')
# 	template_name = 'restaurant/restaurant-list.html'

# class AsianFusionRestaurantListView(ListView):
# 	queryset = RestaurantLocation.objects.filter(category__iexact='asian fusion')
# 	template_name = 'restaurant/restaurant-list.html'






# class HomeView(TemplateView):
# 	template_name = 'home.html'

# 	def get_context_data(self, *args, **kwargs):
# 		context = super(HomeView, self).get_context_data(*args, **kwargs)
# 		num = None
# 		some_list = [
# 			random.randint(0, 1000000),
# 			random.randint(0, 1000000),
# 			random.randint(0, 1000000),
# 		]
# 		condition_bool_item = True
# 		if condition_bool_item:
# 			num = random.randint(0, 1000000)
# 		context = {
# 			"num" : num,
# 			"some_list": some_list
# 		}
# 		return context

# class AboutView(TemplateView):
# 	template_name = 'about.html'

# class ContactView(TemplateView):
# 	template_name = 'contact.html'

#function based view

# def home_old(request):
#  	#f strings
#  	html_var = 'Louis gwapo'
#  	html_ = f"""<!DOCTYPE html>
#  	<html lang=en>
#  	<head>
#  	</head>
#  	<body>
#  	<h1>Hello World!</h1>
#  	<p>This is {html_var} coming through</p>
#  	</body>
#  	</html>
#  	"""
#  	return HttpResponse(html_)

# def home(request):
# 	num = None
# 	some_list = [
# 		random.randint(0, 1000000),
# 		random.randint(0, 1000000),
# 		random.randint(0, 1000000),
# 	]
# 	condition_bool_item = True
# 	if condition_bool_item:
# 		num = random.randint(0, 1000000)
# 	context = {
# 		"num" : num,
# 		"some_list": some_list
# 	}
# 	return render(request,"home.html", context)#response

# def about(request):
# 	context = {
# 	}
# 	return render(request,"about.html", context)#response

# def contact(request):
# 	context = {
# 	}
# 	return render(request,"contact.html", context)#response

#class based view
# class ContactView(View):
# 	def get(self, request, *args, **kwargs):
# 		context = {}
# 		return render(request, "contact.html", context)