# Get the count of Members in a chat and check how many of those have sent a message
# in the last x messages. Change the limit variable to check more messages.

from pyrogram import Client

app = Client("my_account")

chat = "pyrogramchat"
people = {}

with app:
    total = app.get_chat_members_count(chat)
    for msg in app.iter_history(chat, limit=1000):
        if msg.from_user and not msg.from_user.is_bot:
            people[msg.from_user.id] = msg.from_user.first_name

print(len(people) / total)
