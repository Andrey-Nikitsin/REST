from aiohttp import web
from aiohttp_jinja2 import template, render_template


class HomePage(web.View):

    @template('home.html')
    async def get(self):
        return {}

class Tabs(web.View):

    @template('Tabs.html')
    async def get(request):
        return {'key' : request}

class About(web.View):

    @template('about.html')
    async def get(self):
        return

