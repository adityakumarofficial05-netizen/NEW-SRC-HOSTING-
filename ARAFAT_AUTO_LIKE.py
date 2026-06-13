# bot_premium.py
# CREDIT: @arafat_codex1
# JO CREDIT CHANGE KAROGE O MERA BACCHA HAIN

import os
import json
import requests
import httpx
import aiohttp
from datetime import datetime
from io import BytesIO
from html import escape
from typing import Dict, List, Optional

from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update, User
from telegram.constants import ChatType
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    CallbackQueryHandler,
    MessageHandler,
    filters,
)

# ---------------- CONFIG ----------------
BOT_TOKEN = "YOUR_BOT_TOKEN"

API_VISIT_BASE = "YOUR_VISIT_API"
API_LIKE_BASE = "YOUR_LIKE_API"
SPAM_API = "https://arafat-spam-api.vercel.app"
INFO_API = "https://mafuuuu-info-api.vercel.app/mafu-info?uid={uid}"
ULTRA_API_URL = "https://checkregion-api.vercel.app/region?uid={uid}"

ALLOWED_GROUP_ID = -1003986145954

OWNER_USERNAME = "@ARAFAT_CODEX1"
OWNER_USER_ID = 7705767559
ADMIN_USERNAME = "@Mobin_codex"
ADMIN_USER_ID = 8669516794

ADMINS = [7705767559, 8669516794]

VIP_FILE = "vip_users.json"
AUTO_TASKS_FILE = "auto_tasks.json"
STATS_FILE = "bot_stats.json"

# Premium themes and emojis
class PremiumTheme:
    MAIN_EMOJI = "🔥"
    SUCCESS_EMOJI = "✅"
    ERROR_EMOJI = "❌"
    WARNING_EMOJI = "⚠️"
    PROCESS_EMOJI = "⏳"
    BOT_EMOJI = "🤖"
    CROWN_EMOJI = "👑"
    STAR_EMOJI = "⭐"
    ROCKET_EMOJI = "🚀"
    SHIELD_EMOJI = "🛡️"
    LIGHTNING_EMOJI = "⚡"
    DIAMOND_EMOJI = "💎"
    SUPPORT_EMOJI = "🎧"
    INFO_EMOJI = "ℹ️"
    HELP_EMOJI = "🆘"

THEME = PremiumTheme()

# ---------------- file persistence ----------------
def load_json_file(path, default=None):
    if not os.path.exists(path):
        return default or []
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default or []

