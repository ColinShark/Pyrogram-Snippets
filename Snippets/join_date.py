# Get a list of all chat members and sort them by the date they joined the group
# The Creator of the group has no join_date internally,
# so he gets the group creation date

import os
from datetime import datetime

from pyrogram import Client, filters
from pyrogram.types import Message

app = Client("my_account")


@app.on_message(filters.command("joindate") & filters.me)
def join_date(app, message: Message):
    members = []
    for m in app.iter_chat_members(message.chat.id):
        members.append(
            (
                m.user.first_name,
                m.joined_date or app.get_messages(message.chat.id, 1).date,
            )
        )

    members.sort(key=lambda member: member[1])

    with open("joined_date.txt", "w", encoding="utf8") as f:
        f.write("Join Date      First Name\n")
        for member in members:
            f.write(
                str(datetime.fromtimestamp(member[1]).strftime("%y-%m-%d %H:%M"))
                + f" {member[0]}\n"
            )

    app.send_document(message.chat.id, "joined_date.txt")
    os.remove("joined_date.txt")


app.run()
