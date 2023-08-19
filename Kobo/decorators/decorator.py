from functools import wraps
from config import bot,own
from pyrogram import enums
from time import time
from pyrogram.enums import ChatMemberStatus
from datetime import datetime 
from pytz import timezone
from pyrogram import Client
import traceback
from pyrogram.errors.exceptions.forbidden_403 import ChatWriteForbidden
from pyrogram.errors import FloodWait



def split_limits(text):
  if len(text) < 2048:
    return [text]

  lines = text.splitlines(True)
  small_msg = ""
  result = []
  for line in lines:
    if len(small_msg) + len(line) < 2048:
      small_msg += line
    else:
      result.append(small_msg)
      small_msg = line
  result.append(small_msg)

  return result

def error(func):
  @wraps(func)
  async def capture(client, message, *args, **kwargs):
    try:
      return await func(client, message, *args, **kwargs)
    except ChatWriteForbidden:
      return await bot.leave_chat(message.chat.id)
    except Exception as err:
      exc = traceback.format_exc()
      error_feedback = split_limits(
          "**ERROR** | {} | {}({})\n\n\n".format(">">
          message.from_user.mention if message.from_user else 0,
          message.chat.id if message.chat else 0,
          message.chat.title if message.chat else 0,
          message.text or message.caption,
          exc,
        )
      )
      error = f"__**Respon Error!**__\n**Error:** {err}"
      for x in error_feedback:        
        try:
          await bot.send_message(-1001519186585, x)
          try:
            await client.message.edit(error)
          except Exception as e:
            await message.reply(error)
        except FloodWait as e:
          await asyncio.sleep(e.value)
        raise err

  return capture







def info_cmd(func):
  @wraps(func)
  async def cmd(client,m,*args,**kwargs):
    t_zona= datetime.now(tz=timezone('Asia/Makassar')) 
    hari = t_zona.strftime("%A")
    tgl = t_zona.strftime("%d/%B/%Y")
    jam = t_zona.strftime("%H:%M:%S")
    user = m.from_user.mention
    cmd1 = m.command
    text = f"**Informasi Bot CMD:**\n"
    if m.from_user.id in own:
      return await func(client,m,*args,**kwargs)
    if m.chat.type.value == 'private':
      text += f"""
**Chat type {m.chat.type.value}**
**From:** {user}
**Hari:** {hari}
**TGL:** {tgl}
**Jam:** {jam}
**Perintah:** {m.text}
"""     
      await bot.send_message(-1001738215280,text)
      return await func(client,m,*args,**kwargs)
   
    else:
      chtid = str(m.chat.id)[4:]
      title = m.chat.title
      msg_id = m.id
      if m.chat.is_forum == True:
        thread_id = m.topics.id
        link_id = f"https://t.me/c/{chtid}/{thread_id}/{msg_id}"
      else:
        link_id = f"https://t.me/c/{chtid}/{msg_id}"

      text += f"""
**Chat type {m.chat.type.value}**
**Group:** {title}
**Pesan:** click
**From:** {user}
**Hari:** {hari}
**TGL:** {tgl}
**Jam:** {jam}
**Perintah:** {m.text}
"""
      await bot.send_message(-1001738215280,text)
      return await func(client,m,*args,**kwargs)
  return cmd





def admins_only(func):
  @wraps(func)
  async def admins(client,m,*args,**kwargs): 
    if m.from_user.id in own:
      return await func(client, m, *args, **kwargs)
    if m.chat.type.value == 'private':
      return await func(client,m,*args,**kwargs) 
    else:
      admin = await bot.get_chat_member(m.chat.id,m.from_user.id)
      if admin.status.value in ['owner','administrator']:
        return await func(client, m, *args, **kwargs)
      else:
        return await m.reply_text("Anda harus menjadi admin untuk melakukan ini.")
  return admins


def bot_admin(func):
  @wraps(func)
  async def admins(client,m,*args,**kwargs):
    imbot = await bot.get_me()
    idbot = imbot.id
    if m.from_user.id in own:
      return await func(client,m,*args,**kwargs)
    if m.chat.type.value == 'private':
      return await func(client,m,*args,**kwargs) 
    else:
      infobot = await bot.get_chat_member(m.chat.id,idbot)
      if infobot.status.value in ['owner','administrator']:
        return await func(client,m,*args,**kwargs)
      else:
        return await m.reply_text("Saya harus menjadi admin untuk menjalankan perintah ini.")
  return admins





admins_in_chat = {}

async def list_admin(chat_id):
  global admins_in_chat
  if chat_id in admins_in_chat:
    interval = time() - admins_in_chat[chat_id]["last_updated_at"]
    if interval < 3600:
      return admins_in_chat[chat_id]["data"]

    admins_in_chat[chat_id] = {
        "last_updated_at": time(),
        "data": [member.user.id async for member in bot.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS)],
    }
  return admins_in_chat[chat_id]["data"]




async def member_permissions(chat_id, user_id):
  perms = []
  try:
    member = await bot.get_chat_member(chat_id, user_id)
    perijinan = member.privileges
  except Exception:
    return []
  if member.status != enums.ChatMemberStatus.MEMBER:
    if perijinan.can_post_messages:
      perms.append("can_post_messages")
    if perijinan.can_edit_messages:
      perms.append("can_edit_messages")
    if perijinan.can_delete_messages:
      perms.append("can_delete_messages")
    if perijinan.can_restrict_members:
      perms.append("can_restrict_members")
    if perijinan.can_promote_members:
      perms.append("can_promote_members")
    if perijinan.can_change_info:
      perms.append("can_change_info")
    if perijinan.can_invite_users:
      perms.append("can_invite_users")
    if perijinan.can_pin_messages:
      perms.append("can_pin_messages")
    if perijinan.can_manage_video_chats:
      perms.append("can_manage_video_chats")
  return perms 


def izin(permission):
  def subFunc(func):
    @wraps(func)
    async def subFunc2(client, message, *args, **kwargs):
      chatID = message.chat.id
      if not message.from_user:
        # For anonymous admins
        if message.sender_chat and message.sender_chat.id == message.chat.id:
          return await message.reply_text(f"Anda tidak memiliki izin yang diperlukan untuk melakukan tindakan ini.\n**Izin:** {permission}")
      # For admins and sudo users
      userID = message.from_user.id
      permissions = await member_permissions(chatID, userID)
      if userID not in own and permission not in permissions:
        return await message.reply_text(f"Anda tidak memiliki izin yang diperlukan untuk melakukan tindakan ini.\n**Izin:** {permission}")
  
      return await func(client, message, *args, **kwargs)
    return subFunc2

  return subFunc







def private(func):
  @wraps(func)
  async def pv(client,m,*args,**kwargs):
    if m.chat.type.value == 'private':
      return await func(client, m, *args, **kwargs)
    else:
      return await m.reply_text("Perintah ini dibuat untuk digunakan di obrolan pribadi, bukan di obrolan group!")
  return pv

def group(func):
  @wraps(func)
  async def gc(client,m,*args,**kwargs):
    if m.chat.type.value != 'private':
      return await func(client, m, *args, **kwargs)
    else:
      return await m.reply_text("Perintah ini dibuat untuk digunakan di obrolan group, bukan di obrolan pribadi!")
  return gc
