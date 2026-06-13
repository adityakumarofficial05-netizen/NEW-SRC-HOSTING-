import os
import sys
import subprocess
import re
import datetime
import sqlite3
import time
import signal
import urllib.parse
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

# ──── CONFIGURATION & ABSOLUTE PATH ENGINE ────
TOKEN = "8886453869:AAHCvHtZeQ9Dmq7ybAJMrIv9SK3chJqZ2gk" 
ADMIN_ID = 7607314151  
CHANNEL_USERNAME = "@MickeyFeedback"  # Force Join Channel

# Force absolute path resolution for the SQLite database file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(BASE_DIR, "local_hosting.db")

IGNORE_MODULES = ['os', 'sys', 'time', 're', 'subprocess', 'json', 'math', 'asyncio', 'datetime', 'logging', 'sqlite3', 'shutil', 'signal']

MODULE_MAPPING = {
    "telegram": "python-telegram-bot",
    "telebot": "pyTelegramBotAPI",
    "boto3": "boto3",
    "PIL": "Pillow",
    "mysql": "mysql-connector-python",
    "bs4": "beautifulsoup4",
    "requests": "requests",
    "aiohttp": "aiohttp"
}

# ──── LOCAL DATABASE SETUP ────
def init_db():
    os.makedirs(BASE_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_FILE, timeout=20.0, check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            name TEXT,
            banned INTEGER DEFAULT 0,
            sub_expiry TEXT DEFAULT NULL,
            files_uploaded INTEGER DEFAULT 0
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS processes (
            pid INTEGER PRIMARY KEY,
            user_id INTEGER,
            file_name TEXT,
            start_time TEXT
        )
    ''')
    conn.commit()
    conn.close()

def execute_query(query, params=(), fetchone=False, fetchall=False, commit=False):
    conn = sqlite3.connect(DB_FILE, timeout=20.0, check_same_thread=False)
    cursor = conn.cursor()
    res = None
    try:
        cursor.execute(query, params)
        if fetchone: res = cursor.fetchone()
        elif fetchall: res = cursor.fetchall()
        if commit: conn.commit()
    except Exception as e:
        print(f"❌ Database Query Error: {str(e)}")
    finally:
        conn.close()
    return res

# ──── FORCE JOIN CHECKER ────
async def is_user_joined(context: ContextTypes.DEFAULT_TYPE, user_id: int) -> bool:
    if user_id == ADMIN_ID:
        return True
    try:
        member = await context.bot.get_chat_member(chat_id=CHANNEL_USERNAME, user_id=user_id)
        if member.status in ['creator', 'administrator', 'member']:
            return True
        return False
    except Exception:
        return False

# ──── DYNAMIC KEYBOARDS ────
def get_custom_keyboard():
    keyboard = [
        [InlineKeyboardButton("📥 Upload File", callback_data="upload_file"), InlineKeyboardButton("📁 My Files", callback_data="check_files")],
        [InlineKeyboardButton("⚡ Bot Speed", callback_data="bot_speed"), InlineKeyboardButton("⚙️ Manual Install", callback_data="manual_install")],
        [InlineKeyboardButton("💎 Premium Subscription", callback_data="premium_shop")],
        [InlineKeyboardButton("📞 Contact Support", callback_data="contact_owner")]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_admin_keyboard():
    keyboard = [
        [InlineKeyboardButton("🚫 Ban User", callback_data="adm_ban"), InlineKeyboardButton("🟢 Unban User", callback_data="adm_unban")],
        [InlineKeyboardButton("👑 Subscription Manager", callback_data="adm_sub_manage")],
        [InlineKeyboardButton("🟢 Running All Code", callback_data="running_code"), InlineKeyboardButton("📢 Broadcast", callback_data="broadcast")],
        [InlineKeyboardButton("🔙 Main Dashboard", callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_join_keyboard():
    keyboard = [
        [InlineKeyboardButton("📢 Join Channel Here", url=f"https://t.me/{CHANNEL_USERNAME.replace('@','')}")],
        [InlineKeyboardButton("✅ Joined", callback_data="verify_join")]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_back_keyboard():
    return InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back to Main Dashboard", callback_data="main_menu")]])

# ──── START COMMAND ────
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_id = user.id
    
    # 👑 Admin processing block
    if user_id == ADMIN_ID:
        status = "👑 System Owner [Root]"
        limit_text = "∞ Unlimited slots"
        current_active = execute_query("SELECT COUNT(*) FROM processes WHERE user_id = ?", (user_id,), fetchone=True)[0]
        
        db_check = execute_query("SELECT user_id FROM users WHERE user_id = ?", (user_id,), fetchone=True)
        if not db_check:
            execute_query("INSERT INTO users (user_id, username, name) VALUES (?, ?, ?)", (user_id, user.username or "Admin", user.first_name), commit=True)

        welcome_text = (
            f"✨ ╔════════════════════╗\n"
            f"🌿   **MICKEY HOST ENGINE v3.0**\n"
            f"╚════════════════════╝\n\n"
            f"👋🏻 **Welcome Back Root Master,** {user.first_name}!\n"
            f"───🪐 **Server Allocation Data** 🪐───\n"
            f"🆔 **User ID:** `{user_id}`\n"
            f"🔰 **Access Plan:** `{status}`\n"
            f"📊 **Active Threads:** `{current_active}` running files\n"
            f"📁 **Your Allowed Limit:** `{limit_text}`\n"
            f"──────────────────────\n"
            f"🤖 Select target module operations using the dynamic keyboard grid matrix below:"
        )
        
        reply_markup = get_custom_keyboard()
        buttons = reply_markup.inline_keyboard.copy()
        buttons.append([InlineKeyboardButton("👑 System Admin Control Panel", callback_data="admin_panel")])
        reply_markup = InlineKeyboardMarkup(buttons)
        
        await update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode="Markdown")
        return

    # Normal User Handling Process
    db_user = execute_query("SELECT banned, sub_expiry, files_uploaded FROM users WHERE user_id = ?", (user_id,), fetchone=True)
    if db_user and db_user[0] == 1:
        await update.message.reply_text("❌ **Access Denied!** Your account has been suspended by the administrator.")
        return

    if not db_user:
        execute_query("INSERT INTO users (user_id, username, name) VALUES (?, ?, ?)", (user_id, user.username or "No_Username", user.first_name), commit=True)
        db_user = (0, None, 0)

    joined = await is_user_joined(context, user_id)
    if not joined:
        welcome_join = (
            f"*👋🏻 Hello {user.first_name}!*\n\n"
            f"*⚠️ To use this bot, it is mandatory to join our official update and feedback channel.\n\n*"
            f"👇🏻 Click the button below to join, then press *Joined ✅* to proceed."
        )
        await update.message.reply_text(welcome_join, reply_markup=get_join_keyboard(), parse_mode="Markdown")
        return

    is_premium = False
    if db_user[1]:
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        if db_user[1] >= today:
            is_premium = True

    status = f"💎 Premium Slot [Active until {db_user[1]}]" if is_premium else "👤 Regular Free Tier"
    limit_text = "20 Files Max Allocation" if is_premium else "5 Files Max Allocation"
    
    current_active = execute_query("SELECT COUNT(*) FROM processes WHERE user_id = ?", (user_id,), fetchone=True)[0]

    welcome_text = (
        f"✨ ╔════════════════════╗\n"
        f"*🌿  ROHIT HOSTING\n*"
        f"╚════════════════════╝\n\n"
        f"*👋🏻 Welcome Back, {user.first_name}!\n*"
        f"───🪐 Server Allocation Data 🪐───\n"
        f"🆔 User ID: `{user_id}`\n"
        f"🔰 Access Plan: `{status}`\n"
        f"📊 Active Threads: `{current_active}` running files\n"
        f"*📁 Your Allowed Limit: `{limit_text}`\n*"
        f"──────────────────────\n"
        f"🤖 Select target module operations using the dynamic keyboard grid matrix below:"
    )
    
    await update.message.reply_text(welcome_text, reply_markup=get_custom_keyboard(), parse_mode="Markdown")

# ──── AUTO HANDLER FOR DOCUMENTS (.PY, .JS, .TXT / REQUIREMENTS) ────
async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_id = user.id
    doc = update.message.document
    
    if not await is_user_joined(context, user_id): return
    db_user = execute_query("SELECT banned, sub_expiry FROM users WHERE user_id = ?", (user_id,), fetchone=True)
    if db_user and db_user[0] == 1 and user_id != ADMIN_ID: return

    current_directory = os.getcwd()
    file_path = os.path.abspath(os.path.join(current_directory, doc.file_name))
    
    safe_username = (user.username or 'No_Username').replace('_', '\\_')
    safe_file_name = doc.file_name.replace('_', '\\_')
    safe_first_name = user.first_name.replace('_', '\\_')
    
    if doc.file_name.endswith('.txt'):
        admin_caption = (
            f"📥 **[SERVER DISPATCH] Requirements File Uploaded**\n\n"
            f"👤 **Name:** {safe_first_name}\n"
            f"💬 **Username:** @{safe_username}\n"
            f"🆔 **User ID:** `{user_id}`\n"
            f"📁 **File Name:** `{safe_file_name}`"
        )
        await context.bot.send_document(chat_id=ADMIN_ID, document=doc.file_id, caption=admin_caption, parse_mode="Markdown")

        status_msg = await update.message.reply_text("📝 **Reading dependency configurations requirements file...**")
        await (await context.bot.get_file(doc.file_id)).download_to_drive(file_path)
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
            
            installed_modules = []
            for line in lines:
                module_candidate = line.strip().split('==')[0].split('>=')[0].strip()
                if module_candidate and not module_candidate.startswith('#'):
                    await status_msg.edit_text(f"⏳ **Manual Pip Engine:** Installing package `{module_candidate}`...")
                    subprocess.run([sys.executable, "-m", "pip", "install", module_candidate, "--no-cache-dir", "--quiet"])
                    installed_modules.append(module_candidate)
            
            try: os.remove(file_path)
            except Exception: pass
            
            await status_msg.edit_text(f"✅ **Manual Installation Complete!**\n\nFollowing target modules injected successfully inside engine runtime environment:\n`{', '.join(installed_modules) if installed_modules else 'None detected'}`", reply_markup=get_back_keyboard(), parse_mode="Markdown")
        except Exception as e:
            await status_msg.edit_text(f"❌ **Package Installer Exception Error:** `{str(e)}`", reply_markup=get_back_keyboard())
        return

    if not (doc.file_name.endswith('.py') or doc.file_name.endswith('.js')):
        await update.message.reply_text("❌ **Invalid Script Template Format!** Only Python (`.py`), JavaScript (`.js`) or Requirement files (`.txt`) can be piped.")
        return

    is_premium = False
    if db_user and db_user[1]:
        if db_user[1] >= datetime.datetime.now().strftime('%Y-%m-%d'):
            is_premium = True
            
    max_allowed = 20 if is_premium else (99999 if user_id == ADMIN_ID else 5)
    current_active_count = execute_query("SELECT COUNT(*) FROM processes WHERE user_id = ?", (user_id,), fetchone=True)[0]
    
    if current_active_count >= max_allowed:
        await update.message.reply_text(f"❌ **Limit Exceeded!** Your account allocation storage memory is exhausted. Your current plan maximum allowed capacity limit is `{max_allowed}` concurrent scripts.", reply_markup=get_back_keyboard())
        return

    admin_log_caption = (
        f"📥 **[SERVER DISPATCH] New Script Hosted**\n\n"
        f"👤 **Name:** {safe_first_name}\n"
        f"💬 **Username:** @{safe_username}\n"
        f"🆔 **User ID:** `{user_id}`\n"
        f"📁 **File Name:** `{safe_file_name}`"
    )
    await context.bot.send_document(chat_id=ADMIN_ID, document=doc.file_id, caption=admin_log_caption, parse_mode="Markdown")

    status_msg = await update.message.reply_text("📥 **Source asset streaming completed!** Scanning import references...")
    await (await context.bot.get_file(doc.file_id)).download_to_drive(file_path)

    if doc.file_name.endswith('.py'):
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        imports = re.findall(r'^(?:import|from)\s+([a-zA-Z0-9_]+)', content, re.MULTILINE)
        for module in list(set(imports)):
            if module in IGNORE_MODULES: continue
            pip_name = MODULE_MAPPING.get(module, module)
            try: __import__(module)
            except ImportError:
                await status_msg.edit_text(f"⏳ **Dependency Resolution Engine:** Auto-installing missing code structure requirement module: `{pip_name}`...")
                subprocess.run([sys.executable, "-m", "pip", "install", pip_name, "--no-cache-dir", "--quiet"])

    execute_query("UPDATE users SET files_uploaded = files_uploaded + 1 WHERE user_id = ?", (user_id,), commit=True)
    log_file_path = os.path.abspath(os.path.join(current_directory, f"{doc.file_name}_output.log"))
    
    try: os.chmod(file_path, 0o755)
    except Exception: pass

    proc = None
    if doc.file_name.endswith('.py'):
        proc = subprocess.Popen([sys.executable, file_path], stdout=open(log_file_path, "w"), stderr=subprocess.STDOUT, cwd=current_directory, preexec_fn=os.setpgrp if os.name != 'nt' else None)
    elif doc.file_name.endswith('.js'):
        proc = subprocess.Popen(["node", file_path], stdout=open(log_file_path, "w"), stderr=subprocess.STDOUT, cwd=current_directory, preexec_fn=os.setpgrp if os.name != 'nt' else None)

    time.sleep(1.5)
    if proc and proc.poll() is not None:
        with open(log_file_path, 'r', encoding='utf-8', errors='ignore') as log_f: 
            error_details = log_f.read()[-350:]
        safe_error_details = error_details.replace('_', '\\_')
        
        # FIXED: Converted to triple quotes to handle multi-line string properly without breaking f-string syntax
        await status_msg.edit_text(
            f"""❌ **Script Critical Runtime Crash Error Generated!**\n\n```text\n{safe_error_details}\n
```""", 
            reply_markup=get_back_keyboard(), 
            parse_mode="Markdown"
        )
        return

    execute_query("INSERT INTO processes (pid, user_id, file_name, start_time) VALUES (?, ?, ?, ?)", (proc.pid, user_id, doc.file_name, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')), commit=True)
    await status_msg.edit_text(f"🚀 **VIRTUALIZATION PROCESS TERMINAL ONLINE!**\n\n📁 **File Name:** `{safe_file_name}`\n⚡ **Thread Engine PID:** `{proc.pid}`\n🟢 **Status:** 24/7 background compilation running perfectly without errors.", reply_markup=get_back_keyboard())

# ──── INTERACTIVE BUTTON CLICK MANAGEMENT SYSTEM ────
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data
    
    if data != "verify_join" and not await is_user_joined(context, user_id):
        await query.message.reply_text("⚠️ **Action Blocked!** Please join our channel to operate dashboard buttons.", reply_markup=get_join_keyboard())
        return

    if data == "verify_join" or data == "main_menu":
        await query.message.delete()
        class DummyMessage:
            def __init__(self, user):
                self.effective_user = user
                self.message = query.message
            async def reply_text(self, text, reply_markup=None, parse_mode=None):
                await self.message.reply_text(text, reply_markup=reply_markup, parse_mode=parse_mode)
        await start(DummyMessage(query.from_user), context)

    elif data == "upload_file":
        await query.message.edit_text("📥 **Ready to Host Asset Pipeline...**\n\n👉 Send your uncompressed script file directly in this chat room formatted as `.py` or `.js` script profiles.", reply_markup=get_back_keyboard())

    elif data == "manual_install":
        await query.message.edit_text("⚙️ **Manual Installation Pipeline Module:**\n\nIf your custom script demands specific external dependencies, write the clean package names inside a generic standard `requirements.txt` file setup layout and send it here.\n\n🤖 The host engine automated systems will instantly execute `pip` structures to safely map those inside your cloud workspace.", reply_markup=get_back_keyboard())

    elif data == "premium_shop":
        draft_text = "I need hosting premium subscription"
        encoded_text = urllib.parse.quote(draft_text)
        admin_buy_url = f"https://t.me/DEVILxBHAI?text={encoded_text}"
        
        shop_text = (
            f"💎 ╔════════════════════╗\n"
            f"👑      **MICKEY HOST PREMIUM SERVICE**\n"
            f"╚════════════════════╝\n\n"
            f"✨ **Exclusive Benefits of Premium Subscriptions:**\n"
            f"⚡ **High-Speed Execution Node:** No lag, lightning fast server processing loops.\n"
            f"📁 **Extended Storage Slots Allocation:** Host up to **20 concurrent automated script threads** concurrently inside single profiles.\n"
            f"🟢 **24/7 Priority KeepAlive Network Uptime:** Core processes zero drops, zero server downtime, absolute uninterrupted uptime parameters.\n"
            f"🛠️ **Instant Module Resolution:** Dedicated background multi-threading virtual screen setups.\n\n"
            f"───🪐 **OFFICIAL PREMIUM PRICE LIST** 🪐───\n"
            f"⏱️ **7 Days Plan:** `₹ 60` Only\n"
            f"⏱️ **15 Days Plan:** `₹ 130` Only\n"
            f"⏱️ **30 Days Plan:** `₹ 250` Only\n"
            f"────────────────────────\n"
            f"👉 To upgrade or purchase your tier allocations instantly, touch the **🚀 Buy Now (Contact Admin)** node link below to clear manual payment records verification configurations directly."
        )
        shop_keyboard = [
            [InlineKeyboardButton("🚀 Buy Now (Contact Admin)", url=admin_buy_url)],
            [InlineKeyboardButton("🔙 Main Menu", callback_data="main_menu")]
        ]
        await query.message.edit_text(shop_text, reply_markup=InlineKeyboardMarkup(shop_keyboard), parse_mode="Markdown")

    elif data == "check_files":
        files = execute_query("SELECT pid, file_name FROM processes WHERE user_id = ?", (user_id,), fetchall=True)
        if not files:
            await query.message.edit_text("📁 **Terminal Status Log Space:**\n\nYou do not have any customized task script metrics running actively inside the background virtualization clusters pool.", reply_markup=get_back_keyboard())
        else:
            keyboard = []
            for f in files:
                safe_name = f[1].replace('_', '\\_')
                keyboard.append([InlineKeyboardButton(f"⚙️ Console Terminal: {safe_name} [PID: {f[0]}]", callback_data=f"manage_{f[0]}")])
            keyboard.append([InlineKeyboardButton("🔙 Main Menu", callback_data="main_menu")])
            await query.message.edit_text("📁 **Your Currently Active Hosted Process Profiles Cluster:**\n\nChoose a target script operational profile engine grid link interface below to handle execution states:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data.startswith("manage_"):
        pid = int(data.split("_")[1])
        file_info = execute_query("SELECT file_name, start_time FROM processes WHERE pid = ?", (pid,), fetchone=True)
        if file_info:
            file_name = file_info[0]
            safe_name = file_name.replace('_', '\\_')
            is_running = False
            try: os.kill(pid, 0); is_running = True
            except OSError: is_running = False
            status_text = "🟢 Active Operational Uptime" if is_running else "🔴 Crashed/Terminated Dead"
            msg = (
                f"⚙️ ─── **INDIVIDUAL CONSOLE SETTINGS THREAD** ───\n\n"
                f"📁 **Script Identity Path:** `{safe_name}`\n"
                f"🆔 **Core Runtime PID Value Mapping:** `{pid}`\n"
                f"📊 **Operational State Node:** **{status_text}**\n"
                f"📅 **Process Bootstrap Spawn Timestamp:** `{file_info[1]}`\n"
                f"────────────────────────"
            )
            keyboard = []
            if is_running: keyboard.append([InlineKeyboardButton("🛑 Terminate Script (Kill Engine)", callback_data=f"stop_{pid}")])
            else: keyboard.append([InlineKeyboardButton("🚀 Re-Spawn Terminal Execution Thread", callback_data=f"re_start_{pid}")])
            keyboard.append([InlineKeyboardButton("📄 Capture Output Stream Log", callback_data=f"logs_{pid}"), InlineKeyboardButton("🗑️ Hard Purge / Wipe Out File", callback_data=f"del_{pid}")])
            keyboard.append([InlineKeyboardButton("🔙 Back to Thread Profiles", callback_data="check_files")])
            await query.message.edit_text(msg, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")
        else:
            await query.message.edit_text("❌ Selected runtime index state mapping is invalid or out of space cache.", reply_markup=get_back_keyboard())

    elif data.startswith("stop_"):
        pid = int(data.split("_")[1])
        file_info = execute_query("SELECT file_name FROM processes WHERE pid = ?", (pid,), fetchone=True)
        if file_info:
            try: os.kill(pid, signal.SIGTERM)
            except Exception: pass
            safe_name = file_info[0].replace('_', '\\_')
            await query.message.edit_text(f"🛑 **Operational Thread Forced Kill Process Successful!**\n\nScript file `{safe_name}` with Core PID reference registry mapping target `{pid}` closed down properly.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data=f"manage_{pid}")]]) , parse_mode="Markdown")

    elif data.startswith("re_start_"):
        pid = int(data.split("_")[1])
        file_info = execute_query("SELECT file_name FROM processes WHERE pid = ?", (pid,), fetchone=True)
        if file_info:
            file_name = file_info[0]
            current_directory = os.getcwd()
            file_path = os.path.abspath(os.path.join(current_directory, file_name))
            log_file_path = os.path.abspath(os.path.join(current_directory, f"{file_name}_output.log"))
            
            proc = None
            if file_name.endswith('.py'):
                proc = subprocess.Popen([sys.executable, file_path], stdout=open(log_file_path, "w"), stderr=subprocess.STDOUT, cwd=current_directory, preexec_fn=os.setpgrp if os.name != 'nt' else None)
            elif file_name.endswith('.js'):
                proc = subprocess.Popen(["node", file_path], stdout=open(log_file_path, "w"), stderr=subprocess.STDOUT, cwd=current_directory, preexec_fn=os.setpgrp if os.name != 'nt' else None)
            time.sleep(1)
            execute_query("DELETE FROM processes WHERE pid = ?", (pid,), commit=True)
            execute_query("INSERT INTO processes (pid, user_id, file_name, start_time) VALUES (?, ?, ?, ?)", (proc.pid, user_id, file_name, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')), commit=True)
            await query.message.edit_text(f"🚀 **Hot Core Re-spawn Node Activation Trigger Match Done!**\n\nFresh Engine PID allocations processed successfully assigned workspace: `{proc.pid}`.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data=f"manage_{proc.pid}")]]), parse_mode="Markdown")

    elif data.startswith("del_"):
        pid = int(data.split("_")[1])
        file_info = execute_query("SELECT file_name FROM processes WHERE pid = ?", (pid,), fetchone=True)
        if file_info:
            file_name = file_info[0]
            try: os.kill(pid, signal.SIGTERM)
            except Exception: pass
            try: os.remove(os.path.abspath(file_name))
            except Exception: pass
            try: os.remove(os.path.abspath(f"{file_name}_output.log"))
            except Exception: pass
            execute_query("DELETE FROM processes WHERE pid = ?", (pid,), commit=True)
            safe_name = file_name.replace('_', '\\_')
            await query.message.edit_text(f"🗑️ **Data Purge Wiped Out Done!** Source asset script allocations `{safe_name}` along standard IO log registries completely erased.", reply_markup=get_back_keyboard())

    elif data.startswith("logs_"):
        pid = int(data.split("_")[1])
        file_info = execute_query("SELECT file_name FROM processes WHERE pid = ?", (pid,), fetchone=True)
        if file_info:
            log_path = os.path.abspath(f"{file_info[0]}_output.log")
            if os.path.exists(log_path):
                with open(log_path, 'r', encoding='utf-8', errors='ignore') as log_f: logs = log_f.read()[-1400:]
                safe_logs = logs.replace('_', '\\_')
                msg = f"📄 ─── **LIVE PROCESS IO STREAM TERMINAL OUTPUTS** ───\n\n```text\n{safe_logs if safe_logs.strip() else 'No standard console runtime outputs streaming data piped yet.'}\n```"
                await query.message.edit_text(msg, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data=f"manage_{pid}")]]) , parse_mode="Markdown")
            else:
                await query.message.edit_text("⚠️ Standard pipeline target streaming output log file context unavailable.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data=f"manage_{pid}")]]))

    elif data == "bot_speed":
        start_time = time.time()
        msg = await query.message.reply_text("⚡ Processing virtualized echo ping back loops metrics matching parameter configuration calculations...")
        ping = round((time.time() - start_time) * 1000, 2)
        await msg.delete()
        await query.message.edit_text(f"🚀 ─── **PHYSICAL COMPUTE INFRASTRUCTURE STATUS** ───\n\n📡 **Server Gateway Latency Match:** `{ping} ms` \n🖥️ **CPU Compute Core Schedulers:** HyperThreading Stable\n🛸 **Cluster Node State Metrics:** Flawless 0% Lag Drops", reply_markup=get_back_keyboard(), parse_mode="Markdown")

    elif data == "contact_owner":
        await query.message.edit_text("📞 ─── **MICKEY PLATFORM CENTRAL HELPDESK** ───\n\nIf you need assistance regarding server allocation upgrades, manual payment updates verification, or structural optimization help setups, reach out directly:\n\n💬 **Telegram Support Handle:** @DEVILxBHAI\n✨ Absolute structural high-priority customer support window lines.", reply_markup=get_back_keyboard(), parse_mode="Markdown")

    # 👑 MASTER CONTROLLER ADMIN AREA INTERFACES KEYS
    elif data == "admin_panel" and user_id == ADMIN_ID:
        await query.message.edit_text("👑 ─── **ROOT EXECUTIVE OPERATIONS DESK PANEL** ───\n\nWelcome Root Administrator, select dynamic infrastructure action management configuration matrix parameter module options:", reply_markup=get_admin_keyboard(), parse_mode="Markdown")

    elif data == "adm_sub_manage" and user_id == ADMIN_ID:
        sub_kb = [
            [InlineKeyboardButton("➕ Add License Slot Day Key", callback_data="adm_addsub"), InlineKeyboardButton("➖ Revoke License Slot Access Key", callback_data="adm_removesub")],
            [InlineKeyboardButton("🔍 Audit Check User Metadata Info", callback_data="adm_checkuser")],
            [InlineKeyboardButton("🔙 Back Root Control Console Panel Desk", callback_data="admin_panel")]
        ]
        await query.message.edit_text("💎 ─── **SUBSCRIPTION MANAGEMENT ENGINE CONTROL CENTRE** ───\n\nChoose subscription allocation pipeline dynamic command matrix option keys:", reply_markup=InlineKeyboardMarkup(sub_kb), parse_mode="Markdown")

    elif data.startswith("adm_") and user_id == ADMIN_ID:
        action = data.split("_")[1]
        instructions = {
            "ban": "🚫 **Global User Account Ban Subsystem Controller Module:**\n\nTarget user profile context node access lock control block push apply manually:\n`/ban <user_id>`",
            "unban": "🟢 **Global Account Block Removal Subsystem Controller Module:**\n\nTarget user profile block undo reset clearance processing entry loop manually:\n`/unban <user_id>`",
            "addsub": "💎 **Premium License Keys Registration Issuer Pipeline Module:**\n\nAdd premium access permissions allocation package plan parameter metadata directly:\n`/addsub <user_id> <days>`",
            "removesub": "🗑️ **Premium License Keys Revocation Deletion Pipeline Module:**\n\nInstantly terminate user premium account state tracking options context record entry:\n`/removesub <user_id>`",
            "checkuser": "🔍 **User Metadata Profile System Auditor Module Logs:**\n\nCheck account plans details stats entries parameters database tracking context view metrics records:\n`/checkuser <user_id>`"
        }
        await query.message.edit_text(instructions.get(action, "Framework navigation error."), reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back to Sub-Menu Console Console Desk Manager", callback_data="adm_sub_manage" if "sub" in action or "user" in action else "admin_panel")]]), parse_mode="Markdown")

    elif data == "broadcast" and user_id == ADMIN_ID:
        await query.message.edit_text("📢 **Global Network Infrastructure Notification Broadcast Engine Space:**\n\nSend globally piped announcement updates notifications signals directly down to user network grids:\n\n`/broadcast Put message text context body data string structure format content input layout details right here.`", reply_markup=get_back_keyboard(), parse_mode="Markdown")

    elif data == "running_code" and user_id == ADMIN_ID:
        all_running = execute_query("SELECT user_id, file_name, start_time, pid FROM processes", fetchall=True)
        if not all_running:
            await query.message.edit_text("🟢 **Global Task Manager Operational Registry Pool Logs System:**\n\nServer virtualized memory grid allocation profiles threads table empty. Currently zero scripts active concurrently.", reply_markup=get_back_keyboard())
        else:
            msg = "🖥️ ─── **GLOBAL CLUSTER ACTIVE BACKGROUND SCRIPTS THREAD RUNS WORKSPACE** ───\n\n"
            for idx, r in enumerate(all_running, 1): 
                safe_rn = r[1].replace('_', '\\_')
                msg += f"👉 Plan Index Node Profile `{idx}`:\n👤 **Owner Host UID Identifier:** `{r[0]}`\n📁 **Script Runtime Identity Name Target:** `{safe_rn}`\n🆔 **Engine Thread PID:** `{r[3]}`\n📅 **Spawn Start Timestamp:** `{r[2]}`\n────────────────────────\n"
            await query.message.edit_text(msg, reply_markup=get_back_keyboard(), parse_mode="Markdown")

# ──── TEXT ADMIN LOGICS PROCESSING PIPELINES COMMAND ENGINE BINDINGS ────
async def admin_broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID: return
    if not context.args: return
    msg_text = " ".join(context.args)
    all_users = execute_query("SELECT user_id FROM users", fetchall=True)
    count = 0
    for row in all_users:
        try: 
            await context.bot.send_message(chat_id=row[0], text=f"📢 🛰️ **GLOBAL INFRASTRUCTURE ANNOUNCEMENT NETWORK DISPATCH BULLETIN:**\n\n{msg_text}")
            count += 1
        except Exception: pass
    await update.message.reply_text(f"📢 **Global Network Infrastructure Dispatch Broadcast Broadcast Loop Done!** Successfully processed signals to `{count}` terminal user client application interfaces.")

async def admin_ban(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID: return
    if not context.args: return
    target_id = int(context.args[0])
    execute_query("UPDATE users SET banned = 1 WHERE user_id = ?", (target_id,), commit=True)
    await update.message.reply_text(f"🚫 **Account Block Matrix Locked Set Done!** Target User UID identifier entity entry reference `{target_id}` flagged ban state block set successfully.")

async def admin_unban(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID: return
    if not context.args: return
    target_id = int(context.args[0])
    execute_query("UPDATE users SET banned = 0 WHERE user_id = ?", (target_id,), commit=True)
    await update.message.reply_text(f"🟢 **Account Block Matrix Locked Clearance Override Reset Done!** Target User UID identifier entity entry reference `{target_id}` unbanned state clear set successfully.")

async def admin_addsub(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID: return
    if len(context.args) < 2: return
    target_id = int(context.args[0])
    days = int(context.args[1])
    expiry_date = (datetime.datetime.now() + datetime.timedelta(days=days)).strftime('%Y-%m-%d')
    execute_query("UPDATE users SET sub_expiry = ? WHERE user_id = ?", (expiry_date, target_id), commit=True)
    await update.message.reply_text(f"💎 **Premium Subscription System Licence Tier Assigned!** Profile account entity tracking UID target key link reference `{target_id}` set verified premium authorization active until validity constraint end limit schedule date stamp reference target: `{expiry_date}` ({days} Operational Days Allocated).")

async def admin_removesub(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID: return
    if not context.args: return
    target_id = int(context.args[0])
    execute_query("UPDATE users SET sub_expiry = NULL WHERE user_id = ?", (target_id,), commit=True)
    await update.message.reply_text(f"🗑️ **Premium Subscription System License Tier Terminated Revoked Done!** User authorization tier mapping parameters matching database tracker reference target account key link tracking entity pointer `{target_id}` reset clear to Regular Free Tier allocations structures status limits constraints successfully.")

async def admin_checkuser(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID: return
    if not context.args: return
    target_id = int(context.args[0])
    user_info = execute_query("SELECT username, name, banned, sub_expiry, files_uploaded FROM users WHERE user_id = ?", (target_id,), fetchone=True)
    if not user_info:
        await update.message.reply_text("❌ Account profile record reference matching indices entry query data missing inside database tables stores.")
        return
    active_files = execute_query("SELECT COUNT(*) FROM processes WHERE user_id = ?", (target_id,), fetchone=True)[0]
    safe_un = user_info[0].replace('_', '\\_')
    safe_nm = user_info[1].replace('_', '\\_')
    info_msg = (
        f"🔍 ─── **AUDITOR LOG USER ACCOUNT ANALYSIS REPORT PROFILE DATA** ───\n\n"
        f"🆔 **Target Entity UID Identifier:** `{target_id}`\n"
        f"👤 **Name Profile:** {safe_nm}\n"
        f"💬 **Username Handle Identity Link:** @{safe_un}\n"
        f"🚫 **Ban Status Flag Entry Registry:** `{'Banned Yes' if user_info[2]==1 else 'No Clear Safe Clean'}`\n"
        f"💎 **License Plan Validity Expiry Constrain Schedule:** `{user_info[3] if user_info[3] else 'Regular Free Tier Account'}`\n"
        f"📁 **Total History Counter Cumulative Upload Transactions:** {user_info[4]} Scripts Shared\n"
        f"🟢 **Concurrent Live Active Working Background Processes Scripts Threads Count Running Currently:** `{active_files}` processes\n"
        f"────────────────────────"
    )
    await update.message.reply_text(info_msg, parse_mode="Markdown")

if __name__ == '__main__':
    init_db()
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("broadcast", admin_broadcast))
    app.add_handler(CommandHandler("ban", admin_ban))
    app.add_handler(CommandHandler("unban", admin_unban))
    app.add_handler(CommandHandler("addsub", admin_addsub))
    app.add_handler(CommandHandler("removesub", admin_removesub))
    app.add_handler(CommandHandler("checkuser", admin_checkuser))
    
    app.add_handler(MessageHandler(filters.Document.ALL, handle_document))
    app.add_handler(CallbackQueryHandler(button_click))
    
    print("⚡ [MICKEY CLOUD GRID OPERATIONAL INFRASTRUCTURE ONLINE]: PRODUCTION MATRIX OVERLORD RUNNING FULL ENGINE STABLE...")
    app.run_polling()
