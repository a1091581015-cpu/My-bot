import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("هلا ابو سهم ✅ البوت شغال")

def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        print("BOT_TOKEN missing")
        return
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot started")
    app.run_polling()

if __name__ == "__main__":
    main()
