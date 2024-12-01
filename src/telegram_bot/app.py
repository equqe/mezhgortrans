import asyncio

import aiohttp
import aiohttp_cors
from aiogram import executor
from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response

import aiohttp_jinja2
import jinja2

from pathlib import Path

here = Path(__file__).resolve().parent

import filters
import handlers
import middlewares  # Нужно
from data.config import (
    MAILING_WEBHOOK_PATH,
    ORDER_REVISION_NOTIFY_WEBHOOK_PATH,
    UPDATE_DRIVER_LOCATION_PERIOD,
    WEBAPP_HOST,
    WEBAPP_PORT,
    WEBHOOK_PATH,
    WEBHOOK_URL,
)
from data.texts import DRIVERS_HAD_FOUNDED
from keyboards.inline.order import (
    create_order_revision_keyboard,
    revision_order_keyboard,
)
from loader import bot, core, dp
from models.referral import Mailing
from utils.mailing import message_to_user_list
from utils.misc.logging import logger
from utils.notify_admins import on_startup_notify
from utils.stop_session import stop_session
from utils.tasks.update_driver_locations import update_user_locations

app = web.Application()
routes = web.RouteTableDef()

print(f"{MAILING_WEBHOOK_PATH=}")


@routes.post(MAILING_WEBHOOK_PATH)
async def mailing_webhook(request: Request):
    """
    Принимает запрос на рассылку и начинает рассылку
    """
    payload = await request.json()
    mailing = Mailing.parse_obj(payload)
    logger.info(f"Новая рассылка: {mailing}")

    await message_to_user_list(
        user_list=mailing.telegram_ids,
        text=mailing.message.text,
        photo=mailing.message.photo_url,
        video=mailing.message.video_url,
        url=mailing.message.url,
        url_button_name=mailing.message.url_button_name,
        **mailing.message.get_message_kwargs(),
    )
    logger.info("Рассылка завершена!")
    return Response(status=200, text="ok")


print(f"{ORDER_REVISION_NOTIFY_WEBHOOK_PATH=}")


@routes.post(ORDER_REVISION_NOTIFY_WEBHOOK_PATH)
async def order_revision_check_handler(request: Request):
    """
    Принимает заказы, в которых нашлись водители спустя время
    """
    payload = await request.json()
    success = payload["success"]
    failed = payload["failed"]

    for revision in success:
        chat_id = revision.get("chat_id")
        order_id = revision.get("order_id")
        await bot.send_message(
            chat_id,
            DRIVERS_HAD_FOUNDED,
            reply_markup=await revision_order_keyboard(order_id),
        )

    for revision in failed:
        chat_id = revision.get("chat_id")
        order_id = revision.get("order_id")
        await bot.send_message(
            chat_id,
            "К сожалению, я не смог найти водителей. Администрация уведомлена об этой проблеме и будет нанимать больше водителей. Нажмите на кнопку ниже, чтобы снова включить поиск.",
            reply_markup=await create_order_revision_keyboard(order_id=order_id),
        )

    return Response(status=200, text="ok")




async def temp(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            return await r.json()

@routes.get('/nomination/search')
async def nomination(request):
    response = await temp("http://5.188.158.24/search?" + request.query_string)
    return web.json_response(response)


@routes.get('/nomination/reverse')
async def nomination(request):
    response = await temp("http://5.188.158.24/reverse?" + request.query_string)
    return web.json_response(response)


async def update_user_locations_task():
    while True:
        try:
            await update_user_locations()
        except Exception as E:
            logger.warning(f"Не удалось обновить геопозицию водителей {E.args}")
        await asyncio.sleep(UPDATE_DRIVER_LOCATION_PERIOD)


async def on_startup(dispatcher):
    # Уведомляет про запуск
    print("Start set webhook")
    await bot.set_webhook(WEBHOOK_URL)
    print("End set webhook")
    await core.start_session()
    await on_startup_notify(dispatcher)
    loop = asyncio.get_running_loop()
    loop.create_task(update_user_locations_task())


async def on_shutdown(dispatcher):
    """
            Активирутеся при выключении
    :param dispatcher:
    :return:
    """
    await stop_session()
    await bot.delete_webhook()
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


@routes.get('/')
async def nomination(request):

    response = await temp("http://5.188.158.24/reverse?" + request.query_string)
    return web.json_response(response)




def html_response(document):
    s = open(document, "r")
    return web.Response(text=s.read(), content_type='text/html')

@routes.get('/map')
async def index_handler(request):
    return html_response('static/index.html')

#?telegram_auth_token=5b732bbe88eff976f8b71dce5ef869d12403175f



# Чтобы не ругался
__noinspection_pycharm__ = (filters, handlers, middlewares)
if __name__ == "__main__":

    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str(here)))
    app.router.add_get('/', index_handler)

    app.router.add_static('/static/', path='static', name='static')


    app.add_routes(routes)
    

    cors = aiohttp_cors.setup(app, defaults={
    "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*"
        )
    })

    for route in list(app.router.routes()):
        cors.add(route)


    # executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=True)
    print(f"{WEBHOOK_PATH=}")
    e = executor.set_webhook(
        dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        web_app=app,
    )

    print(f"start app: {WEBAPP_HOST}:{WEBAPP_PORT}")
    
    e.run_app(host=WEBAPP_HOST, port=WEBAPP_PORT)
