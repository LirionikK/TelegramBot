import logging

from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler

TOKEN_BOT = "6816954307:AAEOezMsXyl_Wtzn39t9Q4fH-gVg-EoR7dQ"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Welcome")


def run():
    app = ApplicationBuilder().token(TOKEN_BOT).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", start))

    app.run_polling()


if __name__ == "__main__":
    run()
