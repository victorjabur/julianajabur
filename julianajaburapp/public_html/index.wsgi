import os, sys, site
site.addsitedir('/home/storage/c/6e/e5/julianajabur/.python/lib')
import django.core.handlers.wsgi
sys.path.append('/home/storage/c/6e/e5/julianajabur/wsgi_apps/julianajabur')
sys.path.append('C:/Users/Victor/pythonProjects/wsgi_apps/julianajabur')
sys.path.append('/home/victor/app/pythonProjects/wsgi_apps/julianajabur')
os.environ['DJANGO_SETTINGS_MODULE']='settings'
application = django.core.handlers.wsgi.WSGIHandler()
