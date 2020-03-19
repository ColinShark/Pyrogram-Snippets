# Compare all names of a chat against an ASCII-encoded
# version and print each difference.

from pyrogram import Client

chat = "pyrogramchat"

app = Client("my_account")

with app:
    for member in app.iter_chat_members(chat):
        if member.user.is_deleted:
            continue
        x = member.user.first_name
        y = member.user.first_name.encode().decode("ascii", "ignore")
        if x != y:
            print(f"{x}\t|\t{y}")