def save_json_file(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# ================== VIP STORAGE ==================
def load_vips():
    data = load_json_file(VIP_FILE, [])
    return set(int(x) for x in data if x)

def save_vips(data):
    save_json_file(VIP_FILE, list(data))

vip_users = load_vips()

# ================== STATS STORAGE ==================
def load_stats():
    return load_json_file(STATS_FILE, {
        "total_likes": 0,
        "total_visits": 0,
        "total_spams": 0,
        "total_info_requests": 0,
        "commands_used": {},
        "last_restart": datetime.now().isoformat()
    })

def save_stats(stats):
    save_json_file(STATS_FILE, stats)

stats = load_stats()

def update_stats(command_name: str, action_type: str = None):
    stats["commands_used"][command_name] = stats["commands_used"].get(command_name, 0) + 1
    if action_type == "like":
        stats["total_likes"] += 1
    elif action_type == "visit":
        stats["total_visits"] += 1
    elif action_type == "spam":
        stats["total_spams"] += 1
    elif action_type == "info":
        stats["total_info_requests"] += 1
    save_stats(stats)

def is_owner(user: User) -> bool:
    return user.id == OWNER_USER_ID

def is_admin(user: User) -> bool:
    return user.id in ADMINS

def is_vip(user: User) -> bool:
    if is_owner(user) or is_admin(user):
        return True
    return user.id in vip_users

# ---------------------- Helper Functions ----------------------
def create_fancy_header(title: str) -> str:
    return f"╔════════════════════════════════════════════════╗\n║  {THEME.BOT_EMOJI} <b>{title}</b>"

def create_fancy_footer() -> str:
    return f"╠════════════════════════════════════════════════╣\n║  {THEME.CROWN_EMOJI} 𝐎𝐖𝐍𝐄𝐑: {OWNER_USERNAME}\n║  {THEME.SHIELD_EMOJI} 𝐀𝐃𝐌𝐈𝐍: {ADMIN_USERNAME}\n║  {THEME.SUPPORT_EMOJI} 𝐒𝐔𝐏𝐏𝐎𝐑𝐓: @ARAFAT_LIKE_GROUP\n╚════════════════════════════════════════════════╝"

# ---------------------- WELCOME MESSAGE ----------------------
async def welcome_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        if member.id == context.bot.id:
            welcome_text = f"""
╔════════════════════════════════════════════════╗
║     {THEME.ROCKET_EMOJI} 𝐀𝐔𝐓𝐎 𝐋𝐈𝐊𝐄 & 𝐕𝐈𝐒𝐈𝐓 𝐁𝐎𝐓 {THEME.ROCKET_EMOJI}      ║
╠════════════════════════════════════════════════╣
║                                                 ║
║   {THEME.SUCCESS_EMOJI} <b>𝐁𝐎𝐓 𝐀𝐂𝐓𝐈𝐕𝐀𝐓𝐄𝐃 𝐒𝐔𝐂𝐂𝐄𝐒𝐒𝐅𝐔𝐋𝐋𝐘</b>   ║
║                                                 ║
╠════════════════════════════════════════════════╣
║  {THEME.DIAMOND_EMOJI} <b>𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐅𝐄𝐀𝐓𝐔𝐑𝐄𝐒</b>              ║
║                                                 ║
║  {THEME.LIGHTNING_EMOJI} ✓ <b>Auto Like Sender</b>          ║
║  {THEME.LIGHTNING_EMOJI} ✓ <b>Auto Visit Sender</b>         ║
║  {THEME.LIGHTNING_EMOJI} ✓ <b>VIP Access System</b>         ║
║  {THEME.LIGHTNING_EMOJI} ✓ <b>Spam Protection</b>           ║
║  {THEME.LIGHTNING_EMOJI} ✓ <b>Player Info Checker</b>       ║
║  {THEME.LIGHTNING_EMOJI} ✓ <b>Auto Task Scheduler</b>       ║
║                                                 ║
╠════════════════════════════════════════════════╣
║  {THEME.CROWN_EMOJI} <b>𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒</b>                       ║
║                                                 ║
║  <code>/start</code>     → Show All Commands    ║
║  <code>/like</code>      → Send Like           ║
║  <code>/visit</code>     → Send Visit          ║
║  <code>/info</code>      → Player Info         ║
║  <code>/region</code>    → Check Region        ║
║  <code>/spam</code>      → Spam Request        ║
║                                                 ║
{create_fancy_footer()}

{THEME.STAR_EMOJI} <i>Thanks for adding me! Contact {OWNER_USERNAME} for VIP upgrade</i>
"""
            await update.message.reply_text(welcome_text, parse_mode="HTML")
        
        elif not member.is_bot:
            welcome_msg = f"""
╔════════════════════════════════════════════════╗
║     {THEME.STAR_EMOJI} 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 {THEME.STAR_EMOJI}      ║
╠════════════════════════════════════════════════╣
║                                                 ║
║      {THEME.BOT_EMOJI} <b>𝐖𝐄𝐋𝐂𝐎𝐌𝐄 {member.first_name}!</b>      ║
║                                                 ║
║   {THEME.DIAMOND_EMOJI} <b>ᴠɪᴘ ᴜꜱᴇʀꜱ ɢᴇᴛ ᴘʀᴇᴍɪᴜᴍ ᴀᴄᴄᴇꜱꜱ</b>   ║
║                                                 ║
╠════════════════════════════════════════════════╣
║  {THEME.LIGHTNING_EMOJI} <b>𝐐𝐔𝐈𝐂𝐊 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒</b>                 ║
║                                                 ║
║  🔥 <code>/like ind 6283999318</code>  → Send Like     ║
║  🚀 <code>/visit bd 2452759873</code> → Send Visit    ║
║  ℹ️ <code>/info 6283999318</code>    → Get Info      ║
║  🌍 <code>/region 6283999318</code>  → Check Region  ║
║                                                 ║
{create_fancy_footer()}

{THEME.ROCKET_EMOJI} <i>Enjoy unlimited likes & visits! Contact {OWNER_USERNAME} for support</i>
"""
            await update.message.reply_text(welcome_msg, parse_mode="HTML")

# ---------------------- HELP COMMAND ----------------------
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    is_premium = is_vip(user)
    
    help_text = f"""
╔════════════════════════════════════════════════╗
║     {THEME.HELP_EMOJI} 𝐇𝐄𝐋𝐏 & 𝐆𝐔𝐈𝐃𝐄 {THEME.HELP_EMOJI}             ║
╠════════════════════════════════════════════════╣
║                                                 ║
║  {THEME.STAR_EMOJI} <b>𝐇𝐎𝐖 𝐓𝐎 𝐔𝐒𝐄 𝐓𝐇𝐄 𝐁𝐎𝐓</b>                  ║
║                                                 ║
║  1️⃣ <b>For Like</b>                              ║
║     <code>/like ind 6283999318</code>           ║
║                                                 ║
║  2️⃣ <b>For Visit</b>                             ║
║     <code>/visit bd 2452759873</code>           ║
║                                                 ║
║  3️⃣ <b>Check Player Info</b>                     ║
║     <code>/info 6283999318</code>               ║
║                                                 ║
║  4️⃣ <b>Check Region</b>                          ║
║     <code>/region 6283999318</code>             ║
║                                                 ║
║  5️⃣ <b>Send Spam Request</b>                     ║
║     <code>/spam ind 6283999318</code>           ║
║                                                 ║
╠════════════════════════════════════════════════╣
║  {THEME.DIAMOND_EMOJI} <b>𝐀𝐕𝐀𝐈𝐋𝐀𝐁𝐋𝐄 𝐑𝐄𝐆𝐈𝐎𝐍𝐒</b>              ║
║                                                 ║
║  ind, us, id, ar, eg, ru, br, vn, ph, my, th, tr ║
║                                                 ║
╠════════════════════════════════════════════════╣
║  {THEME.CROWN_EMOJI} <b>𝐕𝐈𝐏 𝐁𝐄𝐍𝐄𝐅𝐈𝐓𝐒</b>                    ║
║                                                 ║
║  ✓ Unlimited Likes & Visits                     ║
║  ✓ Priority Support                            ║
║  ✓ Auto Task Scheduler                         ║
║                                                 ║
{create_fancy_footer()}
"""
    await update.message.reply_text(help_text, parse_mode="HTML")

# ---------------------- ADMIN PANEL ----------------------
async def admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if not (is_owner(user) or is_admin(user)):
        await update.message.reply_text(f"{THEME.ERROR_EMOJI} ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ᴛʜᴇ ᴀᴅᴍɪɴ ᴘᴀɴᴇʟ.")
        return
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(f"{THEME.CROWN_EMOJI} VIP Management", callback_data="admin_vip")],
        [InlineKeyboardButton(f"{THEME.ROCKET_EMOJI} Auto Tasks", callback_data="admin_auto")],
        [InlineKeyboardButton(f"{THEME.STAR_EMOJI} Bot Stats", callback_data="admin_stats")],
        [InlineKeyboardButton(f"{THEME.SHIELD_EMOJI} Broadcast", callback_data="admin_broadcast")],
        [InlineKeyboardButton("❌ Close", callback_data="admin_close")],
    ])
    
    panel_text = f"""
╔════════════════════════════════════════════════╗
║  {THEME.CROWN_EMOJI} <b>𝐀𝐃𝐌𝐈𝐍 𝐂𝐎𝐍𝐓𝐑𝐎𝐋 𝐏𝐀𝐍𝐄𝐋</b> {THEME.CROWN_EMOJI}   ║
╠════════════════════════════════════════════════╣
║                                                 ║
║  {THEME.BOT_EMOJI} <b>ᴡᴇʟᴄᴏᴍᴇ ᴀᴅᴍɪɴ</b>                     ║
║                                                 ║
║  {THEME.DIAMOND_EMOJI} ᴛᴏᴛᴀʟ ᴠɪᴘ ᴜꜱᴇʀꜱ: {len(vip_users)}        ║
║  {THEME.ROCKET_EMOJI} ᴀᴄᴛɪᴠᴇ ᴛᴀꜱᴋꜱ: {len(load_auto_tasks())}   ║
║  {THEME.LIGHTNING_EMOJI} ᴛᴏᴛᴀʟ ʟɪᴋᴇꜱ: {stats['total_likes']}       ║
║  {THEME.STAR_EMOJI} ᴛᴏᴛᴀʟ ᴠɪꜱɪᴛꜱ: {stats['total_visits']}      ║
║                                                 ║
{create_fancy_footer()}
"""
    await update.message.reply_text(panel_text, parse_mode="HTML", reply_markup=keyboard)

