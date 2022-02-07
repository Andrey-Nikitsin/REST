from os import path
from aiohttp import web
import asyncio
from rest.url.router import Controller
import aiohttp_jinja2
from jinja2 import FileSystemLoader
import pathlib


BASE_DIR = pathlib.Path(__file__).parent.parent.absolute()


def createApp():
    app = web.Application()
    Controller.entry_point('rest.web.root.urls')
    for route in Controller.urls():
        print(route)
        app.router.add_route("*", route.path, route.handler, name=route.name)
    app.router.add_static('/static', "static")
    aiohttp_jinja2.setup(
        app,
        default_helpers= True,
        loader= FileSystemLoader(
            [
                path / 'templates'
                for path in (BASE_DIR / "web").iterdir()
                if path.is_dir() and (path / "templates").exists()

            ]
        )
    )
    app['static_root_url'] = "/static"
    
    return app

async def a_create_app():
    return createApp(0)    