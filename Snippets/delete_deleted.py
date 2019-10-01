from time import time

from pyrogram import Client
from pyrogram.errors import FloodWait

chat = "pyrogramlounge"
app = Client("my_account")

with app:
    deleted = [x for x in app.iter_chat_members(chat) if x.user.is_deleted]
    print(len(deleted), "deleted accounts found")
    for u in deleted:
        try:
            app.kick_chat_member(chat, u.user.id, int(time.time() + 60))
        except FloodWait as e:
            time.sleep(e.x)
