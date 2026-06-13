# MADE BY AGAJAYOFFICIAL IF YOU CHANGE CREDIT SO ..☠️
import telebot
import requests
import threading
import time

TOKEN = "YOUR_BOT_TOKEN"
bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

API_URL = "YOUR_LIKE_API"
# 🔄 ANIMATION
def animate(chat_id, msg_id, stop):
    texts = [
        "⚡ Connecting to Server",
        "📡 Sending Likes",
        "🚀 Boosting Profile"
    ]
    i = 0

    while not stop["stop"]:
        text = texts[i % len(texts)]
        dots = "." * (i % 4)

        try:
            bot.edit_message_text(
                f"⏳ {text}{dots}",
                chat_id,
                msg_id
            )
        except:
            pass

        time.sleep(0.6)
        i += 1

# ▶️ START
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "<b>✅ Bot Activated!\nUse: /like <region> <uid></b>")

# ❤️ LIKE COMMAND
@bot.message_handler(commands=['like'])
def like_cmd(message):

    # ❌ PRIVATE BLOCK
    if message.chat.type == "private":
        bot.reply_to(message, "<b>❌ Use this bot in group</b>")
        return

    parts = message.text.split()
    if len(parts) != 3:
        bot.reply_to(message, "<b>❌ Use: /like <region> <uid></b>")
        return

    region = parts[1]
    uid = parts[2]

    msg = bot.reply_to(message, "🚀 Initializing Like System...")

    # 🔄 START ANIMATION
    stop = {"stop": False}
    t = threading.Thread(target=animate, args=(message.chat.id, msg.message_id, stop))
    t.start()

    try:
        url = f"{API_URL}?uid={uid}&server_name={region}&key=AJAY"
        response = requests.get(url, timeout=15)

        if response.status_code != 200:
            stop["stop"] = True
            bot.edit_message_text("❌ Server Not Responding", message.chat.id, msg.message_id)
            return

        res = response.json()

        # 🛑 STOP ANIMATION
        stop["stop"] = True
        t.join()

        if "error" in res:
            bot.edit_message_text("❌ Invalid UID or Region", message.chat.id, msg.message_id)
            return

        likes = res.get("LikesGivenByAPI", 0)
        name = res.get("PlayerNickname", "Unknown")
        before = res.get("LikesbeforeCommand", 0)
        after = res.get("LikesafterCommand", 0)
        remain = res.get("remains", "0/0")

        # ⚠️ MAX LIKES
        if likes == 0:
            bot.edit_message_text(
                f"<b>⚠️ Like Limit Reached</b>\n\n"
                f"🎮 <b>Player:</b> <code>{name}</code>\n"
                f"🆔 <b>UID:</b> <code>{uid}</code>\n"
                f"🌍 <b>Region:</b> <code>{region.upper()}</code>\n"
                f"📊 <b>Before:</b> <code>{before}</code>\n"
                f"📊 <b>After:</b> <code>{after}</code>\n"
                f"🚫 <b>Likes Given:</b> <code>{likes}</code>\n"
                f"📦 <b>Remaining:</b> <code>{remain}</code>",
                message.chat.id,
                msg.message_id
            )
            return

        # ✅ SUCCESS
        bot.edit_message_text(
            f"<b>🎉 Likes Delivered Successfully</b>\n\n"
            f"🎮 <b>Player:</b> <code>{name}</code>\n"
            f"🆔 <b>UID:</b> <code>{uid}</code>\n"
            f"🌍 <b>Region:</b> <code>{region.upper()}</code>\n"
            f"📈 <b>Before:</b> <code>{before}</code>\n"
            f"📈 <b>After:</b> <code>{after}</code>\n"
            f"🔥 <b>Likes Added:</b> <code>{likes}</code>\n"
            f"📦 <b>Remaining:</b> <code>{remain}</code>",
            message.chat.id,
            msg.message_id
        )

    except requests.exceptions.Timeout:
        stop["stop"] = True
        bot.edit_message_text("⏱️ Request Timeout", message.chat.id, msg.message_id)

    except Exception:
        stop["stop"] = True
        bot.edit_message_text("❌ Server Error", message.chat.id, msg.message_id)

print("🔥 Bot Running...")
bot.infinity_polling()

# MADE BY AGAJAYOFFICIAL 