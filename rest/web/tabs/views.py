from aiohttp import web
from aiohttp_jinja2 import template

class Tabs(web.View):

    @template('Tabs.html')
    async def get(request):
        return {'key' : request}