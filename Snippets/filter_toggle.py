# Use .com to toggle a different message handler on or off.
# Handy if you want to control the usage of a specific command.

from pyrogram import Client, filters

app = Client("my_account")


def commute(self):
    """Switch states between `True` and `False`"""
    self.flag = not self.flag
    return self.flag


f = filters.create(lambda self, _: self.flag, flag=True, commute=commute)


@app.on_message(f & filters.command("hi", "."))
def hi(_, message):
    """Reply with "hi" in case toggle returns `True`"""
    message.reply_text("hi")


@app.on_message(filters.command("com", "."))
def toggle(_, message):
    """Switch between `True` and `False`"""
    c = f.commute()
    message.reply_text("enabled" if c else "disabled")


app.run()
