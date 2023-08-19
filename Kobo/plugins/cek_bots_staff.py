from pyrogram import filters, enums
from pyrogram.errors import FloodWait 
from pyrogram.enums import ChatMemberStatus
from config import bot
import asyncio 

from Kobo.decorators.decorator import admins_only,bot_admin,group,error,info_cmd


@info_cmd
@group 
@bot_admin
@admins_only 
@error
async def BOTS(client, message):  
  try:
    botList = []
    async for bots in bot.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.BOTS):
      botList.append(bots.user)
    lenBotList = len(botList) 
    text3  = f"**BOT LIST - {message.chat.title}**\n\n🤖 Bots\n"
    while len(botList) > 1:
      bots = botList.pop(0)
      text3 += f"├ {bots.mention}\n"    
    else:    
      bots = botList.pop(0)
      text3 += f"└ {bots.mention}\n\n"
      text3 += f"✅ | **Total jumlah bot**: {lenBotList}"
      await message.reply(text=text3) 
  except Exception as e:
    await message.reply(e,quote=True)




#ADMIN/STAFF GROUP 
@info_cmd
@group
@bot_admin
@admins_only
@error
async def STAFF(client, message):
  try: 
    adminList = []
    ownerList = []
    async for admin in bot.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
      if admin.privileges.is_anonymous == False:
        if admin.user.is_bot == True:
          pass
        elif admin.status == ChatMemberStatus.OWNER:
          ownerList.append(admin.user)
        else:  
          adminList.append(admin.user)
      else:
        pass   
    lenAdminList= len(ownerList) + len(adminList)  
    text2 = f"**GROUP STAFF - {message.chat.title}**\n\n"
    try:
      owner = ownerList[0]
      if owner.username == None:
        text2 += f"👑 Owner\n└ {owner.mention}\n\n👮🏻 Admins\n"
      else:
        text2 += f"👑 Owner\n└ @{owner.username}\n\n👮🏻 Admins\n"
    except:
      text2 += f"👑 Owner\n└ <i>Hidden</i>\n\n👮🏻 Admins\n"
    if len(adminList) == 0:
      text2 += "└ <i>Admins are hidden</i>"
      await message.reply_text(text2) 
    else:  
      while len(adminList) > 1:
        admin = adminList.pop(0)
        if admin.username == None:
          text2 += f"├ {admin.mention}\n"
        else:
          text2 += f"├ @{admin.username}\n"    
      else:    
        admin = adminList.pop(0)
        if admin.username == None:
          text2 += f"└ {admin.mention}\n\n"
        else:
          text2 += f"└ @{admin.username}\n\n"
      text2 += f"✅ | **Jumlah total admins**: {lenAdminList}\n❌ | Bot dan admin tersembunyi tidak diikut sertakan." 
      await message.reply_text(text2) 
  except FloodWait as e:
    await asyncio.sleep(e.value) 
