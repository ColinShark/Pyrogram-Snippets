import requests

from pyrogram import Client, Filters

app = Client("my_account")
DOGBIN = "https://del.dog/"

@app.on_message(Filters.command("paste", prefix=".") & Filters.reply)
def dogbin(app, msg):
    msg.edit_text("`pasting...`")
    text = msg.reply_to_message.text
    try:
        paste = requests.post(f"{DOGBIN}/documents", data=text).json()["key"]
    except:
        msg.edit_text("`Pasting failed`")
    else:
        msg.edit_text(f"{DOGBIN}/{paste}")