async def admin_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user = update.effective_user
    
    if not (is_owner(user) or is_admin(user)):
        await query.edit_message_text(f"{THEME.ERROR_EMOJI} ᴜɴᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴀᴄᴄᴇꜱꜱ.")
        return
    
    data = query.data
    
    if data == "admin_vip":
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("➕ Add VIP", callback_data="vip_add"), 
             InlineKeyboardButton("➖ Remove VIP", callback_data="vip_remove")],
            [InlineKeyboardButton("📋 List VIPs", callback_data="vip_list")],
            [InlineKeyboardButton("🔙 Back", callback_data="admin_back")],
        ])
        await query.edit_message_text(f"{THEME.CROWN_EMOJI} <b>VIP Management Panel</b>\n\nUse the buttons below to manage VIP users.", parse_mode="HTML", reply_markup=keyboard)
    
    elif data == "admin_auto":
        tasks = load_auto_tasks()
        if not tasks:
            tasks_text = "❌ ɴᴏ ᴀᴄᴛɪᴠᴇ ᴀᴜᴛᴏ ᴛᴀꜱᴋꜱ."
        else:
            tasks_text = "<b>📋 Active Auto Tasks:</b>\n\n"
            for t in tasks[:10]:
                tasks_text += f"• {t.get('type')} | UID: {t.get('uid')} | Left: {t.get('remaining_runs')}\n"
        
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("➕ New Auto-Like", callback_data="auto_like"),
             InlineKeyboardButton("🆕 New Auto-Visit", callback_data="auto_visit")],
            [InlineKeyboardButton("🗑 Cancel by UID", callback_data="auto_cancel")],
            [InlineKeyboardButton("🔙 Back", callback_data="admin_back")],
        ])
        await query.edit_message_text(f"{THEME.ROCKET_EMOJI} <b>Auto Tasks Manager</b>\n\n{tasks_text}", parse_mode="HTML", reply_markup=keyboard)
    
    elif data == "admin_stats":
        stats_text = f"""
╔════════════════════════════════════════════════╗
║  {THEME.STAR_EMOJI} <b>𝐁𝐎𝐓 𝐒𝐓𝐀𝐓𝐈𝐒𝐓𝐈𝐂𝐒</b> {THEME.STAR_EMOJI}            ║
╠════════════════════════════════════════════════╣
║                                                 ║
║  {THEME.LIGHTNING_EMOJI} <b>ᴛᴏᴛᴀʟ ʟɪᴋᴇꜱ:</b> {stats['total_likes']}         ║
║  {THEME.ROCKET_EMOJI} <b>ᴛᴏᴛᴀʟ ᴠɪꜱɪᴛꜱ:</b> {stats['total_visits']}        ║
║  {THEME.BOT_EMOJI} <b>ᴛᴏᴛᴀʟ ꜱᴘᴀᴍꜱ:</b> {stats['total_spams']}         ║
║  {THEME.DIAMOND_EMOJI} <b>ɪɴꜰᴏ ʀᴇQᴜᴇꜱᴛꜱ:</b> {stats['total_info_requests']}   ║
║                                                 ║
║  <b>📊 ᴄᴏᴍᴍᴀɴᴅ ᴜꜱᴀɢᴇ:</b>                                 ║
"""
        for cmd, count in list(stats["commands_used"].items())[:10]:
            stats_text += f"║   • /{cmd}: {count}\n"
        stats_text += f"\n{create_fancy_footer()}"
        
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="admin_back")]])
        await query.edit_message_text(stats_text, parse_mode="HTML", reply_markup=keyboard)
    
    elif data == "admin_broadcast":
        context.user_data["broadcast_mode"] = True
        await query.edit_message_text(f"{THEME.SHIELD_EMOJI} <b>Broadcast Mode Active</b>\n\nSend me the message you want to broadcast to all VIP users.\n\nType /cancel to exit broadcast mode.", parse_mode="HTML")
    
    elif data == "admin_back":
        await admin_panel(update, context)
    
    elif data == "admin_close":
        await query.edit_message_text(f"{THEME.SUCCESS_EMOJI} ᴀᴅᴍɪɴ ᴘᴀɴᴇʟ ᴄʟᴏꜱᴇᴅ.")
    
    elif data == "vip_add":
        context.user_data["awaiting_vip_add"] = True
        await query.edit_message_text(f"{THEME.SUCCESS_EMOJI} <b>Add VIP User</b>\n\nSend me the Telegram User ID to add as VIP.\n\nType /cancel to cancel.", parse_mode="HTML")
    
    elif data == "vip_remove":
        context.user_data["awaiting_vip_remove"] = True
        await query.edit_message_text(f"{THEME.WARNING_EMOJI} <b>Remove VIP User</b>\n\nSend me the Telegram User ID to remove from VIP.\n\nType /cancel to cancel.", parse_mode="HTML")
    
    elif data == "vip_list":
        if not vip_users:
            await query.edit_message_text(f"{THEME.ERROR_EMOJI} ɴᴏ ᴠɪᴘ ᴜꜱᴇʀꜱ ꜰᴏᴜɴᴅ.")
            return
        msg = f"{THEME.CROWN_EMOJI} <b>VIP Users List</b>\n\n"
        for uid in vip_users:
            msg += f"• <code>{uid}</code>\n"
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="admin_vip")]])
        await query.edit_message_text(msg, parse_mode="HTML", reply_markup=keyboard)
    
    elif data == "auto_like":
        context.user_data["awaiting_auto_like"] = True
        await query.edit_message_text(f"{THEME.SUCCESS_EMOJI} <b>Schedule Auto-Like</b>\n\nSend in format: <code>region uid days</code>\nExample: <code>ind 6283999318 7</code>\n\nType /cancel to cancel.", parse_mode="HTML")
    
    elif data == "auto_visit":
        context.user_data["awaiting_auto_visit"] = True
        await query.edit_message_text(f"{THEME.SUCCESS_EMOJI} <b>Schedule Auto-Visit</b>\n\nSend in format: <code>region uid days</code>\nExample: <code>ind 6283999318 7</code>\n\nType /cancel to cancel.", parse_mode="HTML")
    
    elif data == "auto_cancel":
        context.user_data["awaiting_auto_cancel"] = True
        await query.edit_message_text(f"{THEME.WARNING_EMOJI} <b>Cancel Auto Task</b>\n\nSend the UID to cancel all auto tasks for.\n\nType /cancel to cancel.", parse_mode="HTML")

