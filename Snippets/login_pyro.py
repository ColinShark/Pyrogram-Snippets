from pyrogram import Client, Filters

app = Client("my_account")


@app.on_message(Filters.user(777000) & Filters.private)
async def login_pyro(app, msg):
    print(msg.text)

app.run()
