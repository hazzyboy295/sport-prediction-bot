from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

from config import BOT_TOKEN
from handlers import start, handle_buttons
from admin import (
    admin,
    setfree,
    setvip,
    setresult,
    addvip,
    removevip,
    broadcast,
)


def main():
    if not BOT_TOKEN:
        raise ValueError(
            "BOT_TOKEN is missing. Set it in Railway Variables."
        )

    app = Application.builder().token(BOT_TOKEN).build()

    # User commands
    app.add_handler(CommandHandler("start", start))

    # Admin commands
    app.add_handler(CommandHandler("admin", admin))
    app.add_handler(CommandHandler("setfree", setfree))
    app.add_handler(CommandHandler("setvip", setvip))
    app.add_handler(CommandHandler("setresult", setresult))
    app.add_handler(CommandHandler("addvip", addvip))
    app.add_handler(CommandHandler("removevip", removevip))
    app.add_handler(CommandHandler("broadcast", broadcast))

    # Menu buttons
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handle_buttons,
        )
    )

    print("✅ Sport Prediction Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()
