# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#import random
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView
from .models import RestaurantLocation
# Create your views here.

def restaurant_listview(request):
	template_name = 'restaurant/restaurant-list.html'
	ResLoc = RestaurantLocation.objects.all()
	context = {
		"object_list" : ResLoc
	}
	return render(request, template_name, context)

class RestaurantListView(ListView):
	ResList = RestaurantLocation.objects.all()
	



























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