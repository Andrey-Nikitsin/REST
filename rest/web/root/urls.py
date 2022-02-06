from contextlib import redirect_stderr
from rest.url.router import Controller




# Controller.add('', redirect(), 'root_url')
Controller.include('/home', 'rest.web.home.urls')