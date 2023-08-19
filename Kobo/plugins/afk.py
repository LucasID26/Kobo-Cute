from pyrogram import filters 
from config import bot
import time 
import asyncio 
import json
from pyrogram import enums
import re

from Kobo.decorators.decorator import bot_admin,group,info_cmd,error

a = open("JSON/afk.json")
afk_ = json.load(a)


TIME_DURATION_UNITS = ( ('minggu', 60 * 60 * 24 * 7), ('hari', 60 * 60 * 24), ('jam', 60 * 60), ('menit', 60), ('detik', 1))
def _human_time_duration(seconds):
  if seconds == 0:
    return 'Baru aja off'
  parts = []
  for unit, div in TIME_DURATION_UNITS:
    amount, seconds = divmod(int(seconds), div)
    if amount > 0:
      parts.append('{} {}{}' .format(amount, unit, "" if amount == 1 else ""))
  return ', '.join(parts) 



@info_cmd
@group
@bot_admin
@error
async def AFK(client,m):
  userid = str(m.from_user.id)
  if userid in afk_:
    msg_reason = "Yo ndak tau orang gada ngasi alasan"
    start_time = time.time()
    reason = msg_reason if len(m.text.split("afk ")) == 1 else m.text.split("afk ")[1]
    afk_[userid]["reason"] = reason
    with open("JSON/afk.json","w") as out:
      json.dump(afk_,out, indent=2) 
    await m.reply(f"❏ <b>Update AFK!</b>\n└ <b>Karena:</b> <code>{reason}</code>")
  elif not userid in afk_:
    start_time = time.time() 
    msg_reason = "Yo ndak tau orang gada ngasi alasan"
    reason = msg_reason if len(m.text.split("afk ")) == 1 else m.text.split("afk ")[1]
    afk_[userid] = {"start_time": start_time,
                         "reason": reason}
    with open("JSON/afk.json","w") as out:
      json.dump(afk_,out, indent=2)
    await m.reply(f"❏ <b>Telah AFK!</b>\n└ <b>Karena:</b> <code>{reason}</code>")

@bot.on_message(~filters.private,group=1)
async def afk_respon(client,m):
  if m.text:
    if m.text.lower().startswith('kobo'):
      return 
  userid = str(m.from_user.id)
  if userid in afk_:
    reason = afk_[userid]["reason"]
    end_time = time.time()
    start_time = afk_[userid]["start_time"]
    afk_time = end_time - start_time
    uptime = _human_time_duration(int(afk_time))
    await m.reply(f"❏ {m.from_user.mention}\n⌦ <b>STATUS:</b> <code>ONLINE!</code>\n⌦ <b>Selama:</b> <code>{uptime}</code>")
    del afk_[str(m.from_user.id)]
    with open("JSON/afk.json","w") as out:
      json.dump(afk_,out, indent=2)
  if m.reply_to_message:
    user = m.reply_to_message.from_user
    if str(user.id) in afk_: 
      reason = afk_[str(user.id)]["reason"]
      end_time = time.time()
      start_time = afk_[str(user.id)]["start_time"]
      afk_time = end_time - start_time
      uptime = _human_time_duration(int(afk_time))
      await m.reply(f"❏ {user.mention}\n⌦ <b>STATUS:</b> <code>AFK!</code>\n⌦ <b>Karena:</b> <code>{reason}</code>\n⌦ <b>Selama:</b> <code>{uptime}</code>")
    else:
      pass
  elif m.entities:
    entity = m.entities
    j = 0
    for _ in range(len(entity)):
      if (entity[j].type) == enums.MessageEntityType.MENTION:
        found = re.findall("@([_0-9a-zA-Z]+)", m.text)
        get_user = found[j]
        userid = await bot.get_users(get_user) 
        user_id = str(userid.id)
        mention = (await bot.get_users(user_id)).mention
        if user_id in afk_: 
          reason = afk_[user_id]["reason"]
          end_time = time.time()
          start_time = afk_[user_id]["start_time"]
          afk_time = end_time - start_time
          uptime = _human_time_duration(int(afk_time))
          await m.reply(f"❏ {mention}\n⌦ <b>STATUS:</b> <code>AFK!</code>\n⌦ <b>Karena:</b> <code>{reason}</code>\n⌦ <b>Selama:</b> <code>{uptime}</code>")
        else:
          pass
      elif (entity[j].type) == enums.MessageEntityType.TEXT_MENTION:
        userid = entity[j].user 
        user_id = str(userid.id)
        mention = (await bot.get_users(user_id)).mention
        if user_id in afk_: 
          reason = afk_[user_id]["reason"]
          end_time = time.time()
          start_time = afk_[user_id]["start_time"]
          afk_time = end_time - start_time
          uptime = _human_time_duration(int(afk_time))
          await m.reply(f"❏ {mention}\n⌦ <b>STATUS:</b> <code>AFK!</code>\n⌦ <b>Karena:</b> <code>{reason}</code>\n⌦ <b>Selama:</b> <code>{uptime}</code>")
        else:
          pass