from pyrogram import Client 
import os 
import pyromod.listen


own = [1928677026,5039288972]
ID = os.environ['API_ID']
HASH = os.environ['API_HASH']
TOKEN = os.environ['BOT_TOKEN']
STRING = os.environ['STRING']
USER_AGENT = os.environ['USER_AGENT']
BARD_KEY = os.environ['BARD_KEY']

bot = Client("KOBO",
            api_id=ID,
            api_hash=HASH,
            bot_token=TOKEN,
            in_memory=True,
            alt_port=True) 

user = Client("Asisstant",
             session_string=STRING,
             in_memory=True,
             alt_port=True)


            