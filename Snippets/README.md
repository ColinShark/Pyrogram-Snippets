# Snippets

Here is a list of all Snippets for better overview and a clearer top-level Readme.

All snippets assume you have a `config.ini` with [your api id and hash set up][API].

| # | Name | Description |
| --: | --- | --- |
| 1. | [Delete Migrated](delete_migrated.py) | Delete all chats from your list that have been migrated to a supergroup.
| 2. | [Photo Size Threshold](photo_threshold.py) | Count the amount of photos above or below a given size.
| 3. | [Nekobin](nekobin.py) | Paste a message to [Nekobin](https://nekobin.com) by replying `.neko` to it.
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
| 15. | [Flip Text](flip_text.py) | Flip text upside down (`.flip My text` -> `Wʎ ʇǝxʇ`)<sup>5</sup>
| 16. | [Recent Actions](recent_actions.py) | Get a full list of all recent actions of a specified group.<sup>6</sup>
| 17. | [Profile Photos](profile_photos.py) | Download all profile folder from a supplied username and save them to a folder.<sup>7</sup>
| 18. | [Resolve Invite](resolve_invite_link.py) | Resolve an Invite Link to get the ID of the admin who made it and the Chat ID.
| 19. | [Delete Messages](delete_messages.py) | Delete all your messages by iterating through all messages in all chats.<sup>8</sup>
| 20. | [Auto Scroll](auto_scroll.py) | Send `.autoscroll` to auto-read all new messages in a chat in case you don't have Telegram in focus.
| 21. | [Filter Toggle](filter_toggle.py) | Send `.com` to disable the `.hi` handler. Helpful if you want to completely disable a handler on command.<sup>9</sup>
| 22. | [Screenshot](screenshot.py) | Send a Screenshot Notification. Works only in Private Chats.
| 23. | [Joined Date](join_date.py) | Get a list of all members sorted by date joined.

<sup>1: Iterating through a lot of messages might take some time.<br>
2: This includes Supergroups, as Telegram handles them the same internally.<br>
3: This has been [shared by !null in the Pyrogram Inn][FLOOD].<br>
4: Disclaimer: Keep that Session String SAFE. Anyone who has that key, can log in as you.<br>
5: This has been [shared by James Santagato in the Pyrogram Lounge][FLIP].<br>
6: Useful if you need the ID of people who have no messages left in your chat (eg join-message removed by bot).<br>
7: This will download profile photos individually, which creates a LOT of requests to Telegram. You might find yourself flood-limited.<br>
8: If you are not absolutely sure you want to delete all your messages, do NOT use this!<br>
9: This has been [shared by Dan in the Inn][TOGGLE].<br>
</sup>

[API]: https://docs.pyrogram.org/intro/setup
[FLOOD]: https://t.me/PyrogramLounge/139704
[FLIP]: https://t.me/PyrogramLounge/142144
[TOGGLE]: https://t.me/PyrogramChat/144618
