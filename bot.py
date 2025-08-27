from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8278087886:AAEjFOAX1Ee1VskHUQypGl0yFFwHq75rCcw"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Hii im working")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
