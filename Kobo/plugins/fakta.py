from bs4 import BeautifulSoup as BS 
import requests 
from config import USER_AGENT
from deep_translator import GoogleTranslator 

from Kobo.decorators.decorator import info_cmd,bot_admin,error 

headers = {
  'User-agent': USER_AGENT
}

@info_cmd
@bot_admin
@error
async def FAKTA(client,m):
  msg = await m.reply('<code>Hmm bentarr yaa. . .</code>')
  url = "https://www.google.com/search?q=fun+fact&gl=id&hl=id"
  req = requests.get(url,headers=headers).text
  bs = BS(req,'html.parser')
  soal = bs.find('div',jsname='H17AHc',class_='sW6dbe')
  jawaban = bs.find('div',class_='DRBylb').find('div')
  pesan = f"<b>FAKTA MENYENANGKAN DARI KOBO</b>\n\n{tr(str(soal.text))}\n\n{tr(str(jawaban.text))}"
  await msg.edit(pesan) 

def tr(text):
  return GoogleTranslator(source="auto",target='id').translate(text)