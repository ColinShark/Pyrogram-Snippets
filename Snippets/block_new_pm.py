# This script saves all your current chats and automatically blocks and reports ALL
# incoming private messages. Useful if you don't want any new chats whatsoever.

from pyrogram import Client, Filters
from pyrogram.api import functions

app = Client("my_account")

app.start()

whitelist = [dialog.chat.id for dialog in app.iter_dialogs() if dialog.chat.id > 0]


@app.on_message(Filters.private & ~Filters.chat(whitelist))
def block_new_pm(app, msg):
    whomst = msg.from_user.id
    whomst_peer = app.resolve_peer(whomst)
    app.block_user(whomst)
    app.send(functions.messages.ReportSpam(peer=whomst_peer))
    app.send(functions.messages.DeleteHistory(peer=whomst_peer, max_id=0))


app.idle()
app.stop()
