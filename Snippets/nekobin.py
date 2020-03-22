# Paste a replied-to message to https://del.dog.

import requests
from requests import HTTPError

from pyrogram import Client, Filters

app = Client("my_account")
URL = "nekobin.com"
post = "https://nekobin.com/api/documents"


@app.on_message(Filters.command("paste", prefixes="."))
def dogbin(app, msg):
    msg.edit_text("`pasting...`")
    text = msg.reply_to_message.text if msg.reply_to_message else msg.text[7:]
    try:
        paste = requests.post(post, data={"content": text})
        paste.raise_for_status()
    except (HTTPError, ConnectionError):
        msg.edit_text("`Pasting failed`")
    else:
        msg.edit_text(
            f"{URL}/{paste.json()['result']['key']}", disable_web_page_preview=True
        )


app.run()
