from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler ,filters ,MessageHandler
import os ,threading ,asyncio
import database

async def start(update: Update, context) -> None:
    chat_id = update.effective_chat.id

    if(database.isAuthorised(str(chat_id))):
        await update.message.reply_text("You are authorised !")
        await context.bot.send_message(chat_id = chat_id, text = "Your messages will be anonymously broadcasted to all the users")

    else:
        await update.message.reply_text("You are not authorised ! Please contact the admin")

async def broadcast(update: Update ,context)-> None:
    if(database.isAuthorised(str(update.effective_chat.id))):

        verified_chat_id = str(update.effective_chat.id)
        users = database.getAllUsers()
        
        refined_user_list = []

        for user in users:
            if(user[0] != verified_chat_id):
                refined_user_list.append(user[0])

        for user in refined_user_list:
            await context.bot.copy_message(chat_id = user,from_chat_id = update.effective_chat.id,message_id = update.message.message_id )

def initialize_bot():
    TOKEN = os.getenv("TOKEN")

    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.ALL, broadcast))

    return application

def start_bot(application, loop):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(application.run_polling())

def console() -> None:
    help_message = '''?list-all : List all the users \n?authorise chat_id : Authorise a chat_id \n?deauthorise chat_id : Deauthorise a chat_id \n?help : Commands list'''
    
    print("-------BOT CONSOLE ACTIVE---------")
    print(help_message)

    while True:
        command = str(input()).strip()

        if command == "?help" or command == "?commands":
            print(help_message)
        elif command == "?list-all":
            print(database.getAllUsers())
        elif command.startswith("?authorise"):
            chat_id = command.split(" ")[1]
            database.addAuthorisedUser(chat_id)
        elif command.startswith("?deauthorise"):
            chat_id = command.split(" ")[1]
            database.removeAuthorisedUser(chat_id)    
        else:
            print("Invalid command! Type ?help for list of commands")

if __name__ == '__main__':
    application = initialize_bot()
    loop = asyncio.new_event_loop()
    
    thread1 = threading.Thread(target=start_bot, args=(application, loop))
    thread2 = threading.Thread(target=console)
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()