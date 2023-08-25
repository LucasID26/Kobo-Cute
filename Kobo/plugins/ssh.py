import requests
from bs4 import BeautifulSoup as BS 

from config import USER_AGENT 
from Kobo.decorators.decorator import info_cmd,bot_admin,error

headers = {
  'User-agent': USER_AGENT
}


@info_cmd
@bot_admin
@error
async def STORES(client,m):
  msg = "<b>INI DAFTAR SSH WEBSOCKET DARI SSHSTORES :</b>\n\n"
  req = requests.get("https://sshstores.net/ssh-websocket",headers=headers)
  bs = BS(req.text,"html.parser")
  get = bs.find_all('div',class_='card-body')
  for result in get:
    server = result.find('h4',class_='font-weight-bold')
    jumlah = result.find('div',class_='badge badge-pill badge-light font-weight-normal px-3 py-2')
    if server == None and jumlah == None:
        break
    if len(server.text.split()) > 1:
      replace_name = server.text.replace(" ","-")
      link = f"https://sshstores.net/ssh-websocket/{replace_name}"    
    else:
      link = f"https://sshstores.net/ssh-websocket/{server.text}"
    msg += f"<b>SERVER:</b> {server.text}\n<b>JUMLAH SERVER:</b> {jumlah.text}\n<b>URL:</b> [CREATE]({link})\n\n"
  await m.reply(msg)