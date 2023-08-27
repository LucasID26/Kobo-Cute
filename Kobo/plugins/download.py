from Kobo.tools import httpy
import os 
import re
from urllib.parse import urlparse
import asyncio
from Kobo.decorators.decorator import info_cmd,bot_admin,error
import time 
import requests
from pyrogram.types import InputMediaPhoto, InputMediaVideo 
from pyrogram import filters
from config import bot

@info_cmd
@bot_admin
@error
async def DOWNLOAD(client,m): 
  text = m.text
  pattern = re.compile(r'https?://\S+')
  links = re.findall(pattern, text)
  if not links:
    return await m.reply("Silahkan cantumkan link!!")
  msg = await m.reply(f"Url ditemukan berjumlah {len(links)}")
  jumlah = 0
  await asyncio.sleep(2)
  for link in links:
    parse = urlparse(link)
    msg1 = await m.reply("<code>Checking Url...</code>")
    await asyncio.sleep(2)
    if parse.netloc in ['www.youtube.com', 'youtu.be', 'youtube.com', 'youtu.be']:
      await YOUTUBE(link, m, msg1)    
      
    elif parse.netloc in ['vt.tiktok.com','vm.tiktok.com']:
      await TIKTOK(link, m, msg1)

    elif parse.netloc in ['www.instagram.com']:
      await INSTAGRAM(link, m, msg1)

    elif parse.netloc in ['www.facebook.com','fb.watch']:
      await FACEBOOK(link, m, msg1)
    
    else:
      await msg1.edit(f"Url {link} tidak valid atau tidak terdaftar dalam database saya!!")
  await msg.delete()





async def YOUTUBE(link, m, msg1):
  try:
    await msg1.delete()
    msg1 = await m.chat.ask('Mau download mp3 atau mp4?\n\nbalas pesan ini',reply_to_message_id=m.id,filters=filters.user(m.from_user.id) & filters.text & filters.reply,timeout=600) 
    input = msg1.text.lower()
    if input in ['mp3','mp4','video','musik','lagu']:
      await msg1.request.edit_text(f"<code>Mendownload media dari YOUTUBE...</code>")
      url = f"https://api.akuari.my.id/downloader/yt1?link={link}"
      req = await httpy.get(url)
      photo_url = req['info']['thumbnail']
      video_url = req['urldl_video']['link']
      audio_url = req['urldl_audio']['link']
      judul = req['info']['title']

      photo = await httpy.download_url(photo_url,f'{judul}.jpg')
      video = await httpy.download_url(video_url,f'{judul}.mp4')
      audio = await httpy.download_url(audio_url,f'{judul}.mp3')
      await msg1.request.edit_text("<code>Mengirim media...</code>")
      if input in ['mp4','video']:
        await m.reply_video(video=open(video,'rb'),thumb=photo,caption=judul)
      elif input in ['mp3','lagu','musik']:
        await m.reply_audio(audio=open(audio,'rb'),thumb=photo,caption=judul)
      os.remove(photo)
      os.remove(video)
      os.remove(audio)
    else:
      await msg1.request.edit_text('Input salah melanjutkan ke url berikutnya jika ada!!')
      await asyncio.sleep(2)
    await msg1.request.delete()
  except:
    await msg1.request.edit_text("Gagal mendownload media dari YOUTUBE!!")


async def TIKTOK(link, m, msg1):
  try:
    await msg1.delete()
    msg1 = await m.chat.ask('Mau download mp3 atau mp4?\n\nbalas pesan ini',reply_to_message_id=m.id,filters=filters.user(m.from_user.id) & filters.text & filters.reply,timeout=600) 
    input = msg1.text.lower()
    if input in ['mp3','mp4','video','musik','lagu']:
      await msg1.request.edit_text(f"<code>Mendownload media dari TIKTOK...</code>")
      url = f"https://api.akuari.my.id/downloader/tiktok?link={link}"
      req = await httpy.get(url)
      photo_url = req['respon']['thumbnail']
      video_url = req['respon']['media']
      audio_url = req['respon']['music']
      judul = req['respon']['description']

      photo = await httpy.download_url(photo_url,f'{judul}.jpg')
      video = await httpy.download_url(video_url,f'{judul}.mp4')
      audio = await httpy.download_url(audio_url,f'{judul}.mp3')
      await msg1.request.edit_text("<code>Mengirim media...</code>") 
      if input in ['mp4','video']:
        await m.reply_video(video=open(video,'rb'),thumb=photo,caption=judul)
      elif input in ['mp3','lagu','musik']:
        await m.reply_audio(audio=open(audio,'rb'),thumb=photo,caption=judul)
      os.remove(photo)
      os.remove(video)
      os.remove(audio)
    else:
      await msg1.request.edit_text("Input salah melanjutkan ke url berikutnya jika ada!!")
    await msg1.request.delete()
  except:
    await msg1.request.edit_text("Gagal mendownload media dari TIKTOK!!")


async def FACEBOOK(link, m, msg1):
  try:
    await msg1.delete()
    msg1 = await m.chat.ask('Mau download mp3 atau mp4?\n\nbalas pesan ini',reply_to_message_id=m.id,filters=filters.user(m.from_user.id) & filters.text & filters.reply,timeout=600) 
    input = msg1.text.lower()
    if input in ['mp3','mp4','video','musik','lagu']:
      await msg1.request.edit_text(f"<code>Mendownload media dari FACEBOOK...</code>")
      url = f'https://api.akuari.my.id/downloader/fbdl2?link={link}'
      req = await httpy.get(url)
      video_url = req['hasil'][0]['url']
      audio_url = req['hasil'][1]['url']
      
      video = await httpy.download_url(video_url,f'{time.time()}.mp4')
      audio = await httpy.download_url(audio_url,f'{time.time()}.mp3')
      await msg1.request.edit_text("<code>Mengirim media...</code>") 
      if input in ['mp4','video']:
        await m.reply_video(video=open(video,'rb'))
      elif input in ['mp3','lagu','musik']:
        await m.reply_audio(audio=open(audio,'rb'))
      os.remove(video)
      os.remove(audio)
    else:
      await msg1.request.edit_text("Input salah melanjutkan ke url berikutnya jika ada!!")
    await msg1.request.delete()
  except:
    await msg1.request.edit_text("Gagal mendownload media dari FACEBOOK!!")
      


async def INSTAGRAM(link, m, msg1):
  try:
    await msg1.edit(f"<code>Mendownload media dari INSTAGRAM...</code>")
    url = f"https://api.akuari.my.id/downloader/igdl2?link={link}"
    req = await httpy.get(url)
    if len(req['respon']) == 0:
      return await msg1.edit("Media tidak bisa di download atau mungkin private!")
    media = []
    for i in req['respon']:
      content_type = requests.head(i['url']).headers.get("Content-Type")
      if "image/jpeg" in content_type:
        photo = await httpy.download_url(i['url'],f'{time.time()}.jpg')
        media.append(
          InputMediaPhoto(open(photo,'rb'))) 
        os.remove(photo)
      elif "video/mp4" in content_type:
        video = await httpy.download_url(i['url'],f'{time.time()}.mp4')
        media.append(
          InputMediaVideo(open(video,'rb')))
        os.remove(video)
      else:
        pass 
    await msg1.edit("<code>Mengirim media...</code>")
    await bot.send_media_group(m.chat.id,media=media,reply_to_message_id=m.id)     
    await msg1.delete()
  except:
    await msg1.edit("Gagal mendownload media dari YOUTUBE!!")