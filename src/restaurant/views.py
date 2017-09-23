# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
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

def home(request):
	num = None
	some_list = [
		random.randint(0, 1000000),
		random.randint(0, 1000000),
		random.randint(0, 1000000),
	]
	condition_bool_item = True
	if condition_bool_item:
		num = random.randint(0, 1000000)
	context = {
		"num" : num,
		"some_list": some_list
	}
	return render(request,"home.html", context)#response

def about(request):
	context = {
	}
	return render(request,"about.html", context)#response

def contact(request):
	context = {
	}
	return render(request,"contact.html", context)#response
