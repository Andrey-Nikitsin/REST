from rest.url.router import Controller
from rest.web.tabs import views


Controller.add('', views.Tabs, name='tabs_page')
