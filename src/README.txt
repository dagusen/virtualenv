template inheretance 1:20:44

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
python manage.py createsuperuser