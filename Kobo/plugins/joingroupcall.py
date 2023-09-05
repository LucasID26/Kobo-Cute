from config import *
from typing import Union, Optional
from datetime import datetime
from pyrogram import raw

from pyrogram import filters

@user.on_message(filters.command('joinvc') & filters.user(own) & filters.me, '')
async def joinvc(client, m):
  msg = await m.reply("Proccessing. . .")
  try:
    await join_group_call(chat_id=m.chat.id,)
    await msg.edit("Sukses. . .") 
  except Exception as e:
    await msg.edit(e)

async def get_group_call(chat_id: Union[int, str],limit: int = 1):
  peer = await user.resolve_peer(chat_id, muted=True)
        
  if isinstance(peer, raw.types.InputPeerChannel):
    call = (await user.invoke(
        raw.functions.channels.GetFullChannel(
            channel=peer))).full_chat.call
  else:
    if isinstance(peer, raw.types.InputPeerChat):
        call = (await user.invoke(
            raw.functions.messages.GetFullChat(
                chat_id=peer.chat_id
            ))).full_chat.call

  if call is None:
    return call

  return await user.invoke(
      raw.functions.phone.GetGroupCall(
          call=call,limit=limit))


async def join_group_call(chat_id: Union[int, str],muted: Optional[bool] = None,video_stopped: Optional[bool] = None,invite_hash: Optional[str] = None):
  group_call = await get_group_call(chat_id)

  if group_call is None:
    return None

  call = group_call.call

  return await user.invoke(
      raw.functions.phone.JoinGroupCall(
          call=raw.types.InputGroupCall(
              id=call.id,
              access_hash=call.access_hash),
          join_as=raw.types.InputUserSelf(),
          params=await user.invoke(
              raw.functions.phone.GetCallConfig()
          ),
          muted=muted,
          video_stopped=video_stopped,
          invite_hash=invite_hash))