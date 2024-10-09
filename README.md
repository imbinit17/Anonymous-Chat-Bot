# Anonymous-Chat-Bot

This bot enables fully anonymous chat between authorised users. When an authorised user messages the bot, it is securely broadcasted to all other authorised users without revealing the sender's identity.

<h1>How to use ?</h1>

1. Install python-telegram-bot
2. Set your telegram bot api key to "TOKEN" in environment variables .
3. Run the bot ! (file : telegram_bot.py)
4. Add users who will be authorised to use your bot by typing in the console : "?authorise chat_id"

You are ready to use the bot . Head to telegram and anonymously chat with your peers (authorised users) . Also check the other commands in console .

<h2>Note:</h2>

1. You will get API key from @BotFather in telegram once you create a bot .
2. To get chat_id for a particular user/group/channel (bot treats all three same ,thus you can add a private group's chat_id to the authorised user list too as per preference) , you can either :
   i. Open Telegram Web > Open the chat with desired user/group/channel > Copy chat_id from the URL that is 		   	numeric followed after the "#" (chat_id for group/channel would start with a '-' sign )
   ii. Use external bots
3. In case you have added the bot into a group/channel , please be aware that without admin permissions ,the bot would have no access to messages there
