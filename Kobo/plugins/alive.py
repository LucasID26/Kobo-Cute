from pyrogram import filters,__version__
from config import * 
import time 
from datetime import datetime
import requests
import os
import platform
import psutil
import shutil
from Kobo.tools import size
import cpuinfo
from Kobo.tools import duration
from Kobo.decorators.decorator import info_cmd







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
├• **Owner** ➥ [YOI](https://profile.kulukgalak.repl.co/)
└• **UPtime**  ➥ `{uptime}`
<a href='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTz5q_KcP8RQbDQPciRoBSlwKMyBHAKMNN-pg&amp;usqp=CAU'>⁠</a>
""")

def ping_server():
  url = "https://profile.kulukgalak.repl.co/"
  start = time.time()
  response = requests.get(url, timeout=5) 
  end = time.time()
  ping = (end - start) * 1000
  result = f"{ping:.2f} ms"
  return result





@info_cmd
async def SYSTEM(client,m):
  msg = await m.reply("<code>Sedang mengumpulkan data system. . .</code>")
  await msg.edit(cek_system())

def cek_system():
  try:
    #PLATFORM
    system = platform.uname()
    sistem = system.system
    kernel = system.release
    mesin = system.machine
    cpu_info = cpuinfo.get_cpu_info()['brand_raw']
    p_implementasi = platform.python_implementation()
    bit = platform.architecture()
    python_v = platform.python_version()
    uptime = duration((datetime.utcnow() - starttime).total_seconds())
   
    #DISK
    percent_disk = psutil.disk_usage(".").percent
    total, used, free = shutil.disk_usage(".")
    total_disk = size(total)
    used_disk = size(used)
    free_disk = size(free)
    process = psutil.Process(os.getpid())
    bot_usage = f"{round(process.memory_info()[0]/1024 ** 2)} MB"
    upload = size(psutil.net_io_counters().bytes_sent)
    download = size(psutil.net_io_counters().bytes_recv)

    
    #RAM
    percent_ram = psutil.virtual_memory().percent
    total_ram = size(psutil.virtual_memory().total)
    used_ram = size(psutil.virtual_memory().used)
    
    #CPU
    cpu_percentage = psutil.cpu_percent()
    cpu_counts = psutil.cpu_count()
    
    msg = f"""
**CPU** ( {cpu_counts} core / {cpu_percentage}% )

❏ **SYSTEM**
├• **System** ➥ `{sistem}`
├• **Kernel** ➥ `{kernel}`
├• **CPU** ➥ `{cpu_info}`
├• **Machine** ➥ `{mesin}`
├• **Py_Implementation** ➥ `{p_implementasi}`
├• **BIT** ➥ `{bit[0]}`|`{bit[1]}`
├• **Python Version** ➥ `{python_v}`
└• **Pyro** ➥ `{__version__}`

❏ **DISK**
├• **Percent** ➥ `{percent_disk}%`
├• **Total** ➥ `{total_disk}`
├• **Used** ➥ `{used_disk}`
├• **Bot Usage** ➥ `{bot_usage}`
├• **Upload** ➥ `{upload}`
├• **Download** ➥ `{download}`
└• **Free** ➥ `{free_disk}`

❏ **RAM**
├• **Percent** ➥ `{percent_ram}%`
├• **Total** ➥ `{total_ram}`
└• **Used** ➥ `{used_ram}`



<b>UPTIME:</b> {uptime}
"""
    return msg
  except Exception as e:
    return f"Terjadi kesalahan dalam mengumpulkan data system\n**EROR**: `{e}`"


