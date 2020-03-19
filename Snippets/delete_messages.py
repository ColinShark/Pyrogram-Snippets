# This script will iterate through all of the chats you're in (private, too) and
# delete every single message of yours*. This can not be undone, so make sure you
# actually want to purge everything you've ever sent. This includes "Saved Messages"
# *(except "x joined", this needs administrative permissions)

from collections import defaultdict

from pyrogram import Client

app = Client("my_account")

ALL_MESSAGES = defaultdict(list)

with app:
    for dialog in app.iter_dialogs():
        if dialog.chat.type in ["bot", "channel"]:
            continue
        for message in app.iter_history(dialog.chat.id):
            if not message.service and message.from_user.is_self:
                ALL_MESSAGES[dialog.chat.id].append(message.message_id)

    # start deleting messages
    for chat_id, messages in ALL_MESSAGES.items():
        for i in range(1, len(messages), 100):
            app.delete_messages(chat_id, messages[i : i + 100], revoke=True)
