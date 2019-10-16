from pyrogram import Client

app = Client("my_account")

threshold = 100 * 1024  # 100 kb
below = 0
above = 0
exact = 0
chat = "me"  # Saved Messages, any other @username works, too.

with app:
    for msg in app.iter_history(chat):
        if msg.photo and msg.photo.file_size < threshold:
            below += 1
        elif msg.photo and msg.photo.file_size > threshold:
            above += 1

print(f"Below: {below}\nAbove: {above}\nTotal: {above+below}")
