# Delete the history of all chats that have already been upgraded to a Supergroup.

from pyrogram import Client
from pyrogram.api import functions

app = Client("my_account")

with app:
    for dialog in app.iter_dialogs():
        if dialog.chat.type == "group":
            if dialog.message.migrate_to_chat_id:
                app.send(
                    functions.messages.DeleteHistory(
                        peer=app.resolve_peer(peer_id=dialog.chat.id),
                        max_id=0,
                        just_clear=False,
                        revoke=False,
                    )
                )
