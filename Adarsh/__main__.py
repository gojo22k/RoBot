# (c) adarsh-goel
import os
import sys
import glob
import asyncio
import logging
import importlib
from pathlib import Path
from pyrogram import idle
from .bot import StreamBot
from .vars import Var
from aiohttp import web
from .server import web_server
from .utils.keepalive import ping_server
from Adarsh.bot.clients import initialize_clients
from pyrogram import Client

app = Client("my_bot")

async def main():
    async with app:
        await app.start()

        # Perform time synchronization
        await app.sync_clock()
        
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("aiohttp").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("aiohttp.web").setLevel(logging.ERROR)

ppath = "Adarsh/bot/plugins/*.py"
files = glob.glob(ppath)
StreamBot.start()
loop = asyncio.get_event_loop()


async def start_services():
    try:
        print('\n')
        print('------------------- Initalizing Telegram Bot -------------------')
        bot_info = await StreamBot.get_me()
        StreamBot.username = bot_info.username
        print("------------------------------ DONE ------------------------------")
        print()
        print("---------------------- Initializing Clients ----------------------")
        await initialize_clients()
        print("------------------------------ DONE ------------------------------")
        print('\n')
        print('--------------------------- Importing ---------------------------')
        for name in files:
            with open(name) as a:
                patt = Path(a.name)
                plugin_name = patt.stem.replace(".py", "")
                plugins_dir = Path(f"Adarsh/bot/plugins/{plugin_name}.py")
                import_path = ".plugins.{}".format(plugin_name)
                spec = importlib.util.spec_from_file_location(import_path, plugins_dir)
                load = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(load)
                sys.modules["Adarsh.bot.plugins." + plugin_name] = load
                print("Imported => " + plugin_name)
        if Var.ON_HEROKU:
            print("------------------ Starting Keep Alive Service ------------------")
            print()
            asyncio.create_task(ping_server())
        print('-------------------- Initializing Web Server ---------------------')
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0" if Var.ON_HEROKU else Var.BIND_ADRESS
        await web.TCPSite(app, bind_address, Var.PORT).start()
        print('----------------------------- DONE --------------------------------')
        print('\n')
        print('------------------------------------------------------------------')
        print('------------------------------------------------------------------')
        print(' follow me for more such exciting bots! https://github.com/adarsh-goel')
        print('------------------------------------------------------------------')
        print('\n')
        print('----------------------- Service Started --------------------------')
        print('                        bot =>> {}'.format((await StreamBot.get_me()).first_name))
        print('                        server ip =>> {}:{}'.format(bind_address, Var.PORT))
        print('                        Owner =>> {}'.format((Var.OWNER_USERNAME)))
        if Var.ON_HEROKU:
            print('                        app running on =>> {}'.format(Var.FQDN))
        print('------------------------------------------------------------------')
        print('')
        print('------------------------------------------------------------------')
        await idle()

    except Exception as e:
        if "[400 CHAT_ADMIN_REQUIRED]" in str(e):
            logging.error("Bot lacks admin rights in the channel. Please check permissions.")
            # You can inform the user about the issue here
        else:
            logging.error(f"An error occurred: {e}")
            # Handle other exceptions as needed

if __name__ == '__main__':
    try:
        loop.run_until_complete(start_services())
    except KeyboardInterrupt:
        logging.info('----------------------- Service Stopped -----------------------')
