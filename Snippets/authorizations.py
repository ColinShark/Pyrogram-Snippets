# This Snippet will output a formatted list of all sessions and their creation date.
# If you want other information, please refer to the respective documentation:
# https://docs.pyrogram.org/telegram/types/authorization

from datetime import datetime

from pyrogram import Client
from pyrogram.raw.functions.account import GetAuthorizations

app = Client("my_account")

with app:
    auths = app.send(GetAuthorizations()).authorizations

    # Sort list of Authorizations and give us the longest name+version combination
    auths.sort(key=lambda x: x.date_created)
    width = max(auths, key=lambda x: len(x.app_name + x.app_version))
    width = len(width.app_name + width.app_version) + 1

    for auth in auths:
        print(f"{auth.app_name} {auth.app_version}".ljust(width), end=" - ")
        print(datetime.fromtimestamp(auth.date_created))
