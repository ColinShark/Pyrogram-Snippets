import time

from pyrogram import Client, Filters
from pyrogram.api import functions

app = Client("my_account")


@app.on_message(Filters.command(["s", "screenshot"], prefixes="."))
def take_a_screenshot(app, message):
    message.delete()
    app.send(
        functions.messages.SendScreenshotNotification(
            peer=app.resolve_peer(message.chat.id),
            reply_to_msg_id=0,
            random_id=app.rnd_id(),
        )
    )


app.run()
