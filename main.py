from flask import Flask 
from threading import Thread 
import asyncio
import traceback
import random
import os 


flask_app = Flask(__name__) 

@flask_app.route('/')
def flask_msg():
  return "KOBO CUTE RUN"


def run_flask():
  flask_app.run(host="0.0.0.0", port=random.randint(5000, 9999))


def run_thread():
  Thread(target=run_flask).start() 


async def run_all():
  #os.system("pip install -r requirements.txt")
  #os.system("clear")
  import Kobo
  from Kobo.plugins.restart import restarting
  from pyrogram import idle 
  import config
  await config.bot.start()
  run_thread()
  await restarting()
  await idle()
  await config.bot.stop()

loop = asyncio.get_event_loop()
if __name__ == "__main__":
  try:
    loop.run_until_complete(run_all()) 
  except KeyboardInterrupt:
    pass
  except Exception:
    err = traceback.format_exc()
    print(err)
  finally:
    loop.stop()