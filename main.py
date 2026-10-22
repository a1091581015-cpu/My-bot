import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# التوكن - حطه هنا او في Render كـ Environment Variable
TOKEN = os.getenv("BOT_TOKEN") or "PUT_YOUR_TOKEN_HERE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلا! البوت شغال الآن ✅\nأرسل /start")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("كيف أقدر أساعدك؟")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    print("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
