mk mysite

pip3 install virtualenv

virtualenv myenv

source activate

pip3 install django==2.1

django-admin startproject tutorialdjango .

python manage.py migrate

python manage.py runserver 0:80

python manage.py startapp main

tutorialdjango/settings.py 
 * INSTALLED_APPS = [ 'main' ]
 
tutorialdjango/urls.py
* from main.views import index
* path('', index)

make main/templates/main/index.html

python manage.py makemigrations
: db를 만들 수 있는 파일

python manage.py migrate
: 반영되게

admin.py
* from .models import Cafe
* admin.site.register(Cafe)

python manage.py createsuperuser

1234!


