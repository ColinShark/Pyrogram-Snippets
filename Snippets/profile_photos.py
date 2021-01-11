# Download all profile photos of a specified user.
# Just in case you want them, or something.

from pyrogram import Client

app = Client("my_account")

user = "me"

with app:
    all_pics = app.iter_profile_photos(user)
    for i, pic in enumerate(all_pics, 1):
        path = app.download_media(
            message=pic.file_id,
            file_name=f"profile_pics/{user}/{i}.jpg",
        )
        print(path.split("\\")[-1])
