from pyrogram import Client, Filters

app = Client("my_account")


def commute(self):
    """Switch states between `True` and `False`"""
    self.flag = not self.flag
    return self.flag


f = Filters.create(lambda self, _: self.flag, flag=True, commute=commute)


@app.on_message(f & Filters.command("hi", "."))
def hi(app, message):
    """Reply with "hi" in case toggle returns `True`"""
    message.reply_text("hi")


@app.on_message(Filters.command("com", "."))
def toggle(app, message):
    """Switch between `True` and `False`"""
    c = f.commute()
    m.reply_text("enabled" if c else "disabled")


app.run()
