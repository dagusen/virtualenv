3:09:54 Get Single Items from db
4:07:03 user

# create virtualenv
mkdir name_of_VirEnv && cd name_of_VirEnv
virtualenv -p python3 .

# activate virtual env
source bin/activate

#install django and start project
pip install django==1.11.3

#start project
mkdir src && cd src
django-admin.py startproject name_of_project

# create new settings
cd name_of_project
mkdir settings && cd settings

#creating __init__.py
echo "from .base import *

from .production import *

try:
   from .local import *
except:
   pass
" > __init__.py

#copy setting.py to dir settings then change base_dir to 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#create local settings (local.py) and make new (base.py & production.py) 

#some other common installations
pip install psycopg2
pip install gunicorn dj-database-url
pip install django-crispy-forms
pip install pillow
pip install django-mathfilters

# create requirements.txt 
pip freeze > requirements.txt

# run migration & create superuser
python manage.py migrate
python manage.py 


#shell

#import

from restaurant.models import RestaurantLocation

#adding data to models
obj = RestaurantLocation.objects.create(name='Chronic tacos', location='Corona Del Mar', category='Mexican')
obj
obj.timestamp

qs = RestaurantLocation.objects.all()
qs

qs =RestaurantLocation.objects.filter(category__iexact='mexican').exclude(name__icontains='Tacos')

qs = count()

#view all objects
RestaurantLocation.objects.all()
for obj in RestaurantLocation.objects.all():
	print(obj.name)

#create a new query set
qs =RestaurantLocation.objects.all()
qs.filter(category='Phillipines') or qs.filter(category__iexact='Phillipines')


#update field
qs.update(category='philippines')
qs.filter(category__iexact='philippines')


#query set 2
qs2 = RestaurantLocation.objects.filter(category__iexact='mexican')
qs2

#if it exists
qs.exists()


#count
qs2.count()


3:00:49 Get Single Items from db
from restaurant.models import RestaurantLocation
qs = RestaurantLocation
qs
qs.first, last, [1]
RestaurantLocation.objects.get(pk=1)
#404
from django.shortcuts import render, get_object_or_404
obj = get_object_or_404(RestaurantLocation, pk=12000)


#show user in shell
from django.contrib.auth import get_user_model
User = get_user_model
User.objects.al()
admin_user = User.objects.get(id=1)
admin_user
admin_user.username
admin_user.is_active
admin_user.is_staff
obj = admin_user
obj.restaurantlocation.all()
obj.restaurantlocation.filter(contain__iexact='mexican')

#filter all post
from restaurant.models import RestaurantLocation
RestaurantLocation.objects.filter(user__id=1)
RestaurantLocation.objects.filter(user__iexact='admin')

new_qs = cfe_user.restaurantlocation_set.all()
new_obj = new_qs.first()
new_obj
RK = new_obj.__class__
RK.objects.all()