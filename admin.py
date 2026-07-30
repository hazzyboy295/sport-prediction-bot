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
async def addvip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        return

    if len(context.args) != 1:
        await update.message.reply_text("Usage: /addvip <user_id>")
        return

    try:
        user_id = int(context.args[0])
    except ValueError:
        await update.message.reply_text("Invalid user ID.")
        return

    data = load_data()

    if user_id not in data["vip_users"]:
        data["vip_users"].append(user_id)
        save_data(data)

    await update.message.reply_text("✅ VIP user added.")


async def removevip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        return

    if len(context.args) != 1:
        await update.message.reply_text("Usage: /removevip <user_id>")
        return

    try:
        user_id = int(context.args[0])
    except ValueError:
        await update.message.reply_text("Invalid user ID.")
        return

    data = load_data()

    if user_id in data["vip_users"]:
        data["vip_users"].remove(user_id)
        save_data(data)

    await update.message.reply_text("✅ VIP user removed.")
