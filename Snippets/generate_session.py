from pyrogram import Client

app = Client(":memory:")

with app:
    session_string = app.export_session_string()
    with open("session.txt", mode="w+", encoding="utf8") as s_file:
        s_file.write(session_string)
    print("Session String has been saved to session.txt. KEEP IT SAFE!")
    print(session_string)
