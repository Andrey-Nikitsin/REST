from aiohttp import web
from rest.conf import setup
from rest.app.server import createApp, a_create_app


def run():
    app = createApp()
    web.run_app(app, host= "127.0.0.1", port= 8001 )
