from pyrogram import filters 
from config import * 
import random
from Kobo.plugins import *


def ccmd(commands, input):
  if isinstance(commands, str):
    commands = [commands]
  return any(input.startswith(("/", ".")) and input[1:] == command for command in commands)

def cmd(commands, text):
  lower_text = text.lower()
  text_split = lower_text.split()
  for cmd in commands:
    if cmd.lower() in text_split:
      return True
  return False


MSG = "HAI,\nAda yang bisa Kobo bantu?","Haii kaka imut :D","Kamu perlu bantuan Kobo?"
cinte = "Bacot nt","Apa manggil manggil cinte"," Berisik China","Sok asik lu kontol"
@bot.on_message(filters.command('kobo',''))
async def command_text(client,m):
  if len(m.command) == 1:
    if m.from_user.id == 1771565060:
      return await m.reply(random.choice(cinte))
    return await m.reply(random.choice(MSG))
  #cmd = m.command[1].lower()
  text = m.text
  if cmd in ['google']:
    await google.GOOGLE(client,m)
  
  #FUNGSI ADMINS
  elif cmd(['kick'],text):
    await admins.KICK(client,m)
  elif cmd(['mute','dmute'],text):
    await admins.MUTED(client,m)
  elif cmd(['unmute'],text):
    await admins.UNMUTED(client,m) 
  elif cmd(['ban'],text):
    await admins.BANNED(client,m)
  elif cmd(['unban'],text):
    await admins.UNBANNED(client,m)
  #BARD
  elif cmd(["apa","bagaimana","mengapa","kapan","dimana","siapa","berapa","apakah","bagaimanakah","mengapakah","kapanlah","dimanakah","siapakah","berapakah","arti","maksud","contoh","jawaban","carikan"],text):
    await bard.BARD(client,m)
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

  #FETCH
  if cmd(['fetch'],text):
    import subprocess
    fetch_output = subprocess.check_output("neofetch", shell=True, text=True)
    await m.reply("```\n" + fetch_output + "\n```")
 
  else:
    msg2 = "Ahh kobo tidak tau harus ngapain"," Seperti tidak ada perintah untuk Kobo","Auu ahh nyuruh yang bener 😠","Cih gada perintah"
    await m.reply(random.choice(msg2))