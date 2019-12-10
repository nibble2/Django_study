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


