from rest.url.router import Controller
from rest.web.about import views


Controller.add('', views.About, name='about_page')
