# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#signals
from django.db.models.signals import pre_save, post_save
#slug generator
from .utils import unique_slug_generator

#validators
from .validators import validate_category


#for user
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.

class RestaurantLocation(models.Model):
	user 			= models.ForeignKey(User)# class_instance.model_set.all() # Django Models Unleashed JOINCFE.com
	name			= models.CharField(max_length=120)
	location		= models.CharField(max_length=120, null=True, blank=True)
	category		= models.CharField(max_length=120, null=True, blank=True, validators=[validate_category])
	timestamp		= models.DateTimeField(auto_now_add=True)
	updated			= models.DateTimeField(auto_now=True)
	slug			= models.SlugField(null=True, blank=True)
	#my_date_field	= models.DateTimeField(auto_now=False,auto_now_add=False)

	def __str__(self):
		return self.name

	def get_absolute_url(self): #get_absolute_url
		return "/restaurant/{self.slug}"

	@property
	def title(self):
		return self.name # obj.title

def rl_pre_save_receiver(sender, instance, *arg, **kwargs):
	instance.category = instance.category.capitalize()
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

# def rl_post_save_receiver(sender, instance, created, *arg, **kwargs):
# 	print('saved')
# 	print(instance.timestamp)
# 	if not instance.slug:
# 		instance.slug = unique_slug_generator(instance)
# 		instance.save()


pre_save.connect(rl_pre_save_receiver, sender=RestaurantLocation)
# post_save.connect(rl_post_save_receiver, sender=RestaurantLocation)