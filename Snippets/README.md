# Snippets

Here is a list of all Snippets for better overview and a clearer top-level Readme.

All snippets assume you have a `config.ini` with [your api id and hash set up][API].

| # | Name | Description |
| --: | --- | --- |
| 1. | [Delete Migrated](delete_migrated.py) | Delete all chats from your list that have been migrated to a supergroup.
| 2. | [Photo Size Threshold](photo_threshold.py) | Count the amount of photos above or below a given size.
| 3. | [Dogbin](dogbin.py) | Paste a message to [del.dog](https://del.dog) by replying `.paste` to it.
| 4. | [Block New PMs](block_new_pm.py) | Block new private messages from coming through. Instantly block and report the offender.
| 5. | [Participant%](participant_percent.py) | Get the % of people who have participated in the last 5000 messages.<sup>1</sup>
| 6. | [Word Count](word_count.py) | Get a list of the 50 most used words in the chat.<sup>1</sup>
| 7. | [Sticker Sets](all_sets.py) | Get a count of all saved stickers across all saved packs.
| 8. | [Unicode Names](unicode.py) | Get all members whose name contains unicode. Display their name with and without unicode characters.
| 9. | [Left Channels](left_channels.py) | Retrieve a list of all Channels<sup>2</sup> you've created and left.
| 10. | [Thanos](thanos.py) | You already know <small>(mutes half the chat for 24 hours)</small>
| 11. | [Deleted Account](delete_deleted.py) | Remove deleted accounts from the chat, without cluttering the ban list.
| 12. | [Unread](unread.py) | Mark a chat as unread and go back to the chatlist.
| 13. | [FloodWatch](flood_watch.py) | Count the messages of people and warn them, if they send too many too quickly<sup>3</sup>
| 14. | [Session String](generate_session.py) | Create a session string and save it to a `session.txt`. Handy when you use Heroku for hosting.<sup>4</sup>
| 15. | [Flip Text](flip_text.py) | Flip text upside down (`.flip My text` -> `Wʎ ʇǝxʇ`)

<sup>1: Iterating through a lot of messages might take some time.<br>
2: This includes Supergroups, as Telegram handles them the same internally.<br>
3: This has been [shared by !null in the Pyrogram Inn][FLOOD].<br>
4: Disclaimer: Keep that Session String SAFE. Anyone who has that key, can log in as you.<br>
</sup>

[API]: https://docs.pyrogram.org/intro/setup
[FLOOD]: https://t.me/PyrogramLounge/139704
