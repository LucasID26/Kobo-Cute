from config import USER_AGENT, bot
from requests import get
import json
import os
import random
import asyncio
from bardapi import Bard
from config import BARD_KEY
from pyrogram.types import InputMediaPhoto


from pyrogram import filters, enums
from Kobo.decorators.decorator import error, info_cmd

from Kobo.tools import httpy

headers = {'User-agent': USER_AGENT}


@info_cmd
@error
async def AI(client, m):
  teks = m.text
  teks2 = teks.split(" ", 1)
  msg = await m.reply("<code>Sedang berfikir. . .</code>")
  try: 
    try:
      await BARD1(teks2[1], m,  msg)
    except:
      await msg.edit("<code>Hmm mengganti kepintaran otomatis...</code>")
      await GPT(teks2[1], msg)
  except Exception as e:
    msg2 = "Ahh kobo tidak tau harus ngapain", "Auu ahh nyuruh yang bener 😠", "Sedang mengalami gangguan silahkan coba lain kali!", "au ah kobo lagi mager", "gamau!", "dih lu siapa nyuruh²", "bodo amat!"
    await msg.edit(random.choice(msg2))

async def BARD1(input, m, msg):
  token = BARD_KEY
  bard = Bard(token=token)
  result = bard.get_answer(input)
  content = result['content']
  links = result['links']
  photo = []
  for img in links:
    if img.endswith(('.jpg','.jpeg','.png')):
      photo.append(InputMediaPhoto(img))
  max = 4096    
  if len(photo) == 0:
    if len(content) > max:
      part1 = content[:max]
      part2 = content[max:]
      await msg.edit(part1)
      await msg.reply(part2)
    else:
      await msg.edit(content)
  else:
    send_media = await bot.send_media_group(m.chat.id,media=photo,reply_to_message_id=m.id)
    if len(content) > max:
      part1 = content[:max]
      part2 = content[max:]
      await send_media[0].reply(part1)
      await seng_media[0].reply(part2)
    else:
      await seng_media[0].reply(content)
    await msg.delete()


async def BARD(input, m):
  req = await httpy.get(f"https://api.safone.me/bard?message={input}")
  content = req['message']
  img = req['extras'][0]['images']
  if len(img) != 0:
    max = 4096
    if len(content) > max:
      part1 = content[:max]
      part2 = content[max:]
      await m.reply_photo(photo=img[0], caption=part1)
      await m.reply(part2)
    else:
      await m.reply_photo(photo=img[0], caption=content)
  else:
    max = 4096
    if len(content) > max:
      part1 = content[:max]
      part2 = content[max:]
      await m.reply(part1)
      await m.reply(part2)
    else:
      await m.reply(content)


async def GPT(input, msg):
  await msg.edit("<code>Mencoba berfikir kembali...</code>")
  req = await httpy.get(f"https://api.akuari.my.id/ai/gpt?chat={input}")
  content = req['respon']
  max = 4096
  if len(content) > max:
    part1 = content[:max]
    part2 = content[max:]
    await msg.edit(part1)
    await m.reply(part2)
  else:
    await msg.edit(content)


@bot.on_message(filters.bot)
async def balas_bot(client,m):
  return await bot.send_message(m.chat.id,"hallo kawan ku kita sama² bot yaa")
