from rest.url.router import Controller





# Controller.add('', redirect(), 'root_url')
Controller.include('/home', 'rest.web.home.urls')
Controller.include('/tabs', 'rest.web.tabs.urls')
Controller.include('/about', 'rest.web.about.urls')

