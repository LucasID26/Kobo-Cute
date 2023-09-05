from config import *
from pyrogram import filters
import subprocess
import sys
import os
import re 
import pickle

@bot.on_message(filters.command(['reboot','restart'],'') & filters.user(own))
async def RESTART(client,m):
  msg = await m.reply_text("__Restarting BOT__. . .")
  with open("restart.pickle", "wb") as status:
    pickle.dump([m.chat.id, msg.id], status)
  restart_program() 

async def restarting():
  if os.path.exists("restart.pickle"):
    with open('restart.pickle', 'rb') as status:
      chat_id, message_id = pickle.load(status)
      os.remove("restart.pickle")
      await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f"`Restarting berhasil✅`")

def restart_program():
  os.execv(sys.executable, ['python', 'main.py'])