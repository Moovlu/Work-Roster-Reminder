# Work-Roster-Reminder
A simple program to check for additions to my work roster and send a telegram message to me when it notices a change/update to the roster.

# How to use
The program is pretty simple to setup, first start by creating a Telegram account. **It's recommended you do this on a phone.**

After you have a Telegram account, you need to create a bot. You can do this by talking with [the bot father](https://t.me/botfather).

![Screenshot of the bot father](/readme/bot_father.png)

The bot father should list a bunch of different commands. We want to use the **/newbot** command

![Screenshot of the newbot command](/readme/new_bot.png)

You are free to name your bot whatever you would like. Following this, it will ask you for a username. This can also be anything.

After creating a bot it will congratulate you and provide you with a token. **Make sure to copy this**.

![Screenshot of token](/readme/bot_token.png)

Visit the link at the start of the congratulatory message and send **any** message to the bot, this will create a chat.

Now we need to find the chat ID for the chat we have just created. Visit the following link but **replace [token] with your token**

> ## https://api.telegram.org/bot[token]/getUpdates

This should bring you to a basic http response page. (look may vary with different browsers)

![Screenshot of http response](/readme/chat_id.png)

Once you have both the token and the chat ID, input them into the program's "info.ini" file.

## **Readme incomplete, to be added at a further date**