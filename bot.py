import json
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN =8690968861:AAFn4QPIy0Y0ZEd4_Cb5esFWiTaBydRKxxE

def load_database():
    with open("database.json", "r") as file:
        return json.load(file)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("⚽ Today's Predictions", callback_data="today")],
        [InlineKeyboardButton("🔥 VIP Predictions", callback_data="vip")],
        [InlineKeyboardButton("📊 Results", callback_data="results")],
        [InlineKeyboardButton("👤 My Account", callback_data="account")],
        [InlineKeyboardButton("ℹ️ About Bot", callback_data="about")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "⚽ Welcome to Football Prediction Bot\n\nChoose an option below:",
        reply_markup=reply_markup
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    db = load_database()

    if query.data == "today":
        predictions = db.get("today_predictions", "No predictions available yet.")
        await query.edit_message_text(
            f"⚽ Today's Predictions:\n\n{predictions}"
        )

    elif query.data == "vip":
        vip = db.get("vip_predictions", "VIP predictions are locked.")
        await query.edit_message_text(
            f"🔥 VIP Predictions:\n\n{vip}"
        )

    elif query.data == "results":
        results = db.get("results", "No results available.")
        await query.edit_message_text(
            f"📊 Results:\n\n{results}"
        )

    elif query.data == "account":
        await query.edit_message_text(
            "👤 Account\n\nYour profile will appear here."
        )

    elif query.data == "about":
        await query.edit_message_text(
            "ℹ️ Football Prediction Bot\n\nDaily football tips and analysis."
        )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
