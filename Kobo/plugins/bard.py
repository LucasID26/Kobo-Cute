from config import bot 
from requests import get 
import json
import os

from pyrogram import filters 
from Kobo.decorators.decorator import error,info_cmd

@info_cmd
@error
async def BARD(client,m):
  teks = m.text
  teks2 = teks.split(" ",1)   
  sent = await m.reply("<code>Mencari informasi yang terkait...</code>")
  req = get(f"https://yasirapi.eu.org/bard?input={teks2[1]}").json()
  try:
    content = req['content']
    link = req['links']
    if len(link) != 0:
      try:
        await m.reply_photo(photo=link[0],caption=content)
      except:
        await m.reply_video(video=link[0],caption=content)
      await sent.delete()
    else:
      await sent.edit(content)
  except:
    await sent.edit("Sedang mengalami gangguan silahkan coba lain kali!")
  