# ---------------------- START COMMAND ----------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    is_premium = is_vip(user)
    
    status_emoji = THEME.DIAMOND_EMOJI if is_premium else "🟢"
    status_text = "✨ ᴘʀᴇᴍɪᴜᴍ ᴠɪᴘ ᴜꜱᴇʀ ✨" if is_premium else "🆓 ꜰʀᴇᴇ ᴜꜱᴇʀ"
    
    msg = f"""
╔════════════════════════════════════════════════╗
║     {THEME.ROCKET_EMOJI} 𝐀𝐔𝐓𝐎 𝐋𝐈𝐊𝐄 & 𝐕𝐈𝐒𝐈𝐓 𝐁𝐎𝐓 {THEME.ROCKET_EMOJI}        ║
╠════════════════════════════════════════════════╣
║                                                 ║
║      {THEME.BOT_EMOJI} <b>𝐇𝐄𝐋𝐋𝐎 {user.first_name}!</b>          ║
║                                                 ║
║      {status_emoji} <b>𝐒𝐓𝐀𝐓𝐔𝐒</b> : {status_text}          ║
║                                                 ║
╠════════════════════════════════════════════════╣
║  {THEME.DIAMOND_EMOJI} <b>𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒</b> (VIP Only)      ║
║                                                 ║
║  🔥 <code>/like [region] [uid]</code>    → Send Like      ║
║  🚀 <code>/visit [region] [uid]</code>   → Send Visit     ║
║                                                 ║
╠════════════════════════════════════════════════╣
║  {THEME.STAR_EMOJI} <b>𝐅𝐑𝐄𝐄 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒</b> (Everyone)          ║
║                                                 ║
║  ℹ️ <code>/info [uid]</code>        → Player Info     ║
║  🌍 <code>/region [uid]</code>      → Check Region    ║
║  💀 <code>/spam [region] [uid]</code> → Spam Request    ║
║  🆘 <code>/help</code>             → Help Guide      ║
║                                                 ║
╠════════════════════════════════════════════════╣
║  {THEME.CROWN_EMOJI} <b>𝐀𝐃𝐌𝐈𝐍 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒</b>                  ║
║                                                 ║
║  👑 <code>/admin</code>           → Admin Panel     ║
║  ➕ <code>/addvip [id]</code>     → Add VIP User    ║
║  ➖ <code>/removevip [id]</code>  → Remove VIP User ║
║  📋 <code>/listvip</code>         → List VIP Users  ║
║                                                 ║
{create_fancy_footer()}

{THEME.SUCCESS_EMOJI} <i>Type /help for detailed guide or contact {OWNER_USERNAME} for VIP upgrade!</i>
"""
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(f"{THEME.DIAMOND_EMOJI} ɢᴇᴛ ᴠɪᴘ", callback_data="premium_features"),
         InlineKeyboardButton(f"{THEME.SUPPORT_EMOJI} ꜱᴜᴘᴘᴏʀᴛ", url="https://t.me/ARAFAT_LIKE_GROUP")],
        [InlineKeyboardButton(f"{THEME.HELP_EMOJI} ʜᴇʟᴘ", callback_data="help_menu"),
         InlineKeyboardButton(f"{THEME.STAR_EMOJI} ᴏᴡɴᴇʀ", url=f"https://t.me/{OWNER_USERNAME[1:]}")],
    ])
    
    await update.message.reply_text(msg, parse_mode="HTML", reply_markup=keyboard)

# ---------------------- VIP Request Helper ----------------------
def vip_request_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(f"{THEME.DIAMOND_EMOJI} Request VIP", url=f"https://t.me/{OWNER_USERNAME[1:]}")],
        [InlineKeyboardButton(f"{THEME.SUPPORT_EMOJI} Support Group", url="https://t.me/ARAFAT_LIKE_GROUP")],
    ])

