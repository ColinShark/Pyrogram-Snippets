# Watch how many messages people send and warn them about sending too many messages.
# If you have admin permissions they will be muted.

import time

from pyrogram import Client, filters
from pyrogram.types import Message

app = Client("my_account")


flooders = {}
FLOOD_MUTE_TIME = 60
GROUP_ADMINS = {}


def get_chat_admins(app: Client, message: Message) -> list:
    return [
        admin.user.id
        for admin in app.get_chat_members(message.chat.id, filter="administrators")
    ]


@app.on_message(filters.group)
def flood_watcher(app, message: Message):
    c_id = message.chat.id
    u_id = message.from_user.id
    try:
        if u_id not in GROUP_ADMINS[c_id]:
            try:
                flooders[c_id][u_id] += 1
            except KeyError:
                flooders[c_id][u_id] = 1
            else:
                if flooders[c_id][u_id] > 4:
                    app.restrict_chat_member(
                        c_id, u_id, int(time.time() + FLOOD_MUTE_TIME)
                    )
                    message.reply_text(
                        "Please avoid spamming, or you might get kicked."
                    )
                else:
                    time.sleep(1.5)
                    try:
                        flooders[c_id][u_id] -= 1
                        if flooders[c_id][u_id] == 0:
                            del flooders[c_id][u_id]
                    except KeyError as e:
                        print(e)
    except KeyError:
        GROUP_ADMINS[c_id] = get_chat_admins(app, message)


app.run()
