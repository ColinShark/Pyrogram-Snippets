# This snippets gives you a count of all stickers you have saved across all your packs

from pyrogram import Client
from pyrogram.raw import functions

app = Client("my_account")

with app:
    all_sets = app.send(functions.messages.GetAllStickers(hash=0)).sets
    count = sum([x.count for x in all_sets])
    print(
        f"{count} stickers across {len(all_sets)} sets.\n"
        f"Average of {count / len(all_sets):.2f} stickers per pack."
    )
