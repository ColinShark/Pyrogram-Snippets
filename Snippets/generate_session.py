from pyrogram import Client

with Client(":memory:") as app, open("session.txt", "w+") as s_file:
    session_string = app.export_session_string()
    s_file.write(session_string)
    print("Session String has been saved to session.txt. KEEP IT SAFE!")
    print(session_string)