# ---------------------- LIKE COMMAND ----------------------
async def like_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await allow_group_only(update):
        return
    
    user = update.effective_user
    if not is_vip(user):
        await update.message.reply_text(
            f"{THEME.ERROR_EMOJI} ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ɪꜱ ꜰᴏʀ ᴘʀᴇᴍɪᴜᴍ ᴠɪᴘ ᴜꜱᴇʀꜱ ᴏɴʟʏ.\n\n{THEME.DIAMOND_EMOJI} ᴜᴘɢʀᴀᴅᴇ ᴛᴏ ᴠɪᴘ ᴛᴏ ᴀᴄᴄᴇꜱꜱ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅꜱ!",
            reply_markup=vip_request_keyboard()
        )
        return
    
    if len(context.args) < 2:
        await update.message.reply_text(
            f"{THEME.WARNING_EMOJI} <b>Usage:</b>\n<code>/like ind 6283999318</code>\n\n<b>Available regions:</b> ind, us, id, ar, eg, ru, br, vn, ph, my, th, tr",
            parse_mode="HTML"
        )
        return
    
    region = context.args[0].lower()
    uid = context.args[1]
    
    processing = await update.message.reply_text(f"{THEME.PROCESS_EMOJI} <b>Processing Like Request...</b>\n\nUID: <code>{uid}</code>\nRegion: <b>{region.upper()}</b>", parse_mode="HTML")
    
    api_url = f"{API_LIKE_BASE}/like?uid={uid}&server_name={region}"
    
    try:
        r = requests.get(api_url, timeout=30).json()
        nickname = r.get("PlayerNickname", "-")
        before = r.get("LikesbeforeCommand", "-")
        after = r.get("LikesafterCommand", "-")
        added = r.get("LikesGivenByAPI", "-")
        status = r.get("status", 0)
        
        update_stats("like", "like")
        
        if status == 1:
            msg = f"""
╔════════════════════════════════════════════════╗
║  {THEME.SUCCESS_EMOJI} <b>𝐋𝐈𝐊𝐄 𝐒𝐄𝐍𝐓 𝐒𝐔𝐂𝐂𝐄𝐒𝐒𝐅𝐔𝐋𝐋𝐘</b> {THEME.SUCCESS_EMOJI}   ║
╠════════════════════════════════════════════════╣
║                                                 ║
║  {THEME.DIAMOND_EMOJI} <b>ᴘʟᴀʏᴇʀ:</b> {nickname}                    ║
║  {THEME.BOT_EMOJI} <b>ᴜɪᴅ:</b> <code>{uid}</code>                       ║
║  {THEME.STAR_EMOJI} <b>ʀᴇɢɪᴏɴ:</b> {region.upper()}                     ║
║                                                 ║
╠════════════════════════════════════════════════╣
║  📊 <b>𝐋𝐈𝐊𝐄 𝐒𝐓𝐀𝐓𝐔𝐒</b>                             ║
║                                                 ║
║  • ʙᴇꜰᴏʀᴇ: {before}                                    ║
║  • ᴀᴅᴅᴇᴅ: +{added}                                     ║
║  • ᴀꜰᴛᴇʀ: {after}                                     ║
║                                                 ║
{create_fancy_footer()}
"""
        else:
            msg = f"""
╔════════════════════════════════════════════════╗
║  {THEME.WARNING_EMOJI} <b>𝐋𝐈𝐊𝐄 𝐀𝐋𝐑𝐄𝐀𝐃𝐘 𝐒𝐄𝐍𝐓</b> {THEME.WARNING_EMOJI}        ║
╠════════════════════════════════════════════════╣
║                                                 ║
║  {THEME.ERROR_EMOJI} <b>ʜᴇʏ {nickname}</b>                        ║
║  {THEME.BOT_EMOJI} ʏᴏᴜ'ᴠᴇ ᴀʟʀᴇᴀᴅʏ ʀᴇᴄᴇɪᴠᴇᴅ ᴀ ʟɪᴋᴇ ᴛᴏᴅᴀʏ!   ║
║                                                 ║
║  {THEME.STAR_EMOJI} ᴛʀʏ ᴀɢᴀɪɴ ᴛᴏᴍᴏʀʀᴏᴡ                        ║
║                                                 ║
{create_fancy_footer()}
"""
        
        await processing.edit_text(msg, parse_mode="HTML")
    except Exception as e:
        await processing.edit_text(f"{THEME.ERROR_EMOJI} <b>API Error:</b>\n<code>{escape(str(e))}</code>\n\nᴘʟᴇᴀꜱᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴀᴛᴇʀ.", parse_mode="HTML")

# ---------------------- VISIT COMMAND ----------------------
async def visit_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await allow_group_only(update):
        return
    
    user = update.effective_user
    if not is_vip(user):
        await update.message.reply_text(f"{THEME.ERROR_EMOJI} ᴘʀᴇᴍɪᴜᴍ ᴄᴏᴍᴍᴀɴᴅ. ᴜᴘɢʀᴀᴅᴇ ᴛᴏ ᴠɪᴘ!", reply_markup=vip_request_keyboard())
        return
    
    if len(context.args) < 2:
        await update.message.reply_text(f"{THEME.WARNING_EMOJI} Usage: <code>/visit bd 2452759873</code>", parse_mode="HTML")
        return
    
    region = context.args[0].lower()
    uid = context.args[1]
    
    processing = await update.message.reply_text(f"{THEME.PROCESS_EMOJI} <b>Processing Visit Request...</b>\n\nUID: <code>{uid}</code>\nRegion: <b>{region.upper()}</b>", parse_mode="HTML")
    
    api_url = f"{API_VISIT_BASE}/{region}/{uid}"
    
    try:
        r = requests.get(api_url, timeout=120).json()
        nickname = r.get("PlayerNickname", "-")
        success = r.get("SuccessfulVisits", 0)
        failed = r.get("FailedVisits", 0)
        total = r.get("TotalVisits", 0)
        credits = r.get("Arafat_codex1")
        
        update_stats("visit", "visit")
        
        msg = f"""
╔════════════════════════════════════════════════╗
║  {THEME.SUCCESS_EMOJI} <b>𝐕𝐈𝐒𝐈𝐓 𝐒𝐄𝐍𝐓 𝐒𝐔𝐂𝐂𝐄𝐒𝐒𝐅𝐔𝐋𝐋𝐘</b> {THEME.SUCCESS_EMOJI}   ║
╠════════════════════════════════════════════════╣
║                                                 ║
║  {THEME.DIAMOND_EMOJI} <b>ᴘʟᴀʏᴇʀ:</b> {nickname}                    ║
║  {THEME.BOT_EMOJI} <b>ᴜɪᴅ:</b> <code>{uid}</code>                       ║
║  {THEME.STAR_EMOJI} <b>ʀᴇɢɪᴏɴ:</b> {region.upper()}                     ║
║                                                 ║
╠════════════════════════════════════════════════╣
║  📊 <b>𝐕𝐈𝐒𝐈𝐓 𝐒𝐓𝐀𝐓𝐔𝐒</b>                             ║
║                                                 ║
║  • {THEME.SUCCESS_EMOJI} ꜱᴜᴄᴄᴇꜱꜱ: {success}                           ║
║  • {THEME.ERROR_EMOJI} ꜰᴀɪʟᴇᴅ: {failed}                            ║
║  • 📨 ᴛᴏᴛᴀʟ: {total}                                    ║
║                                                 ║
║  {THEME.DIAMOND_EMOJI} <b>ᴄʀᴇᴅɪᴛꜱ ʟᴇꜰᴛ:</b> {credits}                 ║
║                                                 ║
{create_fancy_footer()}
"""
        await processing.edit_text(msg, parse_mode="HTML")
    except Exception as e:
        await processing.edit_text(f"{THEME.ERROR_EMOJI} API Error: <code>{e}</code>", parse_mode="HTML")

