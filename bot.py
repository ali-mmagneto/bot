from pyrogram import Client, filters

APP_ID = 2374174
API_HASH = "c23db4aa92da73ff603666812268597a"
STRING_SESSION = "BACVj_JzS6Sqgnq754w8mbemtrHhrQAJfAtxzUsjcifzTzETUknZd1T25wP8ZRrIMsmKDxQDtSW3xlj7MXFrrZSuGxxyzaH3_bUXhCZP-5s4ZkcA87nWCUsEGSO96lkj3s3xa5sVTMXI7C6bA2Tv9kUGxRIjUCg810cx4dr9o9PrEWfKnzrW7F0yia2UbyNz_gyo1L3Jqtuy3LEG77LpydMOUtzAgmw3AUIyKsF2U6nF3ICf7lKp_baXnsEtDeBNiORqgRS0nxC5OxhdeSoBitJy3w7Lr5QfoUn39eIAag2vSu7f06QGrIVWOHVNKrefpFgaN1qjw3-O6J9ckbvLGZo1X19oqAA" 
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
    video = 
    userbot.send_video(
        chat_id=OWNER_ID,
        video=video)
except Exception as e:
    print(e)
