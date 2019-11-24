from base64 import urlsafe_b64decode
from struct import unpack

from pyrogram import Client, Filters, Message

app = Client("my_account")


@app.on_message(Filters.command("invite", ".") & Filters.me)
def resolve_invite(app: Client, message: Message):
    link = message.command[1].split("/")[-1]
    d = urlsafe_b64decode(link + "==")
    message.edit_text(
        "Invite Link: `{}`\nAdmin: `{}`\nChat: `-100{}`\nHash: `{}`".format(
            link, *unpack(">iiq", d)
        )
    )


app.run()
