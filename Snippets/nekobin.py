# Paste a replied-to message to https://nekobin.com.

import requests
from requests import HTTPError

from pyrogram import Client
from pyrogram.types import filters

app = Client("my_account")
URL = "nekobin.com"
post = "https://nekobin.com/api/documents"


@app.on_message(filters.command("neko", prefixes="."))
def neko(app, msg):
    msg.edit_text("`pasting...`")
    text = msg.reply_to_message.text if msg.reply_to_message else msg.text[7:]
    try:
        paste = requests.post(post, data={"content": text})
        paste.raise_for_status()
    except (HTTPError, ConnectionError) as e:
        msg.edit_text(f"`Pasting failed\n{e}`")
    else:
        msg.edit_text(
            f"{URL}/{paste.json()['result']['key']}", disable_web_page_preview=True
        )


app.run()
