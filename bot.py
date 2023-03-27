from pyrogram import Client, filters

APP_ID = os.environ.get("APP_ID", None)
API_HASH = os.environ.get("API_HASH", None)
STRING_SESSION = os.environ.get("BOT_TOKEN", None)
PRE_LOG = os.environ.get("PRE_LOG", None)
OWNER_ID = "mmagneto"
try:
    userbot = Client(
        name='Userbot',
        api_id=APP_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION,
    ) 
    userbot.start()
    me = userbot.get_me()
    userbot.send_message(OWNER_ID, f"Userbot Bașlatıldı..\n\n**Premium Durumu**: {me.is_premium}\n**Ad**: {me.first_name}\n**id**: {me.id}")
except Exception as e:
    print(e)
