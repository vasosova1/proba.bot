from telegram.ext import Updater, MessageHandler, Filters
from telegram import Update
from telegram.ext.callbackcontext import CallbackContext

# Tvoj bot token
TOKEN = "7565127463:AAHGF-BHhQAXMH59KOKGpW1Vzut7e5GhGfQ"

def handle_message(update: Update, context: CallbackContext):
    user = update.effective_user
    name = user.first_name.lower() if user.first_name else ""
    username = user.username.lower() if user.username else ""

    print(f"👤 Poruku poslao: {user.first_name} (@{user.username})")

    if "nedjo" in name or "nedjo" in username:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            reply_to_message_id=update.message.message_id,
            text="/gurtna_oralni_rob"
        )

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    # Ovo hvata sve poruke
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    print("🤖 Bot je pokrenut i čeka poruke...")
    updater.idle()

if __name__ == "__main__":
    main()