# ---------------------- INFO COMMAND ----------------------
async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1:
        await update.message.reply_text(f"{THEME.WARNING_EMOJI} Usage: <code>/info 15515555530</code>", parse_mode="HTML")
        return
    
    uid = context.args[0]
    update_stats("info", "info")
    
    processing = await update.message.reply_text(f"{THEME.PROCESS_EMOJI} <b>Fetching Player Info...</b>\n\nUID: <code>{uid}</code>", parse_mode="HTML")
    
    api_url = f"https://ajay-new-all-region-info-api.vercel.app/ajay-info?uid={uid}&key=AJAY"
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(api_url, timeout=20)
            if response.status_code != 200:
                await processing.edit_text(f"{THEME.ERROR_EMOJI} ᴘʟᴀʏᴇʀ ɴᴏᴛ ꜰᴏᴜɴᴅ ᴏʀ ᴀᴘɪ ᴇʀʀᴏʀ")
                return
            
            data = response.json()
            basic = data.get("basicInfo", {})
            
            msg = f"""
╔════════════════════════════════════════════════╗
║  {THEME.DIAMOND_EMOJI} <b>𝐏𝐋𝐀𝐘𝐄𝐑 𝐈𝐍𝐅𝐎𝐑𝐌𝐀𝐓𝐈𝐎𝐍</b> {THEME.DIAMOND_EMOJI}       ║
╠════════════════════════════════════════════════╣
║                                                 ║
║  {THEME.STAR_EMOJI} <b>ɴᴀᴍᴇ:</b> {basic.get('nickname', 'N/A')}                ║
║  {THEME.BOT_EMOJI} <b>ᴜɪᴅ:</b> <code>{basic.get('accountId', uid)}</code>           ║
║  {THEME.SHIELD_EMOJI} <b>ʀᴇɢɪᴏɴ:</b> {basic.get('region', 'N/A')}                  ║
║  {THEME.LIGHTNING_EMOJI} <b>ʟᴇᴠᴇʟ:</b> {basic.get('level', 'N/A')}                   ║
║  {THEME.SUCCESS_EMOJI} <b>ʟɪᴋᴇꜱ:</b> {basic.get('liked', 'N/A')}                    ║
║                                                 ║
{create_fancy_footer()}
"""
            await processing.edit_text(msg, parse_mode="HTML")
            
            try:
                banner_url = f"https://profile.thug4ff.com/api/profile_card?uid={uid}"
                banner_res = requests.get(banner_url, timeout=60)
                if banner_res.status_code == 200:
                    banner = BytesIO(banner_res.content)
                    banner.name = "banner.webp"
                    await update.message.reply_sticker(sticker=banner)
            except:
                pass
                
    except Exception as e:
        await processing.edit_text(f"{THEME.ERROR_EMOJI} Error: <code>{escape(str(e))}</code>", parse_mode="HTML")

# ---------------------- BROADCAST HANDLER ----------------------
async def handle_broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.user_data.get("broadcast_mode"):
        return
    
    user = update.effective_user
    if not (is_owner(user) or is_admin(user)):
        context.user_data["broadcast_mode"] = False
        return
    
    message_text = update.message.text
    if message_text == "/cancel":
        context.user_data["broadcast_mode"] = False
        await update.message.reply_text(f"{THEME.SUCCESS_EMOJI} ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴍᴏᴅᴇ ᴄᴀɴᴄᴇʟʟᴇᴅ.")
        return
    
    await update.message.reply_text(f"{THEME.PROCESS_EMOJI} ʙʀᴏᴀᴅᴄᴀꜱᴛɪɴɢ ᴛᴏ {len(vip_users)} ᴠɪᴘ ᴜꜱᴇʀꜱ...")
    
    success_count = 0
    for vip_id in vip_users:
        try:
            await context.bot.send_message(chat_id=vip_id, text=f"📢 <b>Broadcast from Admin</b>\n\n{message_text}", parse_mode="HTML")
            success_count += 1
        except:
            pass
    
    context.user_data["broadcast_mode"] = False
    await update.message.reply_text(f"{THEME.SUCCESS_EMOJI} ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴄᴏᴍᴘʟᴇᴛᴇᴅ!\n\nꜱᴇɴᴛ ᴛᴏ: {success_count}/{len(vip_users)} ᴜꜱᴇʀꜱ")

# ---------------------- AUTO TASK HELPERS ----------------------
def load_auto_tasks():
    return load_json_file(AUTO_TASKS_FILE, [])

def save_auto_tasks(tasks):
    save_json_file(AUTO_TASKS_FILE, tasks)

# ---------------------- MAIN FUNCTION ----------------------
async def allow_group_only(update: Update):
    chat = update.effective_chat
    user = update.effective_user
    
    if chat.type == ChatType.PRIVATE:
        if is_owner(user) or is_admin(user):
            return True
        await update.message.reply_text(f"{THEME.ERROR_EMOJI} ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ɪɴ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ.")
        return False
    
    if chat.id != ALLOWED_GROUP_ID:
        await update.message.reply_text(f"{THEME.ERROR_EMOJI} ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ʜᴇʀᴇ.")
        return False
    
    return True

