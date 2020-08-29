# Send .autoscroll in any chat to automatically read all sent messages until you call
# .autoscroll again. This is useful if you have Telegram open on another screen.

from pyrogram import Client, filters
from pyrogram.types import Message

app = Client("my_account")

f = filters.chat([])


@app.on_message(f)
def auto_read(_, message: Message):
    app.read_history(message.chat.id)
    message.continue_propagation()


@app.on_message(filters.command("autoscroll", ".") & filters.me)
def add_keep(_, message: Message):
    if message.chat.id in f:
        f.remove(message.chat.id)
        message.edit("Autoscroll deactivated")
    else:
        f.add(message.chat.id)
        message.edit("Autoscroll activated")


app.run()
