from rest.url.router import Controller
from rest.web.home import views


Controller.add('', views.HomePage, name='home_page')
Controller.add('/tabs', views.Tabs, name= 'tabs_page' )
Controller.add('/about', views.About, name= 'about_page' )