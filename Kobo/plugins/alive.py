from pyrogram import filters,__version__
from config import * 
import time 
from datetime import datetime
import requests
import os
import platform
import psutil

from Kobo.decorators.decorator import info_cmd



TIME_DURATION_UNITS = ( ('minggu', 60 * 60 * 24 * 7), ('hari', 60 * 60 * 24), ('jam', 60 * 60), ('menit', 60), ('detik', 1))
def duration(seconds):
  if seconds == 0:
    return 'Baru aja off'
  parts = []
  for unit, div in TIME_DURATION_UNITS:
    amount, seconds = divmod(int(seconds), div)
    if amount > 0:
      parts.append('{} {}{}' .format(amount, unit, "" if amount == 1 else ""))
  return ', '.join(parts) 



starttime = datetime.utcnow()


@info_cmd
async def PING(client, m):
  uptime = duration((datetime.utcnow() - starttime).total_seconds())
  start = time.time() 
  msg = await m.reply(text="**0% ▒▒▒▒▒▒▒▒▒▒**")
  end = time.time()
  durasi = (end - start) * 1000
  p_result = f"{durasi:.2f} ms"
  #await msg.edit("**20% ██▒▒▒▒▒▒▒▒**")
  #await msg.edit("**40% ████▒▒▒▒▒▒**")
  await msg.edit("**60% ██████▒▒▒▒**")
  #await msg.edit("**80% ████████▒▒**")
  await msg.edit("**100% ██████████**")
  #owner = (await bot.get_users(own[1])).mention
  await msg.edit(f"""
❏ **PONG!!🏓**
├• **Pinger** ➥ `{p_result}`
├• **Server** ➥ `{ping_server()}` 
├• **Uptime** ➥ `{uptime}` 
└• **OWNER**  ➥ @PanggilYoi
<a href='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTz5q_KcP8RQbDQPciRoBSlwKMyBHAKMNN-pg&amp;usqp=CAU'>⁠</a>
""")

def ping_server():
  url = "https://yoi-asisstant.kulukgalak.repl.co/"
  start = time.time()
  response = requests.get(url, timeout=5) 
  end = time.time()
  ping = (end - start) * 1000
  result = f"{ping:.2f} ms"
  return result





@info_cmd
async def SYSTEM(client,m):
  await m.reply(cek_system())

def cek_system():
  try:
    #PLATFORM
    system = platform.uname()
    sistem = system.system
    versi = system.version
    mesin = system.machine
    p_implementasi = platform.python_implementation()
    bit = platform.architecture()
    python_v = platform.python_version()
    uptime = duration((datetime.utcnow() - starttime).total_seconds())
   
    #DISK
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    msg = f"""
❏ **SYSTEM ⚙**
├• **System** ➥ `{sistem}`
├• **Version** ➥ `{versi.split("#",1)[1].split("Sun",1)[0]}`
├• **Machine** ➥ `{mesin}`
├• **Py_Implemenation** ➥ `{p_implementasi}`
├• **BIT** ➥ `{bit[0]}`|`{bit[1]}`
├• **Python Version** ➥ `{python_v}`
├• **Pyro** ➥ `{__version__}`
└• **Uptime** ➥ `{uptime}`

❏ **DISK 💾**
├• **CPU** ➥ `{cpu}%`
├• **RAM** ➥ `{mem}%`
└• **DISK** ➥ `{disk}%`
"""
    return msg
  except Exception as e:
    return f"Terjadi kesalahan dalam mengumpulkan data system\n**EROR**: `{e}`"


