from pyrogram import Client
from pyrogram.api import functions

chat = "pyrogramlounge"
app = Client("my_account")

with app:
    full_log = app.send(
        functions.channels.GetAdminLog(
            channel=app.resolve_peer(chat),
            q="",
            max_id=0,
            min_id=0,
            limit=0,
        )
    )
with open(f"recent_actions_{chat}.txt", "w", encoding="utf8") as log_file:
    log_file.write(str(full_log))
