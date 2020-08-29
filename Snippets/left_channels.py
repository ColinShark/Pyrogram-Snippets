# Get a list of Channels you have created but left.
# This could come in handy if you need to re-join these or get an invite link for.

from pyrogram import Client
from pyrogram.raw import functions

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
