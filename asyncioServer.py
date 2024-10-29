import asyncio
from aiohttp import web

async def handle_index(request):
    return web.FileResponse('index.html')

async def handle_sleep(request):
    await asyncio.sleep(10)
    return web.FileResponse('sleep.html')

app = web.Application()
app.add_routes([
    web.get('/', handle_index),
    web.get('/index', handle_index),
    web.get('/sleep', handle_sleep)
])

if __name__ == '__main__':
    web.run_app(app, port=8000)
