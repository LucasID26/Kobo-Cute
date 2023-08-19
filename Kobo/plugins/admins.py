from config import *  
import asyncio
import re
from pyrogram.errors import UserNotParticipant 
from pyrogram.types import ChatPermissions,Message

from Kobo.decorators.decorator import izin, list_admin, admins_only, bot_admin, group, info_cmd, error 

def get_user(text):
  try:
    extracted_keywords = re.findall(r'\d+|@[\w]+', text)
    return extracted_keywords[0]
  except:
    return False



@info_cmd
@group
@bot_admin
@admins_only
@izin("can_restrict_members")
@error
async def KICK(client,m: Message):
  if m.reply_to_message is not None:
    users = m.reply_to_message.from_user.id
  elif len(m.command) >= 1 and not get_user(m.text):
    return await m.reply_text("Silahkan reply user/cantumkan username pengguna!")
  else:
    users = get_user(m.text) #m.text.split(" ",2)[2]
  try:
    user = await bot.get_chat_member(m.chat.id,users)
  except UserNotParticipant:
    return await m.reply_text("User bukan anggota dari group ini!")
  except :
    return await m.reply_text("Username tidak valid!")
  if user.user.id == client.me.id:
    return await m.reply_text("Anda mau kick saya?,saya bisa keluar sendiri bung!")
  elif user.user.id in own:
    return await m.reply_text("Oops tidak bisa karena beliau owner saya!")
  
  elif user.status.value in ['owner','administrator']:
    return await m.reply_text("Oops tidak bisa karena dia admin!")  
  mention = user.user.mention
  text = f"""
**Banned User:** {mention}
**By: {m.from_user.mention if m.from_user else 'Anon'}
"""
  if m.command[1][0] == "d":
    try:
      await m.reply_to_message.delete()
    except:
      pass
  await m.chat.ban_member(user.user.id)
  await m.reply_text(text)
  await asyncio.sleep(1)
  await m.chat.unban_member(user.user.id) 


@info_cmd
@group 
@bot_admin
@admins_only
@izin("can_restrict_members")
@error
async def BANNED(client,m):
  if m.reply_to_message is not None:
    users = m.reply_to_message.from_user.id
  elif len(m.command) >= 1 and not get_user(m.text):
    return await m.reply_text("Silahkan reply user/cantumkan username pengguna!")
  else:
    users = get_user(m.text) #m.text.split(" ",2)[2]
  try:
    user = await bot.get_chat_member(m.chat.id,users) 
    if user.status.value == 'banned':
      return await m.reply_text("User sudah ada dalam daftar banned group ini!")
  except UserNotParticipant:
    return await m.reply_text("User bukan anggota dari group ini!")
  except :
    return await m.reply_text("Username tidak valid!")
  if user.user.id == client.me.id:
    return await m.reply_text("Anda mau ban saya?,saya bisa keluar sendiri bung!")
  elif user.user.id in own:
    return await m.reply_text("Oops tidak bisa karena beliau owner saya!")
  
  elif user.status.value in ['owner','administrator']:
    return await m.reply_text("Oops tidak bisa karena dia admin!")  
  mention = user.user.mention
  text = f"""
**Banned User:** {mention}
**By: {m.from_user.mention if m.from_user else 'Anon'}
"""
  if m.command[1][0] == "d":
    try:
      await m.reply_to_message.delete()
    except:
      pass
  await m.chat.ban_member(user.user.id)
  await m.reply_text(text) 


@info_cmd
@group 
@bot_admin
@admins_only
@izin("can_restrict_members")
@error
async def UNBANNED(client,m):
  if m.reply_to_message is not None:
    users = m.reply_to_message.from_user.id
  elif len(m.command) >= 1 and not get_user(m.text):
    return await m.reply_text("Silahkan reply user/cantumkan username pengguna!")
  else:
    users = get_user(m.text) #m.text.split(" ",2)[2]
  try:
    user = await bot.get_chat_member(m.chat.id,users) 
  except UserNotParticipant:
    return await m.reply_text("User bukan anggota dari group ini!")
  except :
    return await m.reply_text("Username tidak valid!") 
  if user.status.value == 'banned':
    mention = user.user.mention
    text = f"""
**Unbanned User:** {mention}
**By: {m.from_user.mention if m.from_user else 'Anon'}
"""
    await m.chat.unban_member(user.user.id)
    return await m.reply_text(text) 
  elif user.status.value != 'banned':
    return await m.reply_text("User tidak ada dalam daftar banned group ini!")



@info_cmd
@group 
@bot_admin
@admins_only
@izin("can_restrict_members")
@error
async def MUTED(client,m: Message):
  if m.reply_to_message is not None:
    users = m.reply_to_message.from_user.id
  elif len(m.command) >= 1 and not get_user(m.text):
    return await m.reply("Silahkan reply user/cantumkan username pengguna!")
  else:
    users = get_user(m.text)
    #m.text.split(" ",2)[2]
  try:
    user = await bot.get_chat_member(m.chat.id,users) 
    if user.status.value == 'restricted':
      return await m.reply("User sudah ada dalam daftar muted group ini!")
  except UserNotParticipant:
    return await m.reply("User bukan anggota dari group ini!")
  except :
    return await m.reply("Username tidak valid!")
  if user.user.id == client.me.id:
    return await m.reply_text("Anda mau mute saya?")
  elif user.user.id in own:
    return await m.reply("Oops tidak bisa karena beliau owner saya!")
  
  elif user.status.value in ['owner','administrator']:
    return await m.reply("Oops tidak bisa karena dia admin!")  
  mention = user.user.mention
  text = f"""
**Muted User:** {mention}
**By: {m.from_user.mention if m.from_user else 'Anon'}
"""
  if m.command[1][0] == "d":
    try:
      await m.reply_to_message.delete()
    except:
      pass
  await bot.restrict_chat_member(m.chat.id, user.user.id, ChatPermissions())
  await m.reply(text)


@info_cmd
@group 
@bot_admin
@admins_only
@izin("can_restrict_members")
@error
async def UNMUTED(client,m: Message):
  if m.reply_to_message is not None:
    users = m.reply_to_message.from_user.id
  elif len(m.command) >= 1 and not get_user(m.text):
    return await m.reply("Silahkan reply user/cantumkan username pengguna!")
  else:
    users = get_user(m.text) 
    #m.text.split(" ",2)[2]
  try:
    user = await bot.get_chat_member(m.chat.id,users) 
  except UserNotParticipant:
    return await m.reply("User bukan anggota dari group ini!")
  except :
    return await m.reply("Username tidak valid!") 
  if user.status.value == 'restricted':
    mention = user.user.mention
    text = f"""
**Unmute User:** {mention}
**By: {m.from_user.mention if m.from_user else 'Anon'}
"""
    await m.chat.unban_member(user.user.id)
    return await m.reply(text) 
  elif user.status.value != 'restricted':
    return await m.reply_text("User tidak ada dalam daftar muted group ini!") 


