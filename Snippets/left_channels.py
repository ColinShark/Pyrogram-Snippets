from pyrogram import Client
from pyrogram.api import functions

app = Client("my_account", takeout=True)


with app:
    channels = [
        c
        for c in app.send(functions.channels.GetLeftChannels(offset=0)).chats
        if c.creator
    ]
    for channel in channels:
        print(channel.title)
# do other stuff with channel if you want
