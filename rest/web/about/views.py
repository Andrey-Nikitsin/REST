from aiohttp import web
from aiohttp_jinja2 import template

class About(web.View):

    @template('about.html')
    async def get(self):
        return