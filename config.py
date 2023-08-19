from pyrogram import Client 
import os 

own = [1928677026,5039288972]
ID = os.environ['API_ID']
HASH = os.environ['API_HASH']
TOKEN = os.environ['BOT_TOKEN']


bot = Client("KOBO",
            api_id=ID,
            api_hash=HASH,
            bot_token=TOKEN,
            in_memory=True)