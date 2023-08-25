from config import USER_AGENT,bot
from requests import get 
import json
import os
import random
import asyncio 

from pyrogram import filters,enums
from Kobo.decorators.decorator import error,info_cmd

from Kobo.tools import get


headers = {
  'User-agent': USER_AGENT
}



@info_cmd
@error
async def AI(client,m):
  teks = m.text
  teks2 = teks.split(" ",1)
  try:
    try:
      await BARD(teks2[1],m)
    except:
      msg = await m.reply("<code>Hmm mengganti kepintaran otomatis...</code>")
      await GPT(teks2[1],msg)
  except:
    msg2 = "Ahh kobo tidak tau harus ngapain","Auu ahh nyuruh yang bener 😠","Sedang mengalami gangguan silahkan coba lain kali!","au ah kobo lagi mager","gamau!","dih lu siapa nyuruh²","bodo amat!"
    await m.reply(random.choice(msg2))


async def BARD(input,m):
  await bot.send_chat_action(m.chat.id,enums.ChatAction.TYPING)
  req = await get(f"http://api.safone.me/bard?message={input}",headers=headers)
  content = req['message']
  img = req['extras'][0]['images']
  if len(img) != 0:
    max = 4096
    if len(content) > max:
      part1 = content[:max]
      part2 = content[max:]
      await m.reply_photo(photo=img[0],caption=part1)
      await m.reply(part2)
    else:
      await m.reply_photo(photo=img[0],caption=content)
  else:
    max = 4096 
    if len(content) > max:
      part1 = content[:max]
      part2 = content[max:]
      await m.reply(part1)
      await m.reply(part2)
    else:
      await m.reply(content)
    
async def GPT(input,msg):
  await msg.edit("<code>Mencoba berfikir kembali...</code>") 
  await bot.send_chat_action(m.chat.id,enums.ChatAction.TYPING)
  req = await get(f"https://api.akuari.my.id/ai/gpt?chat={input}",headers=headers)
  content = req['respon']
  max = 4096
  if len(content) > max:
    part1 = content[:max]
    part2 = content[max:]
    await msg.edit(part1) 
    await m.reply(part2)
  else:
    await msg.edit(content)