from telegram.ext import Updater, CommandHandler
import json
import os

# ====== BOT CONFIG ======
TOKEN = "8752770532:AAGi9BiJc1YPuDGDnC2Q0P85Q8dmY-ESk7E"
ADMIN_USERNAME = "ADITYA"     # without @
GUILD_NAME = "UNIQUE GMR"
DATA_FILE = "guild_data.json"
# ========================

# Load saved data
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        guild_data = json.load(f)
else:
    guild_data = {}

def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(guild_data, f)

def start(update, context):
    update.message.reply_text(
        f"🔥 {GUILD_NAME} GLORY BOT 🔥\n\n"
        "Commands:\n"
        "/add Name Glory\n"
        "/list\n"
        "/rank\n\n"
        f"👑 Admin: {ADMIN_USERNAME}"
    )

def add(update, context):
    user = update.message.from_user.username

    if user != ADMIN_USERNAME:
        update.message.reply_text("❌ Sirf Admin glory add kar sakta hai")
        return

    try:
        name = context.args[0]
        glory = int(context.args[1])

        guild_data[name] = guild_data.get(name, 0) + glory
        save_data()

        update.message.reply_text(
            f"✅ {name} ke {glory} glory add ho gaye 🔥\n"
            f"🏆 Total Glory: {guild_data[name]}"
        )
    except:
        update.message.reply_text(
            "❌ Galat format\n"
            "Example: /add Aman 120"
        )

def list_members(update, context):
    if not guild_data:
        update.message.reply_text("⚠️ Guild me abhi koi data nahi hai")
        return

    text = f"📋 {GUILD_NAME} MEMBERS:\n\n"
    for name, glory in guild_data.items():
        text += f"• {name} : {glory}\n"

    update.message.reply_text(text)

def rank(update, context):
    if not guild_data:
        update.message.reply_text("⚠️ Ranking available nahi hai")
        return

    sorted_data = sorted(
        guild_data.items(),
        key=lambda x: x[1],
        reverse=True
    )

    text = f"🏆 {GUILD_NAME} GLORY RANKING 🏆\n\n"
    for i, (name, glory) in enumerate(sorted_data, start=1):
        text += f"{i}. {name} — {glory}\n"

    update.message.reply_text(text)

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("add", add))
dp.add_handler(CommandHandler("list", list_members))
dp.add_handler(CommandHandler("rank", rank))

updater.start_polling()
print("Bot is running...")
updater.idle()