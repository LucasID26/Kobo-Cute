from config import * 
from flask import Flask 
from threading import Thread 
from pyrogram import idle
import asyncio
import traceback
import random

flask_app = Flask(__name__) 

@flask_app.route('/')
def flask_msg():
  return "KOBO CUTE RUN"


def run_flask():
  flask_app.run(host="0.0.0.0", port=random.randint(5000, 9999))


def run_thread():
  Thread(target=run_flask).start() 

async def run_all():
  import Kobo 
  os.system("pip3 install -r requirements.txt")
  os.system("clear")
  await bot.start()
  run_thread()
  await idle()
  await bot.stop()

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
    