# ---------------------- REGION COMMAND ----------------------
async def region_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(f"{THEME.WARNING_EMOJI} Usage: <code>/region 6283999318</code>", parse_mode="HTML")
        return
    uid = context.args[0]
    msg = await update.message.reply_text(f"{THEME.PROCESS_EMOJI} Checking region for UID: <code>{uid}</code>", parse_mode="HTML")
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(ULTRA_API_URL.format(uid=uid)) as resp:
                data = await resp.json()
                text = f"""
╔════════════════════════════════════════════════╗
║  {THEME.STAR_EMOJI} <b>𝐑𝐄𝐆𝐈𝐎𝐍 𝐈𝐍𝐅𝐎𝐑𝐌𝐀𝐓𝐈𝐎𝐍</b> {THEME.STAR_EMOJI}          ║
╠════════════════════════════════════════════════╣
║                                                 ║
║  {THEME.DIAMOND_EMOJI} <b>ɴᴀᴍᴇ:</b> {data.get('nickname', 'N/A')}                ║
║  {THEME.BOT_EMOJI} <b>ᴜɪᴅ:</b> <code>{uid}</code>                       ║
║  {THEME.SHIELD_EMOJI} <b>ʀᴇɢɪᴏɴ:</b> {data.get('region', 'N/A')}                  ║
║                                                 ║
{create_fancy_footer()}
"""
                await msg.edit_text(text, parse_mode="HTML")
        except Exception as e:
            await msg.edit_text(f"{THEME.ERROR_EMOJI} Error: {e}")

# ---------------------- SPAM COMMAND ----------------------
async def spam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await allow_group_only(update):
        return
    if len(context.args) < 2:
        await update.message.reply_text(f"{THEME.WARNING_EMOJI} Usage: <code>/spam ind 6283999318</code>", parse_mode="HTML")
        return
    region = context.args[0].lower()
    uid = context.args[1]
    loading = await update.message.reply_text(f"{THEME.PROCESS_EMOJI} Sending spam requests...\nUID: <code>{uid}</code>\nRegion: {region.upper()}", parse_mode="HTML")
    try:
        async with aiohttp.ClientSession() as session:
            url = f"{SPAM_API}/spam?uid={uid}&key=ARAFAT"
            async with session.get(url) as resp:
                data = await resp.json()
        if not data or "friend_requests" not in data:
            await loading.edit_text(f"{THEME.ERROR_EMOJI} DATA NOT FOUND!\nWrong UID or Region.")
            return
        fr = data["friend_requests"]
        update_stats("spam", "spam")
        text = f"""
╔════════════════════════════════════════════════╗
║  {THEME.ROCKET_EMOJI} <b>𝐒𝐏𝐀𝐌 𝐑𝐄𝐐𝐔𝐄𝐒𝐓 𝐂𝐎𝐌𝐏𝐋𝐄𝐓𝐄</b> {THEME.ROCKET_EMOJI}      ║
╠════════════════════════════════════════════════╣
║                                                 ║
║  {THEME.BOT_EMOJI} <b>ᴜɪᴅ:</b> <code>{uid}</code>                       ║
║  {THEME.STAR_EMOJI} <b>ʀᴇɢɪᴏɴ:</b> {region.upper()}                     ║
║                                                 ║
╠════════════════════════════════════════════════╣
║  📊 <b>𝐑𝐄𝐒𝐔𝐋𝐓𝐒</b>                                   ║
║                                                 ║
║  • {THEME.SUCCESS_EMOJI} ꜱᴜᴄᴄᴇꜱꜱ: {fr.get('successful', 0)}                      ║
║  • {THEME.ERROR_EMOJI} ꜰᴀɪʟᴇᴅ: {fr.get('failed', 0)}                       ║
║  • 📨 ᴛᴏᴛᴀʟ: {fr.get('total', 0)}                                 ║
║                                                 ║
{create_fancy_footer()}
"""
        await loading.edit_text(text, parse_mode="HTML")
    except Exception as e:
        await loading.edit_text(f"{THEME.ERROR_EMOJI} Error: {escape(str(e))}")

# ---------------------- ADD/REMOVE VIP ----------------------
async def addvip_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await allow_group_only(update):
        return
    if not (is_owner(update.effective_user) or is_admin(update.effective_user)):
        await update.message.reply_text(f"{THEME.ERROR_EMOJI} ᴀᴅᴍɪɴ ᴏɴʟʏ ᴄᴏᴍᴍᴀɴᴅ.")
        return
    if len(context.args) < 1:
        await update.message.reply_text(f"{THEME.WARNING_EMOJI} Usage: <code>/addvip 123456789</code>", parse_mode="HTML")
        return
    try:
        uid = int(context.args[0])
    except:
        await update.message.reply_text(f"{THEME.ERROR_EMOJI} Invalid ID.")
        return
    vip_users.add(uid)
    save_vips(vip_users)
    await update.message.reply_text(f"{THEME.SUCCESS_EMOJI} VIP Added: <code>{uid}</code>", parse_mode="HTML")

async def removevip_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await allow_group_only(update):
        return
    if not (is_owner(update.effective_user) or is_admin(update.effective_user)):
        await update.message.reply_text(f"{THEME.ERROR_EMOJI} ᴀᴅᴍɪɴ ᴏɴʟʏ ᴄᴏᴍᴍᴀɴᴅ.")
        return
    if len(context.args) < 1:
        await update.message.reply_text(f"{THEME.WARNING_EMOJI} Usage: <code>/removevip 123456789</code>", parse_mode="HTML")
        return
    try:
        uid = int(context.args[0])
    except:
        await update.message.reply_text(f"{THEME.ERROR_EMOJI} Invalid ID.")
        return
    vip_users.discard(uid)
    save_vips(vip_users)
    await update.message.reply_text(f"{THEME.SUCCESS_EMOJI} VIP Removed: <code>{uid}</code>", parse_mode="HTML")

