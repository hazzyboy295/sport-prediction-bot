from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

from database import load_data, save_data


MENU = [
    ["⚽ Free Prediction", "🔒 VIP Prediction"],
    ["✅ Results"],
    ["📢 Join Channel", "👤 Contact Admin"]
]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = load_data()

    user_id = update.effective_user.id

    if user_id not in data["users"]:
        data["users"].append(user_id)
        save_data(data)

    await update.message.reply_text(
        "🏆 Welcome to Sport Prediction!\n\n"
        "Choose an option below:",
        reply_markup=ReplyKeyboardMarkup(
            MENU,
            resize_keyboard=True
        )
    )


async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = load_data()
    text = update.message.text
    user_id = update.effective_user.id

    if text == "⚽ Free Prediction":
        await update.message.reply_text(data["free_prediction"])

    elif text == "🔒 VIP Prediction":
        if user_id in data["vip_users"]:
            await update.message.reply_text(data["vip_prediction"])
        else:
            await update.message.reply_text(
                "🔒 This prediction is for VIP members only.\n"
                "Contact the admin to get VIP access."
            )

    elif text == "✅ Results":
        await update.message.reply_text(data["results"])

    elif text == "📢 Join Channel":
        await update.message.reply_text(
            "Channel link will be added later."
        )

    elif text == "👤 Contact Admin":
        await update.message.reply_text(
            "Admin username will be added later."
  )
