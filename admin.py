from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from config import ADMIN_ID
from database import load_data, save_data


def is_admin(user_id):
    return user_id == ADMIN_ID


async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("❌ You are not authorized.")
        return

    await update.message.reply_text(
        "👑 Admin Panel\n\n"
        "/setfree <prediction>\n"
        "/setvip <prediction>\n"
        "/setresult <result>\n"
        "/addvip <user_id>\n"
        "/removevip <user_id>"
    )


async def setfree(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        return

    text = " ".join(context.args)
    data = load_data()
    data["free_prediction"] = text
    save_data(data)
    await update.message.reply_text("✅ Free prediction updated.")


async def setvip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        return

    text = " ".join(context.args)
    data = load_data()
    data["vip_prediction"] = text
    save_data(data)
    await update.message.reply_text("✅ VIP prediction updated.")


async def setresult(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        return

    text = " ".join(context.args)
    data = load_data()
    data["results"] = text
    save_data(data)
    await update.message.reply_text("✅ Results updated.")