async def listvip_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await allow_group_only(update):
        return
    if not (is_owner(update.effective_user) or is_admin(update.effective_user)):
        await update.message.reply_text(f"{THEME.ERROR_EMOJI} ᴀᴅᴍɪɴ ᴏɴʟʏ ᴄᴏᴍᴍᴀɴᴅ.")
        return
    if not vip_users:
        await update.message.reply_text(f"{THEME.ERROR_EMOJI} ɴᴏ ᴠɪᴘ ᴜꜱᴇʀꜱ ꜰᴏᴜɴᴅ.")
        return
    msg = f"{THEME.CROWN_EMOJI} <b>VIP Users List</b>\n\n"
    for u in vip_users:
        msg += f"• <code>{u}</code>\n"
    await update.message.reply_text(msg, parse_mode="HTML")

# ---------------------- AUTO TASK COMMANDS ----------------------
async def autolike_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"{THEME.SUCCESS_EMOJI} Auto-like feature is available. Use /admin panel to schedule.")

async def autovisit_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"{THEME.SUCCESS_EMOJI} Auto-visit feature is available. Use /admin panel to schedule.")

async def listauto_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"{THEME.INFO_EMOJI} Use /admin panel to manage auto tasks.")

async def cancelauto_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"{THEME.INFO_EMOJI} Use /admin panel to cancel auto tasks.")

async def cancelbyuid_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"{THEME.INFO_EMOJI} Use /admin panel to cancel by UID.")

# ---------------------- CALLBACK HANDLER ----------------------
async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "premium_features":
        text = f"""
╔════════════════════════════════════════════════╗
║  {THEME.DIAMOND_EMOJI} <b>𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐅𝐄𝐀𝐓𝐔𝐑𝐄𝐒</b> {THEME.DIAMOND_EMOJI}         ║
╠════════════════════════════════════════════════╣
║                                                 ║
║  {THEME.SUCCESS_EMOJI} ✓ Unlimited Likes & Visits          ║
║  {THEME.ROCKET_EMOJI} ✓ Auto Like/Visit Scheduler        ║
║  {THEME.SHIELD_EMOJI} ✓ Advanced Player Analytics        ║
║  {THEME.LIGHTNING_EMOJI} ✓ Priority Support                 ║
║  {THEME.CROWN_EMOJI} ✓ 24/7 Bot Availability            ║
║                                                 ║
╠════════════════════════════════════════════════╣
║  {THEME.DIAMOND_EMOJI} <b>𝐕𝐈𝐏 𝐏𝐑𝐈𝐂𝐄</b>                           ║
║                                                 ║
║  Contact: {OWNER_USERNAME} for pricing          ║
║                                                 ║
{create_fancy_footer()}
"""
        await query.edit_message_text(text, parse_mode="HTML")
    
    elif query.data == "help_menu":
        await help_command(update, context)
    
    else:
        await admin_callback(update, context)

# ---------------------- MAIN ----------------------
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("admin", admin_panel))
    app.add_handler(CommandHandler("like", like_command))
    app.add_handler(CommandHandler("visit", visit_command))
    app.add_handler(CommandHandler("info", info_command))
    app.add_handler(CommandHandler("region", region_command))
    app.add_handler(CommandHandler("spam", spam))
    app.add_handler(CommandHandler("addvip", addvip_command))
    app.add_handler(CommandHandler("removevip", removevip_command))
    app.add_handler(CommandHandler("listvip", listvip_command))
    app.add_handler(CommandHandler("autolike", autolike_command))
    app.add_handler(CommandHandler("autovisit", autovisit_command))
    app.add_handler(CommandHandler("listauto", listauto_command))
    app.add_handler(CommandHandler("cancelauto", cancelauto_command))
    app.add_handler(CommandHandler("cancelbyuid", cancelbyuid_command))
    
    # Handlers
    app.add_handler(CallbackQueryHandler(callback_handler))
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome_new_member))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_broadcast))
    
    print("""
╔════════════════════════════════════════════════════════════════╗
║   🔥 𝐀𝐔𝐓𝐎 𝐋𝐈𝐊𝐄 & 𝐕𝐈𝐒𝐈𝐓 𝐁𝐎𝐓 𝐕𝟑.𝟎 - 𝐈𝐍𝐈𝐓𝐈𝐀𝐋𝐈𝐙𝐈𝐍𝐆 🔥          ║
╠════════════════════════════════════════════════════════════════╣
║   🤖 ꜱᴛᴀᴛᴜꜱ        ➤   🟢 ᴏɴʟɪɴᴇ & ʀᴇᴀᴅʏ                       ║
║   💎 ᴍᴏᴅᴇ          ➤   🔥 ᴘʀᴇᴍɪᴜᴍ ᴏᴠᴇʀᴅʀɪᴠᴇ                ║
║   🛡️ ꜱᴇᴄᴜʀɪᴛʏ       ➤   🔒 ᴍᴀx ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ᴀᴄᴛɪᴠᴇ            ║
║   ⭐ ᴠɪᴘ ꜱʏꜱᴛᴇᴍ    ➤   ✔ ᴇɴᴀʙʟᴇᴅ ᴡɪᴛʜ {len(vip_users)} ᴜꜱᴇʀꜱ      ║
║   🚀 ʀᴇꜱᴘᴏɴꜱᴇ ʀᴀᴛᴇ ➤   ⚡ ᴜʟᴛʀᴀ ꜰᴀꜱᴛ (0.1ms)                ║
╠════════════════════════════════════════════════════════════════╣
║   👑 ᴄʀᴇᴀᴛᴏʀ / ᴅᴇᴠᴇʟᴏᴘᴇʀ ➤  @ARAFAT_CODEX1                     ║
║   🔰 ᴄᴏ-ᴀᴅᴍɪɴ ➤  @Mobin_codex                                 ║
║   🎧 ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ➤  @ARAFAT_LIKE_GROUP                          ║
╚════════════════════════════════════════════════════════════════╝
""")
    
    app.run_polling()

if __name__ == "__main__":
    main()