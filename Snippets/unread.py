# This marks the current chat as unread and "closes" the Chat,
# putting you back to the chatlist.

from pyrogram import Client, Filters
from pyrogram.api import functions

app = Client("my_account")


@app.on_message(Filters.command("un", prefixes="."))
def unread_chat(app, message):
    message.delete()
    app.send(
        functions.messages.MarkDialogUnread(
            peer=app.resolve_peer(message.chat.id), unread=True
        )
    )


app.run()
