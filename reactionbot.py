import os
from typing import Final 
from telegram import Update, ReactionTypeEmoji 
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


TOKEN: Final = '7798982807:AAEdqS-vwwDM5k5wgKfDPhKvSEPc-0XKI6s'
USERNAME: Final ='7798982807:AAEdqS-vwwDM5k5wgKfDPhKvSEPc-0XKI6s'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me a message and I'll react to it! 😊")

async def react_to_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    chat_id = message.chat_id
    message_id = message.message_id

    # Choose reaction emojis (Telegram supports: 👍, 👎, ❤, 🔥, 🎉, 😁, 🤔, 😢)
    reactions = [
        ReactionTypeEmoji(emoji="👍"),
        ReactionTypeEmoji(emoji="❤")
    ]

    # Add reactions to the message
    await context.bot.set_message_reaction(
        chat_id=chat_id,
        message_id=message_id,
        reaction=reactions,
        is_big=False
    )

async def react_to_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    text = message.text.lower()
    
    if "hii" in text:
        reaction = [ReactionTypeEmoji(emoji="❤️")]
    if "Hii" in text:
        reaction = [ReactionTypeEmoji(emoji="❤️")]
    if "hi" in text:
        reaction = [ReactionTypeEmoji(emoji="❤️")]
    elif "sad" in text:
        reaction = [ReactionTypeEmoji(emoji="😢")]
    if "need" in text:
       reaction = [ReactionTypeEmoji(emoji="👎")]
    else: 
        reaction = [ReactionTypeEmoji(emoji="🤔")]
    
    await context.bot.set_message_reaction(
        chat_id=message.chat_id,
        message_id=message.message_id,
        reaction=reaction,
        is_big=False
    )
if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    
    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, react_to_message))
    
    print("Bot is running...")
    app.run_polling()