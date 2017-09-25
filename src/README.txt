2:25:58

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

