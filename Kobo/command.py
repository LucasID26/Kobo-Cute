from pyrogram import filters 
from config import bot
import random
from Kobo.plugins import *


def ccmd(commands, input):
  if isinstance(commands, str):
    commands = [commands]
  return any(input.startswith(("/", ".")) and input[1:] == command for command in commands)

def cmddd(commands, text):
  lower_text = text.lower()
  text_split = lower_text.split()
  for cmd in commands:
    if cmd.lower() in text_split:
      return True
  return False

def cmd(commands, text):
  lower_text = text.lower()
  text_split = lower_text.split()   
  for cmd in commands:
    cmd_words = cmd.lower().split()
    if all(word in text_split for word in cmd_words):
      return True
            
  return False


MSG = "HAI,\nAda yang bisa Kobo bantu?","Haii kaka imut :D","Kamu perlu bantuan Kobo?"
@bot.on_message(filters.command('kobo',''))
async def command_text(client,m):
  if len(m.command) == 1:
    return await m.reply(random.choice(MSG))
  text = m.text
  
  #FUNGSI ADMINS
  if cmd(['kick'],text):
    await admins.KICK(client,m)
  elif cmd(['mute','dmute'],text):
    await admins.MUTED(client,m)
  elif cmd(['unmute'],text):
    await admins.UNMUTED(client,m) 
  elif cmd(['ban'],text):
    await admins.BANNED(client,m)
  elif cmd(['unban'],text):
    await admins.UNBANNED(client,m)
  #FAKTA
  elif cmd(['fakta menyenangkan','fun fact'],text): 
    await fakta.FAKTA(client,m)
  #SSH_STORES
  elif cmd(['ssh ws','sshstores','ssh websocket','websocket'],text):
    await ssh.STORES(client,m)
  #AFK
  elif cmd(['afk'],text):
    await afk.AFK(client,m)
  #CEK BOTS AND STAFF 
  elif cmd(['staff','admins'],text):
    await cek_bots_staff.STAFF(client,m) 
  elif cmd(['bots'],text):
    await cek_bots_staff.BOTS(client,m) 
  #ALIVE
  elif cmd(['ping'],text):
    await alive.PING(client,m)
  elif cmd(['system'],text):
    await alive.SYSTEM(client,m)
  #DOWNLOAD
  elif cmd(['download','tolong download','dl'],text):
    await download.DOWNLOAD(client,m)
  else:
    await bard.AI(client,m)