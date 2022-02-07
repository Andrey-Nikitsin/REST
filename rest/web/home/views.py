from aiohttp import web
from aiohttp_jinja2 import template, render_template


class HomePage(web.View):

    @template('home.html')
    async def get(self):
        return {}





