from pyrogram import Client


chat = "pyrogramlounge"
limit = 2000
# Limit is for how many messages you want to look through
app = Client("my_account")

class custom(dict):
    def __missing__(self, key):
        return 0


with app:
    words = custom()
    progress = app.send_message(chat, "`processed 0 messages...`")
    total = 0
    for msg in app.iter_history(chat, limit):
        total += 1
        if total % 200 == 0:
            progress.edit_text(f"`processed {total} messages...`")
        if msg.text:
            for word in msg.text.split():
                words[word.lower()] += 1
        if msg.caption:
            for word in msg.caption.split():
                words[word.lower()] += 1
    freq = sorted(words, key=words.get, reverse=True)
    out = "Word Counter\n"
    for i in range(50):
        out += f"{i+1}. {words[freq[i]]}: {freq[i]}\n"

    progress.edit_text(out, parse_mode=None)
