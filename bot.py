from pyrogram import Client, filters


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
    video = 
    userbot.send_video(
        chat_id=OWNER_ID,
        video=video)
except Exception as e:
    print(e)
