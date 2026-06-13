#!/usr/bin/env python3

# =============================================================================
# ╔════════════════════════════════════════════════════════════════════════════╗
# ║                                                                            ║
# ║         ██╗  ██╗ █████╗ ██╗    ██╗███████╗ █████╗ ██████╗                ║
# ║         ██║ ██╔╝██╔══██╗██║    ██║██╔════╝██╔══██╗██╔══██╗               ║
# ║         █████╔╝ ███████║██║ █╗ ██║███████╗███████║██████╔╝               ║
# ║         ██╔═██╗ ██╔══██║██║███╗██║╚════██║██╔══██║██╔══██╗               ║
# ║         ██║  ██╗██║  ██║╚███╔███╔╝███████║██║  ██║██║  ██║               ║
# ║         ╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝               ║
# ║                                                                            ║
# ║                    KAWSAR ULTIMATE GENERATOR v12.0                        ║
# ║              THE MOST ADVANCED ACCOUNT GENERATOR                         ║
# ║                    WITH ULTIMATE ADMIN CONTROL                            ║
# ║                                                                            ║
# ║         CREDIT: KAWSAR  |  GITHUB: https://github.com/KAWSAR             ║
# ║              TELEGRAM: @KAWSAR | @KAWSAR                                  ║
# ║                                                                            ║
# ║         WATERMARKS: ULTIMATE_PROTECTION_v12 SA_GEN_2025                  ║
# ║            PROTECTED_BY_KAWSAR ADMIN_CONTROL_SYSTEM                      ║
# ║                    OWNER_VERIFICATION OWNER MODE                          ║
# ╚════════════════════════════════════════════════════════════════════════════╝
# =============================================================================

import hmac
import hashlib
import requests
import string
import random
import json
import codecs
import time
from datetime import datetime
import os
import sys
import base64
import signal
import threading
import psutil
import re
import subprocess
import importlib
import logging
import warnings
import urllib3
import shutil
import inspect
import platform
import getpass
import asyncio

# Disable warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
warnings.filterwarnings("ignore")

# =============================================================================
# 🛡️ ULTIMATE ANTI-CREDIT & FILENAME PROTECTION SYSTEM
# =============================================================================

class SecurityShield:
    """Security checks removed"""
    @classmethod
    def verify_filename(cls): return True
    @classmethod
    def verify_credits(cls): return True, "OK"
    @classmethod
    def show_breach(cls, reason): pass

# =============================================================================
# 🎨 ULTIMATE VISUAL MASTER - DARK GOLD THEME
# =============================================================================

class VisualMaster:
    """Professional visual design system - Dark Gold Cinema UI"""

    COLORS = {
        # ── Cyan gradient palette ──────────────────────────────────────────
        'primary':   '\033[38;5;51m',    # #00ffff  bright cyan
        'secondary': '\033[38;5;45m',    # #00d7ff  sky cyan
        'success':   '\033[38;5;50m',    # #00ffd7  cyan-mint
        'error':     '\033[38;5;196m',   # red  (rare box)
        'warning':   '\033[38;5;226m',   # yellow (box value)
        'rare':      '\033[38;5;46m',    # green  (couples box)
        'couple':    '\033[38;5;46m',    # green
        'info':      '\033[38;5;87m',    # #5fffff  pale cyan
        'highlight': '\033[38;5;123m',   # #87ffff  ice cyan
        'dim':       '\033[38;5;37m',    # #00afaf  teal
        'owner':     '\033[38;5;51m',
        'admin':     '\033[38;5;45m',
        'user':      '\033[38;5;50m',
        'border':    '\033[38;5;51m',
        'accent':    '\033[38;5;159m',   # #afffff soft cyan
        'reset':     '\033[0m',
        'bold':      '\033[1m',
        'italic':    '\033[3m',
        'bg_dark':   '\033[48;5;16m',
        # ── vivid box-content colors ───────────────────────────────────────
        'box_red':   '\033[38;5;203m',   # salmon-red
        'box_yellow':'\033[38;5;220m',   # gold-yellow
        'box_green': '\033[38;5;82m',    # lime-green
        'box_blue':  '\033[38;5;39m',    # dodger-blue
        'box_white': '\033[38;5;255m',   # pure white
        'box_purple':'\033[38;5;141m',   # soft purple
        'c1':        '\033[38;5;51m',    # cyan shades for gradient
        'c2':        '\033[38;5;45m',
        'c3':        '\033[38;5;44m',
        'c4':        '\033[38;5;38m',
        'c5':        '\033[38;5;37m',
        'c6':        '\033[38;5;36m',
    }

    ICONS = {
        'success': '✅', 'error': '❌', 'warning': '⚠️',  'info': 'ℹ️',
        'rare': '💎',    'couple': '💑', 'fire': '🔥',    'rocket': '🚀',
        'lock': '🔒',    'key': '🔑',   'shield': '🛡️',  'user': '👤',
        'id': '🆔',      'pass': '🔐',  'time': '⏱️',    'speed': '⚡',
        'target': '🎯',  'folder': '📁','stats': '📊',   'globe': '🌍',
        'thread': '🧵',  'crown': '👑', 'star': '⭐',    'heart': '❤️',
        'admin': '👑',   'owner': '💎', 'user_icon': '👤','edit': '✏️',
        'save': '💾',    'config': '⚙️','custom': '🎨',  'credit': '📝',
        'sword': '⚔️',  'diamond': '🔷',
    }

    BOX = {
        'tl': '╔', 'tr': '╗', 'bl': '╚', 'br': '╝', 'h': '═', 'v': '║',
        'ml': '╠', 'mr': '╣',
    }

    @classmethod
    def center_text(cls, text, width=None):
        if width is None:
            width = shutil.get_terminal_size().columns
        return text.center(width)

    @classmethod
    def create_box(cls, title=None, width=70, height=1):
        lines = []
        C = cls.COLORS
        if title:
            top = f"{C['border']}{cls.BOX['tl']}{cls.BOX['h'] * 2} {C['primary']}{C['bold']}{title}{C['reset']}{C['border']} {cls.BOX['h'] * 2}{cls.BOX['tr']}{C['reset']}"
        else:
            top = f"{C['border']}{cls.BOX['tl']}{cls.BOX['h'] * (width-2)}{cls.BOX['tr']}{C['reset']}"
        lines.append(top)
        for _ in range(height - 1):
            lines.append(f"{C['border']}{cls.BOX['v']}{' ' * (width-2)}{cls.BOX['v']}{C['reset']}")
        bottom = f"{C['border']}{cls.BOX['bl']}{cls.BOX['h'] * (width-2)}{cls.BOX['br']}{C['reset']}"
        lines.append(bottom)
        return lines

    @classmethod
    def create_panel(cls, title, content, width=None, color='primary'):
        if width is None:
            width = shutil.get_terminal_size().columns - 4
        C = cls.COLORS
        lines_content = content.split('\n')
        result = []
        result.append(f"{C['border']}{cls.BOX['tl']}{cls.BOX['h'] * 2} {C[color]}{C['bold']}{title}{C['reset']}{C['border']} {cls.BOX['h'] * max(0, width - len(title) - 6)}{cls.BOX['tr']}{C['reset']}")
        result.append(f"{C['border']}{cls.BOX['v']}{C['reset']}{' ' * (width - 2)}{C['border']}{cls.BOX['v']}{C['reset']}")
        for line in lines_content:
            visible_line = re.sub(r'\033\[[0-9;]*m', '', line)
            pad = max(0, width - len(visible_line) - 4)
            result.append(f"{C['border']}{cls.BOX['v']}{C['reset']}  {C['accent']}{line}{C['reset']}{' ' * pad}  {C['border']}{cls.BOX['v']}{C['reset']}")
        result.append(f"{C['border']}{cls.BOX['v']}{C['reset']}{' ' * (width - 2)}{C['border']}{cls.BOX['v']}{C['reset']}")
        result.append(f"{C['border']}{cls.BOX['bl']}{cls.BOX['h'] * (width - 2)}{cls.BOX['br']}{C['reset']}")
        return '\n'.join(result)

    @classmethod
    def create_progress_bar(cls, current, total, width=50):
        C = cls.COLORS
        percent = current / total if total > 0 else 0
        filled = int(width * percent)
        bar = f"{C['primary']}{'█' * filled}{C['dim']}{'░' * (width - filled)}{C['reset']}"
        return f"{bar} {C['bold']}{C['warning']}{percent*100:5.1f}%{C['reset']}"

    @classmethod
    def clear(cls):
        os.system('cls' if os.name == 'nt' else 'clear')

    _header_shown = False   # show once, never clear

    @classmethod
    def show_header(cls, user_level="USER"):
        if not cls._header_shown:
            cls.clear()
            cls.animate_header(user_level)
            cls._header_shown = True
        # After first show: do NOT clear — boxes must stack permanently

    @classmethod
    def animate_header(cls, user_level="USER"):
        """Epic cyan launch animation → permanent ASCII header (no clear after this)"""
        import sys, time, shutil as _sh
        W   = _sh.get_terminal_size().columns
        C   = cls.COLORS
        R   = C['reset'];  B = C['bold']

        # ── shades list for gradient ──────────────────────────────────────
        SH = [C['c1'],C['c2'],C['c3'],C['c4'],C['c5'],C['c6'],
              C['c5'],C['c4'],C['c3'],C['c2'],C['c1']]

        # ══ PHASE 1: matrix rain effect (top 5 lines) ════════════════════
        import random, string as _str
        rand_chars = list("▓▒░│┼╬╪╫╬▓▒░╔═╗║╚╝╠╣╦╩╬")
        for frame in range(18):
            line = "".join(random.choice(rand_chars) for _ in range(W-2))
            shade = SH[frame % len(SH)]
            sys.stdout.write(f"\r{shade}{B}{line}{R}")
            sys.stdout.flush()
            time.sleep(0.035)
        print()

        # ══ PHASE 2: expanding border ════════════════════════════════════
        for i in range(0, W-2, 6):
            bar = "═" * min(i, W-2)
            sys.stdout.write(f"\r{C['c1']}{B}╔{bar}>{R}")
            sys.stdout.flush()
            time.sleep(0.018)
        sys.stdout.write(f"\r{C['c1']}{B}╔{'═'*(W-2)}╗{R}\n")
        sys.stdout.flush()

        # ══ PHASE 3: KAWSAR ASCII art (typed letter-by-letter effect) ════
        KAWSAR = [
            " ██╗  ██╗ █████╗ ██╗    ██╗███████╗ █████╗ ██████╗  ",
            " ██║ ██╔╝██╔══██╗██║    ██║██╔════╝██╔══██╗██╔══██╗ ",
            " █████╔╝ ███████║██║ █╗ ██║███████╗███████║██████╔╝  ",
            " ██╔═██╗ ██╔══██║██║███╗██║╚════██║██╔══██║██╔══██╗  ",
            " ██║  ██╗██║  ██║╚███╔███╔╝███████║██║  ██║██║  ██║  ",
            " ╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝  ",
        ]
        for i, line in enumerate(KAWSAR):
            shade = SH[i % len(SH)]
            # reveal chars left→right
            for end in range(1, len(line)+1, 4):
                sys.stdout.write(f"\r{shade}{B}{line[:end].center(W)}{R}")
                sys.stdout.flush()
                time.sleep(0.006)
            sys.stdout.write(f"\r{shade}{B}{line.center(W)}{R}\n")
            sys.stdout.flush()

        # ══ PHASE 4: wave separator ═══════════════════════════════════════
        waves = ["≋"*(W-4), "〰"*((W-4)//2), "━"*(W-4), "═"*(W-4)]
        for w in waves:
            sys.stdout.write(f"\r{C['c2']}{B}  {w}  {R}")
            sys.stdout.flush()
            time.sleep(0.05)
        print()

        # ══ PHASE 5: CODEX ASCII art ══════════════════════════════════════
        CODEX = [
            "  ██████╗ ██████╗ ██████╗ ███████╗██╗  ██╗  ",
            " ██╔════╝██╔═══██╗██╔══██╗██╔════╝╚██╗██╔╝  ",
            " ██║     ██║   ██║██║  ██║█████╗   ╚███╔╝   ",
            " ██║     ██║   ██║██║  ██║██╔══╝   ██╔██╗   ",
            " ╚██████╗╚██████╔╝██████╔╝███████╗██╔╝ ██╗  ",
            "  ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝  ",
        ]
        for i, line in enumerate(CODEX):
            shade = SH[(i+3) % len(SH)]
            for end in range(1, len(line)+1, 4):
                sys.stdout.write(f"\r{shade}{B}{line[:end].center(W)}{R}")
                sys.stdout.flush()
                time.sleep(0.006)
            sys.stdout.write(f"\r{shade}{B}{line.center(W)}{R}\n")
            sys.stdout.flush()

        # ══ PHASE 6: spinning loader ══════════════════════════════════════
        spin = ["◐","◓","◑","◒","◐","◓","◑","◒","●","○","●"]
        for s in spin:
            sys.stdout.write(f"\r{C['c1']}{B}  {s}  KAWSAR CODEX  {s}  {R}")
            sys.stdout.flush()
            time.sleep(0.07)
        print()

        # ══ PHASE 7: info bar ═════════════════════════════════════════════
        if user_level == "OWNER":
            lv = f"👑 OWNER MODE"; lc = C['c1']
        elif user_level == "ADMIN":
            lv = f"⚡ ADMIN MODE"; lc = C['c2']
        else:
            lv = f"👤 USER MODE"; lc = C['c3']

        info = f"◈  OB53 READY  ·  {lv}  ·  v12  ◈"
        print(f"{lc}{B}{info.center(W)}{R}")
        feat = "⚡ GENERATOR   💎 RARE FINDER   💑 COUPLES   🔥 ACTIVATOR"
        print(f"{C['c4']}{feat.center(W)}{R}")
        cred = "📱 @KAWSAR  |  @KAWSAR  |  🐙 github.com/KAWSAR"
        print(f"{C['c5']}{cred.center(W)}{R}")

        # bottom border
        sys.stdout.write(f"\r{C['c1']}{B}╚{'═'*(W-2)}╝{R}\n\n")
        sys.stdout.flush()

        # ══ PHASE 8: progress bar "LAUNCHING..." ══════════════════════════
        bar_w = min(50, W-20)
        for i in range(bar_w+1):
            filled = "█" * i
            empty  = "░" * (bar_w - i)
            pct    = int(i / bar_w * 100)
            shade  = SH[i % len(SH)]
            sys.stdout.write(f"\r  {C['c2']}LAUNCHING {shade}{B}[{filled}{C['dim']}{empty}{shade}] {pct:3d}%{R}  ")
            sys.stdout.flush()
            time.sleep(0.022)
        print(f"\n  {C['c1']}{B}✔  KAWSAR CODEX READY!{R}\n")


# Initialize Visual Master
VISUAL = VisualMaster()


# Run filename and credit checks first

USER_LEVEL = "OWNER"  # password system removed

# =============================================================================
# ⚡ FAST REQUIREMENTS INSTALLER
# =============================================================================

def install_requirements():
    required = ['requests', 'pycryptodome', 'colorama', 'psutil', 'protobuf']
    print(f"{VISUAL.COLORS['info']}🔧 Checking requirements...{VISUAL.COLORS['reset']}")
    for pkg in required:
        try:
            if pkg == 'pycryptodome':
                import Crypto
            elif pkg == 'requests':
                import requests
            elif pkg == 'colorama':
                from colorama import Fore, Style, init
            elif pkg == 'psutil':
                import psutil
            elif pkg == 'protobuf':
                import google.protobuf
            print(f"{VISUAL.COLORS['success']}✅ {pkg} already installed{VISUAL.COLORS['reset']}")
        except ImportError:
            print(f"{VISUAL.COLORS['info']}📦 Installing {pkg}...{VISUAL.COLORS['reset']}")
            try:
                process = subprocess.Popen(
                    [sys.executable, '-m', 'pip', 'install', '--no-cache-dir', pkg, '-q'],
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE
                )
                try:
                    stdout, stderr = process.communicate(timeout=30)
                    if process.returncode == 0:
                        print(f"{VISUAL.COLORS['success']}✅ {pkg} installed{VISUAL.COLORS['reset']}")
                except subprocess.TimeoutExpired:
                    process.kill()
                    print(f"{VISUAL.COLORS['warning']}⚠️ {pkg} timeout, continuing...{VISUAL.COLORS['reset']}")
            except:
                print(f"{VISUAL.COLORS['warning']}⚠️ {pkg} install failed, continuing...{VISUAL.COLORS['reset']}")
            time.sleep(1)
    try:
        from colorama import Fore, Style, init
        init(autoreset=True)
    except:
        pass
    time.sleep(1)

install_requirements()

# Import crypto
try:
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad
    AES_AVAILABLE = True
except:
    AES_AVAILABLE = False
    def aes_encrypt(data): return data.encode() if isinstance(data, str) else data

# Import updated protobuf modules from genapi zip
try:
    import MajoRLoGinrEq_pb2
    import MajoRLoGinrEs_pb2
    import PorTs_pb2
    NEW_PROTO_AVAILABLE = True
except ImportError:
    NEW_PROTO_AVAILABLE = False

# =============================================================================
# ⚙️ CONFIGURATION
# =============================================================================

class Config:
    VERSION = "12.0 ULTIMATE ADMIN CONTROL"
    MAX_THREADS = min(psutil.cpu_count() * 2, 16)
    USER_LEVEL = USER_LEVEL

    SUCCESS = 0; RARE = 0; COUPLES = 0; ACTIVATED = 0; FAILED = 0; BIO = 0; ATTEMPTS = 0
    LOCK = threading.Lock()
    FILE_LOCKS = {}

    EXIT = False
    AUTO_ACT = True
    AUTO_BIO = True
    MAX_RETRIES = 5 if USER_LEVEL == "USER" else 10

    CUSTOM_NAME_PREFIX = "KAWSAR"
    CUSTOM_PASS_PREFIX = "KAWSAR"
    CUSTOM_RARITY_THRESHOLD = 3
    CUSTOM_TARGET = 999999999
    CURRENT_JSON_BASE = "accounts"
    CURRENT_ACTIVATED_BASE = "accounts-activated"

    if USER_LEVEL in ["ADMIN", "OWNER"]:
        DEBUG_MODE = True
        VERBOSE_LOGGING = True
        MAX_THREADS = min(psutil.cpu_count() * 4, 32)
        CAN_EDIT_CREDITS = True
    else:
        DEBUG_MODE = False
        VERBOSE_LOGGING = False
        CAN_EDIT_CREDITS = False

    if USER_LEVEL == "OWNER":
        BYPASS_RATE_LIMIT = True
        FORCE_GENERATION = True
        CUSTOM_API_PRIORITY = True
    else:
        BYPASS_RATE_LIMIT = False
        FORCE_GENERATION = False
        CUSTOM_API_PRIORITY = False

    RARITY_THRESHOLD = 3

    BIO_TEXT = "[FF0000]🌈[FF7700]K[FFFF00]A[00FF00]W[00BFFF]S[8B00FF]A[FF0000]R[FF7700]_[FFFF00]C[00FF00]O[00BFFF]D[8B00FF]E[FF0000]X [FF7700]C[FFFF00]R[00FF00]E[00BFFF]A[8B00FF]T[FF0000]I[FF7700]O[FFFF00]N[FF0000]🌈"

    REGION_LANG = {
        "ME": "ar", "IND": "hi", "ID": "id", "VN": "vi", "TH": "th",
        "BD": "bn", "PK": "ur", "TW": "zh", "CIS": "ru", "SAC": "es", "BR": "pt"
    }

    ACTIVATION_REGIONS = {
        'IND': {'guest_url': 'https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant',
                'major_login_url': 'https://loginbp.common.ggbluefox.com/MajorLogin',
                'get_login_data_url': 'https://client.ind.freefiremobile.com/GetLoginData',
                'client_host': 'client.ind.freefiremobile.com'},
        'BD':  {'guest_url': 'https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant',
                'major_login_url': 'https://loginbp.ggblueshark.com/MajorLogin',
                'get_login_data_url': 'https://clientbp.ggblueshark.com/GetLoginData',
                'client_host': 'clientbp.ggblueshark.com'},
        'PK':  {'guest_url': 'https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant',
                'major_login_url': 'https://loginbp.ggblueshark.com/MajorLogin',
                'get_login_data_url': 'https://clientbp.ggblueshark.com/GetLoginData',
                'client_host': 'clientbp.ggblueshark.com'},
        'ID':  {'guest_url': 'https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant',
                'major_login_url': 'https://loginbp.ggblueshark.com/MajorLogin',
                'get_login_data_url': 'https://clientbp.ggblueshark.com/GetLoginData',
                'client_host': 'clientbp.ggblueshark.com'},
        'TH':  {'guest_url': 'https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant',
                'major_login_url': 'https://loginbp.ggblueshark.com/MajorLogin',
                'get_login_data_url': 'https://clientbp.common.ggbluefox.com/GetLoginData',
                'client_host': 'clientbp.common.ggbluefox.com'},
        'VN':  {'guest_url': 'https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant',
                'major_login_url': 'https://loginbp.ggblueshark.com/MajorLogin',
                'get_login_data_url': 'https://clientbp.ggblueshark.com/GetLoginData',
                'client_host': 'clientbp.ggblueshark.com'},
        'ME':  {'guest_url': 'https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant',
                'major_login_url': 'https://loginbp.common.ggbluefox.com/MajorLogin',
                'get_login_data_url': 'https://clientbp.ggblueshark.com/GetLoginData',
                'client_host': 'clientbp.ggblueshark.com'},
        'BR':  {'guest_url': 'https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant',
                'major_login_url': 'https://loginbp.ggblueshark.com/MajorLogin',
                'get_login_data_url': 'https://clientbp.ggblueshark.com/GetLoginData',
                'client_host': 'clientbp.ggblueshark.com'},
    }

    # ── OB53 FIXED API CONFIGURATION ──────────────────────────────────────────
    # NEW: /api/v2/ endpoint + JSON body (from ob53new.zip main.py)
    HEX_KEY = "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3"
    API_KEY  = bytes.fromhex(HEX_KEY)

    REGISTER_URL      = "https://100067.connect.garena.com/api/v2/oauth/guest:register"
    TOKEN_URL         = "https://100067.connect.garena.com/api/v2/oauth/guest/token:grant"
    MAJOR_REGISTER_URL = "https://loginbp.ggpolarbear.com/MajorRegister"
    MAJOR_LOGIN_URL    = "https://loginbp.ggpolarbear.com/MajorLogin"
    # ──────────────────────────────────────────────────────────────────────────

    CURRENT_DIR            = os.path.dirname(os.path.abspath(__file__))
    BASE_FOLDER            = os.path.join(CURRENT_DIR, "KAWSARxGUEST-GEN")
    TOKENS_FOLDER          = os.path.join(BASE_FOLDER, "TOKENS")
    ACCOUNTS_FOLDER        = os.path.join(BASE_FOLDER, "ACCOUNTS")
    RARE_ACCOUNTS_FOLDER   = os.path.join(BASE_FOLDER, "RARE_ACCOUNTS")
    COUPLES_ACCOUNTS_FOLDER= os.path.join(BASE_FOLDER, "COUPLES_ACCOUNTS")
    GHOST_FOLDER           = os.path.join(BASE_FOLDER, "GHOST")
    GHOST_ACCOUNTS_FOLDER  = os.path.join(GHOST_FOLDER, "ACCOUNTS")
    GHOST_RARE_FOLDER      = os.path.join(GHOST_FOLDER, "RARE_ACCOUNTS")
    GHOST_COUPLES_FOLDER   = os.path.join(GHOST_FOLDER, "COUPLES_ACCOUNTS")
    ACTIVATED_FOLDER       = os.path.join(BASE_FOLDER, "ACTIVATED")
    FAILED_ACTIVATION_FOLDER = os.path.join(BASE_FOLDER, "FAILED_ACTIVATION")
    CONFIG_FOLDER          = os.path.join(BASE_FOLDER, "CONFIG")
    BACKUP_FOLDER          = os.path.join(BASE_FOLDER, "BACKUP")

    @classmethod
    def create_folders(cls):
        folders = [
            cls.BASE_FOLDER, cls.TOKENS_FOLDER, cls.ACCOUNTS_FOLDER,
            cls.RARE_ACCOUNTS_FOLDER, cls.COUPLES_ACCOUNTS_FOLDER,
            cls.GHOST_FOLDER, cls.GHOST_ACCOUNTS_FOLDER, cls.GHOST_RARE_FOLDER,
            cls.GHOST_COUPLES_FOLDER, cls.ACTIVATED_FOLDER,
            cls.FAILED_ACTIVATION_FOLDER, cls.CONFIG_FOLDER, cls.BACKUP_FOLDER
        ]
        print(f"{VISUAL.COLORS['info']}📁 Creating folders...{VISUAL.COLORS['reset']}")
        for folder in folders:
            os.makedirs(folder, exist_ok=True)
        print(f"{VISUAL.COLORS['success']}✅ Folders ready!{VISUAL.COLORS['reset']}")
        time.sleep(1)

# =============================================================================
# 🔑 ACCOUNT GENERATION HELPERS
# =============================================================================

def generate_exponent_number():
    exponent_digits = {'0': '⁰','1': '¹','2': '²','3': '³','4': '⁴',
                       '5': '⁵','6': '⁶','7': '⁷','8': '⁸','9': '⁹'}
    number = random.randint(1, 99999)
    return ''.join(exponent_digits[d] for d in f"{number:05d}")

def generate_random_name():
    base = Config.CUSTOM_NAME_PREFIX if Config.CUSTOM_NAME_PREFIX else "KAWSAR"
    # All confirmed game-compatible designs (300M+ unique combos)
    designs = [
        # confirmed set 1
        '▲','ℳ','☆','°','ℛ','『','ツ',
        '◇','༺','◆','웃','꧁','彡','★','ン',
        # confirmed set 2
        '•','乂','⍤','유','ヅ','Ø','♪','Ƹ','⌂','シ','⊹',
        # extra game-safe specials
        '·','∞','♡','✦','✧','◈','▸','꧂','༻','࿐',
        'ʜ','ɪ','ᴋ','ᴍ','ɴ','ꪆ','ꪀ','』','「','」',
        '〖','〗','【','】','《','》','ッ','ジ','ヅ','亗',
        'ℳ','ℛ','Ɽ','Ƈ','Ƨ','Ƴ','Ʀ','Ƶ','⋆','⋈',
    ]
    # deduplicate
    designs = list(dict.fromkeys(designs))
    count = random.randint(3, 4)
    suffix = ''.join(random.choices(designs, k=count))
    return f"{base}{suffix}"

def generate_custom_password():
    """OB53: full 64-char hex password"""
    return ''.join(random.choice('0123456789ABCDEF') for _ in range(64))

def smart_delay():
    time.sleep(random.uniform(0.1, 0.3))

def encode_string(original):
    keystream = [0x30,0x30,0x30,0x32,0x30,0x31,0x37,0x30,0x30,0x30,0x30,0x30,0x32,0x30,0x31,0x37,
                 0x30,0x30,0x30,0x30,0x30,0x32,0x30,0x31,0x37,0x30,0x30,0x30,0x30,0x30,0x32,0x30]
    encoded = ""
    for i in range(len(original)):
        encoded += chr(ord(original[i]) ^ keystream[i % len(keystream)])
    return {"open_id": original, "field_14": encoded}

def to_unicode_escaped(s):
    return ''.join(c if 32 <= ord(c) <= 126 else '\\u{:04x}'.format(ord(c)) for c in s)

def decode_jwt_token(jwt_token):
    try:
        parts = jwt_token.split('.')
        if len(parts) >= 2:
            payload_part = parts[1]
            padding = 4 - len(payload_part) % 4
            if padding != 4:
                payload_part += '=' * padding
            decoded = base64.urlsafe_b64decode(payload_part)
            data = json.loads(decoded)
            account_id = data.get('account_id') or data.get('external_id')
            if account_id:
                return str(account_id)
    except:
        pass
    return "N/A"

# =============================================================================
# 🔐 ASYNC PROTOBUF HELPERS (from ob53new.zip)
# =============================================================================

async def EnC_Vr(N):
    if N < 0: return b''
    H = []
    while True:
        BesTo = N & 0x7F
        N >>= 7
        if N: BesTo |= 0x80
        H.append(BesTo)
        if not N: break
    return bytes(H)

async def CrEaTe_VarianT(field_number, value):
    return await EnC_Vr((field_number << 3) | 0) + await EnC_Vr(value)

async def CrEaTe_LenGTh(field_number, value):
    h = await EnC_Vr((field_number << 3) | 2)
    e = value.encode() if isinstance(value, str) else value
    return h + await EnC_Vr(len(e)) + e

async def CrEaTe_ProTo(fields):
    p = bytearray()
    for f, v in fields.items():
        if isinstance(v, dict):
            p.extend(await CrEaTe_LenGTh(f, await CrEaTe_ProTo(v)))
        elif isinstance(v, int):
            p.extend(await CrEaTe_VarianT(f, v))
        elif isinstance(v, (str, bytes)):
            p.extend(await CrEaTe_LenGTh(f, v))
    return p

def run_async(coro):
    """Run a coroutine from synchronous code safely (thread-safe)."""
    loop = asyncio.new_event_loop()
    try:
        return loop.run_until_complete(coro)
    finally:
        loop.close()

def E_AEs(Pc):
    if not AES_AVAILABLE:
        return bytes.fromhex(Pc)
    Z = bytes.fromhex(Pc)
    key = bytes([89,103,38,116,99,37,68,69,117,104,54,37,90,99,94,56])
    iv  = bytes([54,111,121,90,68,114,50,50,69,51,121,99,104,106,77,37])
    K = AES.new(key, AES.MODE_CBC, iv)
    return K.encrypt(pad(Z, AES.block_size))

def encrypt_api(plain_text):
    if not AES_AVAILABLE:
        return plain_text
    Z = bytes.fromhex(plain_text)
    key = bytes([89,103,38,116,99,37,68,69,117,104,54,37,90,99,94,56])
    iv  = bytes([54,111,121,90,68,114,50,50,69,51,121,99,104,106,77,37])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.encrypt(pad(Z, AES.block_size)).hex()

# =============================================================================
# 🔌 API MASTER  (OB53 — new /api/v2/ JSON endpoints)
# =============================================================================

class APIMaster:
    HEX_KEY  = Config.HEX_KEY
    API_KEY  = Config.API_KEY
    API_POOL = [{"id": "100067", "key": Config.API_KEY, "label": f"API {i:02d} ⚡"} for i in range(1, 8)]

    @classmethod
    def init(cls):
        more_ids = ["100068","100069","100070","100071","100072"]
        for i, api_id in enumerate(more_ids, start=len(cls.API_POOL)+1):
            cls.API_POOL.append({"id": api_id, "key": cls.API_KEY, "label": f"API {i:02d} ⚡"})
        return len(cls.API_POOL)

API_COUNT = APIMaster.init()

# =============================================================================
# 📝 CREDIT EDITOR (ADMIN ONLY)
# =============================================================================

class CreditEditor:
    CREDIT_FILE = os.path.join(Config.CONFIG_FOLDER, "credit_config.json")

    @classmethod
    def load_credits(cls):
        default_credits = {
            "primary_credit": "KAWSAR",
            "github": "https://github.com/KAWSAR",
            "telegram1": "@KAWSAR",
            "telegram2": "@KAWSAR",
            "display_name": "KAWSAR",
            "banner_text": "⚡ POWERED BY KAWSAR ⚡",
            "footer_text": "👤 CREDIT: KAWSAR | TELEGRAM: @KAWSAR,@KAWSAR | GITHUB: KAWSAR",
            "bio_text": "[FF0000]🌈[FF7700]K[FFFF00]A[00FF00]W[00BFFF]S[8B00FF]A[FF0000]R[FF7700]_[FFFF00]C[00FF00]O[00BFFF]D[8B00FF]E[FF0000]X [FF7700]C[FFFF00]R[00FF00]E[00BFFF]A[8B00FF]T[FF0000]I[FF7700]O[FFFF00]N[FF0000]🌈",
            "last_modified": datetime.now().isoformat(),
            "modified_by": Config.USER_LEVEL
        }
        try:
            if os.path.exists(cls.CREDIT_FILE):
                with open(cls.CREDIT_FILE, 'r') as f:
                    return json.load(f)
            else:
                cls.save_credits(default_credits)
                return default_credits
        except:
            return default_credits

    @classmethod
    def save_credits(cls, credits):
        try:
            credits["last_modified"] = datetime.now().isoformat()
            credits["modified_by"] = Config.USER_LEVEL
            os.makedirs(os.path.dirname(cls.CREDIT_FILE), exist_ok=True)
            with open(cls.CREDIT_FILE, 'w') as f:
                json.dump(credits, f, indent=4)
            return True
        except:
            return False

    @classmethod
    def backup_current_file(cls):
        try:
            backup_name = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py"
            backup_path = os.path.join(Config.BACKUP_FOLDER, backup_name)
            shutil.copy2(__file__, backup_path)
            return backup_path
        except:
            return None

# =============================================================================
# 🔐 FILE LOCK / JSON
# =============================================================================

def get_file_lock(filename):
    if filename not in Config.FILE_LOCKS:
        Config.FILE_LOCKS[filename] = threading.Lock()
    return Config.FILE_LOCKS[filename]

def safe_json_save(filepath, data):
    try:
        parent = os.path.dirname(filepath)
        if parent and not os.path.isdir(parent):
            os.makedirs(parent, exist_ok=True)
        temp = filepath + '.tmp'
        with open(temp, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        os.replace(temp, filepath) if os.path.exists(filepath) else os.rename(temp, filepath)
        return True
    except:
        return False

def safe_json_load(filepath, default=None):
    try:
        if os.path.isfile(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
    except:
        pass
    return default if default is not None else []

# =============================================================================
# 🔄 COUPLES DETECTION
# =============================================================================

POTENTIAL_COUPLES = {}
COUPLES_LOCK = threading.Lock()

# =============================================================================
# 🚦 SIGNAL HANDLING
# =============================================================================

EXIT_FLAG = False

def safe_exit(signum=None, frame=None):
    global EXIT_FLAG
    EXIT_FLAG = True
    print(f"\n{VISUAL.COLORS['warning']}🚨 Shutting down...{VISUAL.COLORS['reset']}")
    sys.exit(0)

signal.signal(signal.SIGINT, safe_exit)
signal.signal(signal.SIGTERM, safe_exit)

# =============================================================================
# 🖨️ PRINT FUNCTIONS
# =============================================================================

C = VISUAL.COLORS

# When True, background noise is silenced during generation (only boxes show)
GENERATION_SILENT = False

def print_success(msg):
    if not GENERATION_SILENT: print(f"{C['success']}{C['bold']}✅ {msg}{C['reset']}")
def print_error(msg):
    if not GENERATION_SILENT: print(f"{C['error']}{C['bold']}❌ {msg}{C['reset']}")
def print_warning(msg):
    if not GENERATION_SILENT: print(f"{C['warning']}{C['bold']}⚠️  {msg}{C['reset']}")
def print_info(msg):
    if not GENERATION_SILENT: print(f"{C['info']}ℹ️  {msg}{C['reset']}")
def print_rare(msg):
    if not GENERATION_SILENT: print(f"{C['rare']}{C['bold']}💎 {msg}{C['reset']}")
def print_couple(msg):
    if not GENERATION_SILENT: print(f"{C['couple']}{C['bold']}💑 {msg}{C['reset']}")
def print_activation(msg):
    if not GENERATION_SILENT: print(f"{C['primary']}{C['bold']}🔥 {msg}{C['reset']}")

def debug_print(msg):
    if not GENERATION_SILENT and Config.USER_LEVEL in ["ADMIN","OWNER"] and Config.DEBUG_MODE:
        print(f"{C['dim']}🔍 DEBUG: {msg}{C['reset']}")

# =============================================================================
# 🔐 BIO FUNCTION  (Direct — no external API needed)
# =============================================================================

BIO_SET_COUNTER = 0

# ── Bio protobuf descriptor (inline, no separate file needed) ─────────────────
try:
    from google.protobuf import descriptor_pool as _bio_dp
    from google.protobuf import symbol_database as _bio_sym_db
    from google.protobuf.internal import builder as _bio_builder
    _BIO_PROTO = (
        b'\n\ndata.proto\"\xbb\x01\n\x04\x44\x61ta'
        b'\x12\x0f\n\x07\x66ield_2\x18\x02 \x01(\x05'
        b'\x12\x1e\n\x07\x66ield_5\x18\x05 \x01(\x0b\x32\r.EmptyMessage'
        b'\x12\x1e\n\x07\x66ield_6\x18\x06 \x01(\x0b\x32\r.EmptyMessage'
        b'\x12\x0f\n\x07\x66ield_8\x18\x08 \x01(\t'
        b'\x12\x0f\n\x07\x66ield_9\x18\t \x01(\x05'
        b'\x12\x1f\n\x08\x66ield_11\x18\x0b \x01(\x0b\x32\r.EmptyMessage'
        b'\x12\x1f\n\x08\x66ield_12\x18\x0c \x01(\x0b\x32\r.EmptyMessage'
        b'\"\x0e\n\x0c\x45mptyMessageb\x06proto3'
    )
    _bio_builder.BuildMessageAndEnumDescriptors(
        _bio_dp.Default().AddSerializedFile(_BIO_PROTO), globals()
    )
    _bio_builder.BuildTopDescriptorsAndMessages(
        _bio_dp.Default().AddSerializedFile(_BIO_PROTO), 'bio_inline_pb2', globals()
    )
    _BioData      = _bio_sym_db.Default().GetSymbol('Data')
    _EmptyMessage = _bio_sym_db.Default().GetSymbol('EmptyMessage')
    BIO_PROTO_AVAILABLE = True
except Exception as _bio_ex:
    BIO_PROTO_AVAILABLE = False

# ── Bio server map ────────────────────────────────────────────────────────────
_BIO_SERVERS = {
    "IND": "https://client.ind.freefiremobile.com/UpdateSocialBasicInfo",
    "BD":  "https://clientbp.ggblueshark.com/UpdateSocialBasicInfo",
    "SG":  "https://clientbp.ggblueshark.com/UpdateSocialBasicInfo",
    "PK":  "https://clientbp.ggblueshark.com/UpdateSocialBasicInfo",
    "ID":  "https://clientbp.ggblueshark.com/UpdateSocialBasicInfo",
    "VN":  "https://clientbp.ggblueshark.com/UpdateSocialBasicInfo",
    "TH":  "https://clientbp.common.ggbluefox.com/UpdateSocialBasicInfo",
    "ME":  "https://clientbp.common.ggbluefox.com/UpdateSocialBasicInfo",
    "BR":  "https://client.us.freefiremobile.com/UpdateSocialBasicInfo",
    "US":  "https://client.us.freefiremobile.com/UpdateSocialBasicInfo",
    "EU":  "https://clientbp.ggpolarbear.com/UpdateSocialBasicInfo",
}

_BIO_HEADERS = {
    "Expect":          "100-continue",
    "X-Unity-Version": "2018.4.11f1",
    "X-GA":            "v1 1",
    "ReleaseVersion":  "OB53",
    "Content-Type":    "application/x-www-form-urlencoded",
    "User-Agent":      "Dalvik/2.1.0 (Linux; U; Android 11; SM-A305F Build/RP1A.200720.012)",
    "Connection":      "Keep-Alive",
    "Accept-Encoding": "gzip",
}

_BIO_AES_KEY = bytes([89,103,38,116,99,37,68,69,117,104,54,37,90,99,94,56])
_BIO_AES_IV  = bytes([54,111,121,90,68,114,50,50,69,51,121,99,104,106,77,37])

def _bio_encrypt(data_bytes):
    """AES-CBC encrypt for bio payload."""
    if not AES_AVAILABLE:
        return data_bytes
    from Crypto.Cipher import AES as _AES
    from Crypto.Util.Padding import pad as _pad
    cipher = _AES.new(_BIO_AES_KEY, _AES.MODE_CBC, _BIO_AES_IV)
    return cipher.encrypt(_pad(data_bytes, _AES.block_size))

def _bio_guest_login(uid, password):
    """Step 1: Get access_token + open_id via guest OAuth."""
    try:
        payload = {
            'uid':           str(uid),
            'password':      str(password),
            'response_type': 'token',
            'client_type':   '2',
            'client_secret': Config.HEX_KEY,
            'client_id':     '100067',
        }
        headers = {'User-Agent': 'GarenaMSDK/4.0.19P9(SM-M526B ;Android 13;pt;BR;)',
                   'Connection': 'Keep-Alive'}
        resp = requests.post(
            'https://100067.connect.garena.com/oauth/guest/token/grant',
            data=payload, headers=headers, timeout=10, verify=False
        )
        data = resp.json()
        return data.get('access_token'), data.get('open_id')
    except:
        return None, None

def _bio_major_login(access_token, open_id):
    """Step 2: Major login to get JWT token (tries multiple platform types)."""
    try:
        import my_pb2 as _my_pb2
        import output_pb2 as _out_pb2
    except ImportError:
        # Fallback: use the AutoActivator's existing login flow
        return None

    _login_headers = {
        "User-Agent":      "Dalvik/2.1.0 (Linux; U; Android 9; ASUS_Z01QD Build/PI)",
        "Connection":      "Keep-Alive",
        "Accept-Encoding": "gzip",
        "Content-Type":    "application/octet-stream",
        "Expect":          "100-continue",
        "X-Unity-Version": "2018.4.11f1",
        "X-GA":            "v1 1",
        "ReleaseVersion":  "OB53",
    }
    for p_type in [8, 3, 4, 6]:
        try:
            gd = _my_pb2.GameData()
            gd.timestamp     = "2024-12-05 18:15:32"
            gd.game_name     = "free fire"
            gd.game_version  = 1
            gd.version_code  = "1.120.2"
            gd.os_info       = "Android OS 9 / API-28"
            gd.device_type   = "Handheld"
            gd.network_provider = "Verizon Wireless"
            gd.connection_type  = "WIFI"
            gd.screen_width  = 1280
            gd.screen_height = 960
            gd.dpi           = "240"
            gd.cpu_info      = "ARMv7 VFPv3 NEON VMH | 2400 | 4"
            gd.total_ram     = 5951
            gd.gpu_name      = "Adreno (TM) 640"
            gd.gpu_version   = "OpenGL ES 3.0"
            gd.user_id       = "Google|74b585a9-0268-4ad3-8f36-ef41d2e53610"
            gd.ip_address    = "172.190.111.97"
            gd.language      = "en"
            gd.open_id       = open_id
            gd.access_token  = access_token
            gd.platform_type = p_type
            gd.field_99      = str(p_type)
            gd.field_100     = str(p_type)

            encrypted = _bio_encrypt(gd.SerializeToString())
            resp = requests.post(
                "https://loginbp.ggblueshark.com/MajorLogin",
                data=encrypted, headers=_login_headers,
                verify=False, timeout=10
            )
            if resp.status_code == 200:
                msg = _out_pb2.Garena_420()
                msg.ParseFromString(resp.content)
                token = getattr(msg, 'token', None)
                if token:
                    return token
        except:
            continue
    return None

def _bio_update(jwt_token, bio_text, region):
    """Step 3: Send encrypted protobuf bio update to FF server."""
    if not BIO_PROTO_AVAILABLE:
        return False
    try:
        url = _BIO_SERVERS.get(region.upper(), _BIO_SERVERS["IND"])
        data = _BioData()
        data.field_2 = 17
        data.field_5.CopyFrom(_EmptyMessage())
        data.field_6.CopyFrom(_EmptyMessage())
        data.field_8 = bio_text
        data.field_9 = 1
        data.field_11.CopyFrom(_EmptyMessage())
        data.field_12.CopyFrom(_EmptyMessage())

        encrypted = _bio_encrypt(data.SerializeToString())
        headers = _BIO_HEADERS.copy()
        headers['Authorization'] = f'Bearer {jwt_token}'
        r = requests.post(url, headers=headers, data=encrypted, verify=False, timeout=10)
        return r.status_code == 200
    except:
        return False

def set_account_bio(uid, password, bio_text, region="IND", existing_jwt=None):
    """
    Auto bio setter — called after each account is generated.
    Flow: JWT (already have) → UpdateSocialBasicInfo (protobuf)
    OR:   Guest OAuth → _perform_major_login_sync → UpdateSocialBasicInfo
    """
    global BIO_SET_COUNTER
    if not Config.AUTO_BIO:
        return False
    try:
        bio_to_use = Config.BIO_TEXT
        jwt_token  = existing_jwt  # use already-obtained JWT if available

        # ── If no JWT passed, do a fresh login ───────────────────────────────
        if not jwt_token:
            debug_print(f"Bio: guest login for uid={uid}")
            access_token, open_id = _bio_guest_login(uid, password)
            if not access_token or not open_id:
                debug_print("Bio: guest login failed")
                return False

            sess = requests.Session()
            login_result = _perform_major_login_sync(
                uid, password, access_token, open_id, region, sess
            )
            jwt_token = login_result.get("jwt_token", "")

        if not jwt_token:
            debug_print("Bio: could not obtain JWT")
            return False

        debug_print(f"Bio: updating bio for uid={uid}")
        success = _bio_update(jwt_token, bio_to_use, region)
        if success:
            with Config.LOCK:
                BIO_SET_COUNTER += 1
            pass  # bio set silently
            return True
        else:
            debug_print(f"Bio: update request failed for uid={uid}")
    except Exception as e:
        debug_print(f"Bio error: {e}")
    return False

# =============================================================================
# 💎 RARITY DETECTION
# =============================================================================

ACCOUNT_RARITY_PATTERNS = {
    "REPEATED_DIGITS_4":       [r"(\d)\1{3,}", 3],
    "REPEATED_DIGITS_3":       [r"(\d)\1\1(\d)\2\2", 2],
    "SEQUENTIAL_5":            [r"(12345|23456|34567|45678|56789)", 4],
    "SEQUENTIAL_4":            [r"(0123|1234|2345|3456|4567|45678|5678|6789|9876|8765|7654|6543|5432|4321|3210)", 3],
    "PALINDROME_6":            [r"^(\d)(\d)(\d)\3\2\1$", 5],
    "PALINDROME_4":            [r"^(\d)(\d)\2\1$", 3],
    "SPECIAL_COMBINATIONS_HIGH":[r"(69|420|1337|007)", 4],
    "SPECIAL_COMBINATIONS_MED": [r"(100|200|300|400|500|666|777|888|999)", 2],
    "QUADRUPLE_DIGITS":        [r"(1111|2222|3333|4444|5555|6666|7777|8888|9999|0000)", 4],
    "MIRROR_PATTERN_HIGH":     [r"^(\d{2,3})\1$", 3],
    "MIRROR_PATTERN_MED":      [r"(\d{2})0\1", 2],
    "GOLDEN_RATIO":            [r"1618|0618", 3],
}

def check_account_rarity(account_data):
    account_id = account_data.get("account_id", "")
    if account_id == "N/A" or not account_id:
        return False, None, None, 0
    rarity_score = 0
    detected_patterns = []
    for rarity_type, pattern_data in ACCOUNT_RARITY_PATTERNS.items():
        if re.search(pattern_data[0], account_id):
            rarity_score += pattern_data[1]
            detected_patterns.append(rarity_type)
    digits = [int(d) for d in account_id if d.isdigit()]
    if len(set(digits)) == 1 and len(digits) >= 4:
        rarity_score += 5; detected_patterns.append("UNIFORM_DIGITS")
    if len(digits) >= 4:
        diffs = [digits[i+1] - digits[i] for i in range(len(digits)-1)]
        if len(set(diffs)) == 1:
            rarity_score += 4; detected_patterns.append("ARITHMETIC_SEQUENCE")
    if len(account_id) <= 8 and account_id.isdigit() and int(account_id) < 1000000:
        rarity_score += 3; detected_patterns.append("LOW_ACCOUNT_ID")
    threshold = Config.CUSTOM_RARITY_THRESHOLD if Config.USER_LEVEL in ["ADMIN","OWNER"] else Config.RARITY_THRESHOLD
    if rarity_score >= threshold:
        reason = f"ID {account_id} — Score: {rarity_score} — Patterns: {', '.join(detected_patterns)}"
        return True, "RARE_ACCOUNT", reason, rarity_score
    return False, None, None, rarity_score

def check_account_couples(account_data, thread_id):
    account_id = account_data.get("account_id", "")
    if account_id == "N/A" or not account_id:
        return False, None, None
    with COUPLES_LOCK:
        for stored_id, stored_data in list(POTENTIAL_COUPLES.items()):
            couple_found, reason = check_account_couple_patterns(account_id, stored_data.get('account_id', ''))
            if couple_found:
                partner_data = stored_data
                del POTENTIAL_COUPLES[stored_id]
                return True, reason, partner_data
        POTENTIAL_COUPLES[account_id] = {
            'uid': account_data.get('uid',''), 'account_id': account_id,
            'name': account_data.get('name',''), 'password': account_data.get('password',''),
            'region': account_data.get('region',''), 'thread_id': thread_id,
            'timestamp': datetime.now().isoformat()
        }
    return False, None, None

def check_account_couple_patterns(a1, a2):
    if a1 and a2 and abs(int(a1) - int(a2)) == 1:
        return True, f"Sequential IDs: {a1} & {a2}"
    if a1 == a2[::-1]:
        return True, f"Mirror IDs: {a1} & {a2}"
    if a1 and a2:
        s = int(a1) + int(a2)
        if s % 1000 == 0 or s % 10000 == 0:
            return True, f"Complementary sum: {a1}+{a2}={s}"
    for ln in ['520','521','1314','3344']:
        if ln in a1 and ln in a2:
            return True, f"Both contain love number: {ln}"
    return False, None

def print_rarity_found(account_data, rarity_type, reason, rarity_score):
    import sys, time
    # ✅ Rare box — পুরো বক্স লাল রঙের
    RED  = '\033[38;5;196m'
    RED2 = '\033[38;5;160m'
    B = VISUAL.COLORS['bold']; R = VISUAL.COLORS['reset']
    W = 54
    for _ in range(4):
        for ch in ['░','▒','▓','█','▓','▒']:
            sys.stdout.write(f"\r{RED}{B}╔" + ch*W + f"╗{R}")
            sys.stdout.flush(); time.sleep(0.010)
    print()
    print(f"{RED}{B}╔{'═'*W}╗{R}")
    print(f"{RED}{B}║{'💎  RARE ACCOUNT FOUND!  💎'.center(W)}║{R}")
    print(f"{RED}{B}╠{'═'*W}╣{R}")
    def row(k, v):
        line = f"  {k}: {v}"
        pad  = max(0, W - len(line) - 1)
        print(f"{RED}{B}║{R}  {RED2}{k}{R}: {RED}{B}{v}{R}{' '*pad}{RED}{B}║{R}")
    row("🎯 Type   ", str(rarity_type))
    row("⭐ Score  ", str(rarity_score))
    row("👤 Name   ", account_data['name'])
    row("🆔 UID    ", str(account_data['uid']))
    row("🎮 Acct ID", account_data.get('account_id', 'N/A'))
    row("📝 Reason ", str(reason)[:45])
    print(f"{RED}{B}╠{'═'*W}╣{R}")
    print(f"{RED}{B}║{'🔴  SAVED TO RARE ACCOUNTS  🔴'.center(W)}║{R}")
    print(f"{RED}{B}╚{'═'*W}╝{R}\n")

def print_couples_found(account1, account2, reason):
    import sys, time
    # ✅ Couples box — পুরো বক্স সবুজ রঙের (দুটো account একসাথে)
    GRN  = '\033[38;5;46m'
    GRN2 = '\033[38;5;40m'
    GRN3 = '\033[38;5;34m'
    B = VISUAL.COLORS['bold']; R = VISUAL.COLORS['reset']
    W = 58
    for ch in ['·','◇','◈','═']:
        sys.stdout.write(f"\r{GRN}{B}╔" + ch*W + f"╗{R}")
        sys.stdout.flush(); time.sleep(0.022)
    print()
    print(f"{GRN}{B}╔{'═'*W}╗{R}")
    print(f"{GRN}{B}║{'💑  COUPLES ACCOUNT FOUND!  💑'.center(W)}║{R}")
    print(f"{GRN}{B}╠{'═'*W}╣{R}")
    def row(k, v):
        line = f"  {k}: {v}"
        pad  = max(0, W - len(line) - 1)
        print(f"{GRN}{B}║{R}  {GRN3}{k}{R}: {GRN}{B}{v}{R}{' '*pad}{GRN}{B}║{R}")
    row("📝 Reason  ", str(reason))
    print(f"{GRN}{B}╠{'─'*W}╣{R}")
    print(f"{GRN}{B}║{'  ACCOUNT  1  '.center(W)}║{R}")
    row("👤 Name    ", account1['name'])
    row("🆔 UID     ", str(account1.get('uid','N/A')))
    row("🎮 Acct ID ", account1.get('account_id','N/A'))
    print(f"{GRN}{B}╠{'─'*W}╣{R}")
    print(f"{GRN}{B}║{'  ACCOUNT  2  '.center(W)}║{R}")
    row("👤 Name    ", account2['name'])
    row("🆔 UID     ", str(account2.get('uid','N/A')))
    row("🎮 Acct ID ", account2.get('account_id','N/A'))
    print(f"{GRN}{B}╠{'═'*W}╣{R}")
    print(f"{GRN}{B}║{'💚  SAVED TO COUPLES FILE  💚'.center(W)}║{R}")
    print(f"{GRN}{B}╚{'═'*W}╝{R}\n")

# =============================================================================
# ⚡ AUTO ACTIVATOR
# =============================================================================

class AutoActivator:
    def __init__(self, max_workers=5, turbo_mode=True):
        self.key = bytes([89,103,38,116,99,37,68,69,117,104,54,37,90,99,94,56])
        self.iv  = bytes([54,111,121,90,68,114,50,50,69,51,121,99,104,106,77,37])
        self.max_workers = max_workers
        self.turbo_mode  = turbo_mode
        self.session = requests.Session()
        self.stop_execution = False

    def encrypt_api(self, plain_text):
        if not AES_AVAILABLE: return plain_text
        try:
            plain_text = bytes.fromhex(plain_text)
            cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
            return cipher.encrypt(pad(plain_text, AES.block_size)).hex()
        except:
            return None

    def parse_my_message(self, serialized_data):
        try:
            text = serialized_data.decode('utf-8', errors='ignore')
            jwt_start = text.find("eyJ")
            if jwt_start != -1:
                jwt_token = text[jwt_start:]
                second_dot = jwt_token.find(".", jwt_token.find(".") + 1)
                if second_dot != -1:
                    return jwt_token[:second_dot + 44], None, None
            return None, None, None
        except:
            return None, None, None

    def guest_token(self, uid, password, region='IND'):
        if self.stop_execution: return None, None
        region_config = Config.ACTIVATION_REGIONS.get(region, Config.ACTIVATION_REGIONS['IND'])
        url = region_config['guest_url']
        data = {
            "uid": f"{uid}", "password": f"{password}",
            "response_type": "token", "client_type": "2",
            "client_secret": Config.HEX_KEY, "client_id": "100067",
        }
        for attempt in range(3):
            try:
                timeout = 8 if self.turbo_mode else 15
                response = self.session.post(url, data=data, timeout=timeout, verify=False)
                if response.status_code == 200:
                    data_json = response.json()
                    return data_json.get('access_token'), data_json.get('open_id')
                elif response.status_code == 429:
                    time.sleep(2 ** attempt)
            except:
                pass
            if attempt < 2: time.sleep(1)
        return None, None

    def major_login(self, access_token, open_id, region='IND'):
        if self.stop_execution: return None
        region_config = Config.ACTIVATION_REGIONS.get(region, Config.ACTIVATION_REGIONS['IND'])
        url = region_config['major_login_url']
        headers = {
            'X-Unity-Version': '1.123.1', 'ReleaseVersion': 'OB53',
            'Content-Type': 'application/x-www-form-urlencoded', 'X-GA': 'v1 1',
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; ASUS_Z01QD Build/QKQ1.190825.002)',
            'Host': 'loginbp.ggblueshark.com', 'Connection': 'Keep-Alive',
        }
        payload_template = bytes.fromhex(
            '1a13323032352d30372d33302031313a30323a3531220966726565206669726528013a07312e3132302e32422c416e64726f6964204f5320372e312e32202f204150492d323320284e32473438482f373030323530323234294a0848616e6468656c645207416e64726f69645a045749464960c00c68840772033332307a1f41524d7637205646507633204e454f4e20564d48207c2032343635207c203480019a1b8a010f416472656e6f2028544d292036343092010d4f70656e474c20455320332e319a012b476f6f676c657c31663361643662372d636562342d343934622d383730622d623164616364373230393131a2010c3139372e312e31322e313335aa0102656eb201203939366136323964626364623339363462653662363937386635643831346462ba010134c2010848616e6468656c64ea014066663930633037656239383135616633306134336234613966363031393531366530653463373033623434303932353136643064656661346365663531663261f00101ca0207416e64726f6964d2020457494649ca03203734323862323533646566633136343031386336303461316562626665626466e003daa907e803899b07f003bf0ff803ae088004999b078804daa9079004999b079804daa907c80403d204262f646174612f6170702f636f6d2e6474732e667265656669726574682d312f6c69622f61726de00401ea044832303837663631633139663537663261663465376665666630623234643964397c2f646174612f6170702f636f6d2e6474732e667265656669726574682d312f626173652e61706bf00403f804018a050233329a050a32303139313138363933b205094f70656e474c455332b805ff7fc00504e005dac901ea0507616e64726f6964f2055c4b71734854394748625876574c6668437950416c52526873626d43676542557562555551317375746d525536634e30524f3751453141486e496474385963784d614c575437636d4851322b7374745279377830663935542b6456593d8806019006019a060134a2060134'
        )
        OLD_OPEN_ID      = b"996a629dbcdb3964be6b6978f5d814db"
        OLD_ACCESS_TOKEN = b"ff90c07eb9815af30a43b4a9f6019516e0e4c703b44092516d0defa4cef51f2a"
        payload = payload_template.replace(OLD_OPEN_ID, open_id.encode())
        payload = payload.replace(OLD_ACCESS_TOKEN, access_token.encode())
        encrypted_payload = self.encrypt_api(payload.hex())
        if not encrypted_payload: return None
        for attempt in range(3):
            try:
                timeout = 12 if self.turbo_mode else 18
                response = self.session.post(url, headers=headers, data=bytes.fromhex(encrypted_payload), verify=False, timeout=timeout)
                if response.status_code == 200 and len(response.content) > 0:
                    return response.content
            except:
                pass
            if attempt < 2: time.sleep(1)
        return None

    def GET_LOGIN_DATA(self, JWT_TOKEN, access_token, region='IND'):
        if self.stop_execution: return False
        region_config = Config.ACTIVATION_REGIONS.get(region, Config.ACTIVATION_REGIONS['IND'])
        url = region_config['get_login_data_url']
        client_host = region_config['client_host']
        try:
            token_payload_base64 = JWT_TOKEN.split('.')[1]
            token_payload_base64 += '=' * ((4 - len(token_payload_base64) % 4) % 4)
            decoded_payload = json.loads(base64.urlsafe_b64decode(token_payload_base64).decode('utf-8'))
            NEW_EXTERNAL_ID  = decoded_payload['external_id']
            SIGNATURE_MD5    = decoded_payload['signature_md5']
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            payload = bytes.fromhex("1a13323032352d30372d33302031313a30323a3531220966726565206669726528013a07312e3132302e32422c416e64726f6964204f5320372e312e32202f204150492d323320284e32473438482f373030323530323234294a0848616e6468656c645207416e64726f69645a045749464960c00c68840772033332307a1f41524d7637205646507633204e454f4e20564d48207c2032343635207c203480019a1b8a010f416472656e6f2028544d292036343092010d4f70656e474c20455320332e319a012b476f6f676c657c31663361643662372d636562342d343934622d383730622d623164616364373230393131a2010c3139372e312e31322e313335aa0102656eb201203939366136323964626364623339363462653662363937386635643831346462ba010134c2010848616e6468656c64ea014066663930633037656239383135616633306134336234613966363031393531366530653463373033623434303932353136643064656661346365663531663261f00101ca0207416e64726f6964d2020457494649ca03203734323862323533646566633136343031386336303461316562626665626466e003daa907e803899b07f003bf0ff803ae088004999b078804daa9079004999b079804daa907c80403d204262f646174612f6170702f636f6d2e6474732e667265656669726574682d312f6c69622f61726de00401ea044832303837663631633139663537663261663465376665666630623234643964397c2f646174612f6170702f636f6d2e6474732e667265656669726574682d312f626173652e61706bf00403f804018a050233329a050a32303139313138363933b205094f70656e474c455332b805ff7fc00504e005dac901ea0507616e64726f6964f2055c4b71734854394748625876574c6668437950416c52526873626d43676542557562555551317375746d525536634e30524f3751453141486e496474385963784d614c575437636d4851322b7374745279377830663935542b6456593d8806019006019a060134a2060134")
            payload = payload.replace(b"2025-07-30 11:02:51", now.encode())
            payload = payload.replace(b"ff90c07eb9815af30a43b4a9f6019516e0e4c703b44092516d0defa4cef51f2a", access_token.encode("UTF-8"))
            payload = payload.replace(b"996a629dbcdb3964be6b6978f5d814db", NEW_EXTERNAL_ID.encode("UTF-8"))
            payload = payload.replace(b"7428b253defc164018c604a1ebbfebdf", SIGNATURE_MD5.encode("UTF-8"))
            PAYLOAD = self.encrypt_api(payload.hex())
            if not PAYLOAD: return False
            final_payload = bytes.fromhex(PAYLOAD)
        except:
            return False
        headers = {
            'Expect': '100-continue', 'Authorization': f'Bearer {JWT_TOKEN}',
            'X-Unity-Version': '1.123.1', 'X-GA': 'v1 1', 'ReleaseVersion': 'OB53',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; G011A Build/PI)',
            'Host': client_host, 'Connection': 'close', 'Accept-Encoding': 'gzip, deflate, br',
        }
        for attempt in range(2):
            try:
                timeout = 8 if self.turbo_mode else 12
                response = self.session.post(url, headers=headers, data=final_payload, verify=False, timeout=timeout)
                if response.status_code == 200:
                    return True
            except:
                pass
            if attempt < 1: time.sleep(1)
        return False

    def activate_account(self, account_data):
        uid = account_data['uid']
        password = account_data['password']
        region = account_data.get('region', 'IND')
        if region not in Config.ACTIVATION_REGIONS:
            region = 'IND'
        access_token, open_id = self.guest_token(uid, password, region)
        if not access_token or not open_id: return False
        major_login_response = self.major_login(access_token, open_id, region)
        if not major_login_response: return False
        jwt_token, key, iv = self.parse_my_message(major_login_response)
        if not jwt_token: return False
        return self.GET_LOGIN_DATA(jwt_token, access_token, region)

auto_activator = AutoActivator(max_workers=5, turbo_mode=True)

# =============================================================================
# 👤 ACCOUNT CREATION  (OB53 FIXED — new endpoints + JSON body)
# =============================================================================

def create_acc(region, session, is_ghost=False):
    """
    OB53 guest registration using the NEW /api/v2/ JSON endpoints.
    Fixes the broken generation from the original KAWSARxGEN.py.
    """
    if EXIT_FLAG:
        return None

    max_attempts = Config.MAX_RETRIES

    for attempt in range(max_attempts):
        try:
            password = generate_custom_password()

            # ── STEP 1: Register (/api/v2/ JSON body) ──────────────────────────
            payload_register = json.dumps(
                {"app_id": 100067, "client_type": 2, "password": password, "source": 2},
                separators=(',', ':')
            )
            signature = hmac.new(Config.API_KEY, payload_register.encode(), hashlib.sha256).hexdigest()
            headers_reg = {
                "User-Agent": "GarenaMSDK/4.0.39(SM-A325M ;Android 13;en;HK;)",
                "Authorization": f"Signature {signature}",
                "Content-Type": "application/json; charset=utf-8",
                "Accept": "application/json",
                "Connection": "Keep-Alive",
                "Host": "100067.connect.garena.com",
            }
            debug_print(f"Register attempt {attempt+1}")
            resp_reg = session.post(
                Config.REGISTER_URL,
                headers=headers_reg,
                data=payload_register,
                timeout=15,
                verify=False
            )
            if resp_reg.status_code != 200:
                if resp_reg.status_code == 429:
                    time.sleep(2 ** attempt)
                continue
            reg_json = resp_reg.json()
            if reg_json.get("code") != 0:
                debug_print(f"Register error code: {reg_json}")
                continue
            uid = reg_json['data']['uid']
            # Guest registered — silent
            smart_delay()
            with Config.LOCK:
                Config.ATTEMPTS += 1

            # ── STEP 2: Token (/api/v2/ JSON body) ─────────────────────────────
            payload_token = json.dumps({
                "client_id": 100067,
                "client_secret": Config.HEX_KEY,
                "client_type": 2,
                "password": password,
                "response_type": "token",
                "uid": uid,
            }, separators=(',', ':'))
            signature2 = hmac.new(Config.API_KEY, payload_token.encode(), hashlib.sha256).hexdigest()
            headers_tok = {
                "User-Agent": "GarenaMSDK/4.0.39(SM-A325M ;Android 13;en;HK;)",
                "Authorization": f"Signature {signature2}",
                "Content-Type": "application/json; charset=utf-8",
                "Accept": "application/json",
                "Connection": "Keep-Alive",
                "Host": "100067.connect.garena.com",
            }
            resp_tok = session.post(
                Config.TOKEN_URL,
                headers=headers_tok,
                data=payload_token,
                timeout=15,
                verify=False
            )
            if resp_tok.status_code != 200:
                continue
            tok_json = resp_tok.json()
            if tok_json.get("code") != 0:
                debug_print(f"Token error: {tok_json}")
                continue
            access_token = tok_json['data']['access_token']
            open_id      = tok_json['data']['open_id']
            # Token granted — silent
            smart_delay()
            with Config.LOCK:
                Config.ATTEMPTS += 1

            # ── STEP 3: MajorRegister (ggpolarbear.com, sync) ────────────
            name = generate_random_name()
            api_config = {"id": "100067", "key": Config.API_KEY, "label": "API OB53 ⚡"}
            return _major_register_and_login_sync(
                uid, password, access_token, open_id, name,
                region, api_config, session, is_ghost
            )

        except Exception as e:
            debug_print(f"create_acc error: {str(e)[:50]}")

        smart_delay()

    return None

def _major_register_and_login_sync(uid, password, access_token, open_id, name,
                                    region, api_config, session, is_ghost):
    """Sync: MajorRegister → MajorLogin → region binding → veteran select."""
    try:
        # XOR-encode open_id
        keystream = [0x30,0x30,0x30,0x32,0x30,0x31,0x37,0x30,0x30,0x30,0x30,0x30,0x32,0x30,0x31,0x37,
                     0x30,0x30,0x30,0x30,0x30,0x32,0x30,0x31,0x37,0x30,0x30,0x30,0x30,0x30,0x32,0x30]
        encoded_open_id = ""
        for i, ch in enumerate(open_id):
            encoded_open_id += chr(ord(ch) ^ keystream[i % len(keystream)])
        field14 = encoded_open_id.encode('latin1')

        lang_code = "pt" if is_ghost else Config.REGION_LANG.get(region.upper(), "en")
        payload_fields = {
            1: name, 2: access_token, 3: open_id,
            5: 102000007, 6: 4, 7: 1, 13: 1,
            14: field14, 15: lang_code, 16: 1, 17: 1
        }
        proto_bytes = run_async(CrEaTe_ProTo(payload_fields))
        encrypted_payload = E_AEs(bytes(proto_bytes).hex())

        host = "loginbp.ggpolarbear.com"
        register_url = Config.MAJOR_REGISTER_URL
        login_url    = Config.MAJOR_LOGIN_URL

        headers_reg = {
            "Accept-Encoding": "gzip", "Authorization": "Bearer",
            "Connection": "Keep-Alive", "Content-Type": "application/x-www-form-urlencoded",
            "Expect": "100-continue", "Host": host,
            "ReleaseVersion": "OB53",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; ASUS_I005DA Build/PI)",
            "X-GA": "v1 1", "X-Unity-Version": "1.123.1",
        }

        resp_reg = session.post(register_url, headers=headers_reg,
                                data=encrypted_payload, verify=False, timeout=15)
        if resp_reg.status_code != 200:
            return None
        # MajorRegister OK — silent, box will show after activation

        # ── MajorLogin (same host) ──────────────────────────────────────────
        login_result = _perform_major_login_sync(uid, password, access_token, open_id,
                                                  region, session, is_ghost)
        account_id = login_result.get("account_id", "N/A")
        jwt_token  = login_result.get("jwt_token", "")
        ml_key     = login_result.get("ml_key")
        ml_iv      = login_result.get("ml_iv")
        ml_ts      = login_result.get("ml_timestamp")
        ml_url     = login_result.get("ml_url")

        if not is_ghost and jwt_token and account_id != "N/A" and region.upper() != "BR":
            _force_region_binding(region, jwt_token, session)
            _select_veteran(region, jwt_token, session)

        # ── TCP Activation (from genapi main.py — makes account ACTIVE) ──────
        tcp_ok = False
        if jwt_token and account_id != "N/A":
            tcp_ok = _activate_via_tcp(
                account_id, jwt_token, ml_ts, ml_key, ml_iv,
                open_id, access_token, ml_url, session
            )
            # tcp_ok result stored — box printed after all steps done
            pass

        return {
            "uid": uid, "password": password, "name": name,
            "region": "GHOST" if is_ghost else region,
            "status": "success", "account_id": account_id,
            "jwt_token": jwt_token, "api_label": api_config["label"],
            "tcp_activated": tcp_ok,
        }
    except Exception as e:
        debug_print(f"MajorRegister error: {str(e)[:50]}")
        return None

def _encrypt_major_login_proto(open_id, access_token):
    """
    OB53 NEW: Build MajorLogin payload using MajoRLoGinrEq_pb2 protobuf
    (from genapi.zip — updated method)
    """
    if not NEW_PROTO_AVAILABLE or not AES_AVAILABLE:
        return None
    try:
        ml = MajoRLoGinrEq_pb2.MajorLogin()
        ml.event_time            = str(datetime.now())[:-7]
        ml.game_name             = "free fire"
        ml.platform_id           = 1
        ml.client_version        = "1.123.1"
        ml.system_software       = "Android OS 9 / API-28 (PQ3B.190801.10101846/G9650ZHU2ARC6)"
        ml.system_hardware       = "Handheld"
        ml.telecom_operator      = "Verizon"
        ml.network_type          = "WIFI"
        ml.screen_width          = 1920
        ml.screen_height         = 1080
        ml.screen_dpi            = "280"
        ml.processor_details     = "ARM64 FP ASIMD AES VMH | 2865 | 4"
        ml.memory                = 3003
        ml.gpu_renderer          = "Adreno (TM) 640"
        ml.gpu_version           = "OpenGL ES 3.1 v1.46"
        ml.unique_device_id      = "Google|34a7dcdf-a7d5-4cb6-8d7e-3b0e448a0c57"
        ml.client_ip             = "223.191.51.89"
        ml.language              = "en"
        ml.open_id               = open_id
        ml.open_id_type          = "4"
        ml.device_type           = "Handheld"
        ml.memory_available.version      = 55
        ml.memory_available.hidden_value = 81
        ml.access_token          = access_token
        ml.platform_sdk_id       = 1
        ml.network_operator_a    = "Verizon"
        ml.network_type_a        = "WIFI"
        ml.client_using_version  = "7428b253defc164018c604a1ebbfebdf"
        ml.external_storage_total        = 36235
        ml.external_storage_available    = 31335
        ml.internal_storage_total        = 2519
        ml.internal_storage_available    = 703
        ml.game_disk_storage_available   = 25010
        ml.game_disk_storage_total       = 26628
        ml.external_sdcard_avail_storage = 32992
        ml.external_sdcard_total_storage = 36235
        ml.login_by              = 3
        ml.library_path          = "/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/lib/arm64"
        ml.reg_avatar            = 1
        ml.library_token         = "5b892aaabd688e571f688053118a162b|/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/base.apk"
        ml.channel_type          = 3
        ml.cpu_type              = 2
        ml.cpu_architecture      = "64"
        ml.client_version_code   = "2019118695"
        ml.graphics_api          = "OpenGLES2"
        ml.supported_astc_bitset = 16383
        ml.login_open_id_type    = 4
        ml.analytics_detail      = b"FwQVTgUPX1UaUllDDwcWCRBpWA0FUgsvA1snWlBaO1kFYg=="
        ml.loading_time          = 13564
        ml.release_channel       = "android"
        ml.extra_info            = "KqsHTymw5/5GB23YGniUYN2/q47GATrq7eFeRatf0NkwLKEMQ0PK5BKEk72dPflAxUlEBir6Vtey83XqF593qsl8hwY="
        ml.android_engine_init_flag = 110009
        ml.if_push               = 1
        ml.is_vpn                = 1
        ml.origin_platform_type  = "4"
        ml.primary_platform_type = "4"
        serialized = ml.SerializeToString()
        key_b = bytes([89,103,38,116,99,37,68,69,117,104,54,37,90,99,94,56])
        iv_b  = bytes([54,111,121,90,68,114,50,50,69,51,121,99,104,106,77,37])
        cipher = AES.new(key_b, AES.MODE_CBC, iv_b)
        return cipher.encrypt(pad(serialized, AES.block_size))
    except Exception as e:
        debug_print(f"Proto MajorLogin build error: {e}")
        return None

def _perform_major_login_sync(uid, password, access_token, open_id, region, session, is_ghost=False):
    """
    OB53 UPDATED: Uses new protobuf MajorLogin (genapi.zip) as primary method,
    falls back to legacy binary payload if proto not available.
    """
    url = Config.MAJOR_LOGIN_URL
    headers = {
        "Accept-Encoding": "gzip", "Authorization": "Bearer",
        "Connection": "Keep-Alive", "Content-Type": "application/x-www-form-urlencoded",
        "Expect": "100-continue", "Host": "loginbp.ggpolarbear.com",
        "ReleaseVersion": "OB53",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; ASUS_I005DA Build/PI)",
        "X-GA": "v1 1", "X-Unity-Version": "2018.4.11f1",
    }

    # ── Method 1: New protobuf from genapi.zip ────────────────────────────────
    final_payload = None
    if NEW_PROTO_AVAILABLE and AES_AVAILABLE:
        try:
            final_payload = _encrypt_major_login_proto(open_id, access_token)
            debug_print(f"MajorLogin (proto/new) for {uid}")
        except Exception as e:
            debug_print(f"Proto build failed, falling back: {e}")
            final_payload = None

    # ── Method 2: Legacy binary payload fallback ──────────────────────────────
    if final_payload is None:
        try:
            lang = "pt" if is_ghost else Config.REGION_LANG.get(region.upper(), "en")
            payload_parts = [
                b'\x1a\x132025-08-30 05:19:21\"\tfree fire(\x01:\x081.114.13B2Android OS 9 / API-28 (PI/rel.cjw.20220518.114133)J\x08HandheldR\nATM MobilsZ\x04WIFI`\xb6\nh\xee\x05r\x03300z\x1fARMv7 VFPv3 NEON VMH | 2400 | 2\x80\x01\xc9\x0f\x8a\x01\x0fAdreno (TM) 640\x92\x01\rOpenGL ES 3.2\x9a\x01+Google|dfa4ab4b-9dc4-454e-8065-e70c733fa53f\xa2\x01\x0e105.235.139.91\xaa\x01\x02',
                lang.encode("ascii"),
                b'\xb2\x01 1d8ec0240ede109973f3321b9354b44d\xba\x01\x014\xc2\x01\x08Handheld\xca\x01\x10Asus ASUS_I005DA\xea\x01@afcfbf13334be42036e4f742c80b956344bed760ac91b3aff9b607a610ab4390\xf0\x01\x01\xca\x02\nATM Mobils\xd2\x02\x04WIFI\xca\x03 7428b253defc164018c604a1ebbfebdf\xe0\x03\xa8\x81\x02\xe8\x03\xf6\xe5\x01\xf0\x03\xaf\x13\xf8\x03\x84\x07\x80\x04\xe7\xf0\x01\x88\x04\xa8\x81\x02\x90\x04\xe7\xf0\x01\x98\x04\xa8\x81\x02\xc8\x04\x01\xd2\x04=/data/app/com.dts.freefireth-PdeDnOilCSFn37p1AH_FLg==/lib/arm\xe0\x04\x01\xea\x04_2087f61c19f57f2af4e7feff0b24d9d9|/data/app/com.dts.freefireth-PdeDnOilCSFn37p1AH_FLg==/base.apk\xf0\x04\x03\xf8\x04\x01\x8a\x05\x0232\x9a\x05\n2019118693\xb2\x05\tOpenGLES2\xb8\x05\xff\x7f\xc0\x05\x04\xe0\x05\xf3F\xea\x05\x07android\xf2\x05pKqsHT5ZLWrYljNb5Vqh//yFRlaPHSO9NWSQsVvOmdhEEn7W+VHNUK+Q+fduA3ptNrGB0Ll0LRz3WW0jOwesLj6aiU7sZ40p8BfUE/FI/jzSTwRe2\xf8\x05\xfb\xe4\x06\x88\x06\x01\x90\x06\x01\x9a\x06\x014\xa2\x06\x014\xb2\x06"GQ@O\x00\x0e^\x00D\x06UA\x0ePM\r\x13hZ\x07T\x06\x0cm\\V\x0ejYV;\x0bU5'
            ]
            payload_bytes = b''.join(payload_parts)
            payload_bytes = payload_bytes.replace(
                b'afcfbf13334be42036e4f742c80b956344bed760ac91b3aff9b607a610ab4390',
                access_token.encode()
            )
            payload_bytes = payload_bytes.replace(b'1d8ec0240ede109973f3321b9354b44d', open_id.encode())
            d = encrypt_api(payload_bytes.hex())
            if d:
                final_payload = bytes.fromhex(d)
            debug_print(f"MajorLogin (legacy) for {uid}")
        except Exception as e:
            debug_print(f"Legacy payload error: {e}")
            return {"account_id": "N/A", "jwt_token": ""}

    if final_payload is None:
        return {"account_id": "N/A", "jwt_token": ""}

    try:
        response = session.post(url, headers=headers, data=final_payload, verify=False, timeout=15)
        if response.status_code == 200 and len(response.content) > 10:
            # ── Primary: full protobuf decode (key/iv/timestamp/url included) ──
            if NEW_PROTO_AVAILABLE:
                try:
                    res = MajoRLoGinrEs_pb2.MajorLoginRes()
                    res.ParseFromString(response.content)
                    if res.token:
                        account_id = str(res.account_uid) if res.account_uid else decode_jwt_token(res.token)
                        # Extract key/iv as bytes (needed for TCP auth packet)
                        key_bytes = bytes(res.key) if res.key else None
                        iv_bytes  = bytes(res.iv)  if res.iv  else None
                        return {
                            "account_id": account_id,
                            "jwt_token":  res.token,
                            "ml_key":     key_bytes,
                            "ml_iv":      iv_bytes,
                            "ml_timestamp": str(res.timestamp) if res.timestamp else None,
                            "ml_url":     res.url if res.url else None,
                        }
                except:
                    pass
            # ── Fallback: text scan for JWT only ─────────────────────────────
            text = response.text
            jwt_start = text.find("eyJ")
            if jwt_start != -1:
                jwt_token = text[jwt_start:]
                second_dot = jwt_token.find(".", jwt_token.find(".") + 1)
                if second_dot != -1:
                    jwt_token = jwt_token[:second_dot + 44]
                    account_id = decode_jwt_token(jwt_token)
                    return {"account_id": account_id, "jwt_token": jwt_token,
                            "ml_key": None, "ml_iv": None,
                            "ml_timestamp": None, "ml_url": None}
    except Exception as e:
        debug_print(f"MajorLogin request error: {e}")

    return {"account_id": "N/A", "jwt_token": "",
            "ml_key": None, "ml_iv": None, "ml_timestamp": None, "ml_url": None}


# =============================================================================
# 🔌 TCP ACCOUNT ACTIVATION (from genapi main.py)
# =============================================================================

def _build_auth_token_hex(account_id, jwt_token, timestamp, key_bytes, iv_bytes):
    """Build the binary auth packet to send to game TCP servers."""
    try:
        uid = int(account_id)
        uid_hex = hex(uid)[2:]
        uid_length = len(uid_hex)
        ts = int(timestamp)
        ts_hex = hex(ts)[2:]
        if len(ts_hex) == 1:
            ts_hex = "0" + ts_hex

        # Encrypt JWT token with provided key/iv
        cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
        encrypted_token = cipher.encrypt(pad(jwt_token.encode(), AES.block_size))
        encrypted_hex   = encrypted_token.hex()
        enc_len_hex     = hex(len(encrypted_hex) // 2)[2:]

        if uid_length == 9:
            headers_str = '0000000'
        elif uid_length == 8:
            headers_str = '00000000'
        elif uid_length == 10:
            headers_str = '000000'
        elif uid_length == 7:
            headers_str = '000000000'
        else:
            headers_str = '0000000'

        return f"0115{headers_str}{uid_hex}{ts_hex}00000{enc_len_hex}{encrypted_hex}"
    except Exception as e:
        debug_print(f"Auth token build error: {e}")
        return None

def _get_login_data_sync(base_url, open_id, access_token, jwt_token, session):
    """Call GetLoginData to get Online + Chat server IP:Port."""
    try:
        if not NEW_PROTO_AVAILABLE:
            return None, None
        payload = _encrypt_major_login_proto(open_id, access_token)
        if payload is None:
            return None, None
        url = f"{base_url}/GetLoginData"
        host = base_url.replace("https://", "").replace("http://", "")
        headers = {
            "Accept-Encoding": "gzip",
            "Authorization": f"Bearer {jwt_token}",
            "Connection": "Keep-Alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Expect": "100-continue",
            "Host": host,
            "ReleaseVersion": "OB53",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; ASUS_I005DA Build/PI)",
            "X-GA": "v1 1",
            "X-Unity-Version": "2018.4.11f1",
        }
        resp = session.post(url, headers=headers, data=payload, verify=False, timeout=15)
        if resp.status_code == 200 and resp.content:
            data = PorTs_pb2.GetLoginData()
            data.ParseFromString(resp.content)
            online_ip_port = data.Online_IP_Port if data.Online_IP_Port else None
            chat_ip_port   = data.AccountIP_Port if data.AccountIP_Port else None
            return online_ip_port, chat_ip_port
    except Exception as e:
        debug_print(f"GetLoginData error: {e}")
    return None, None

async def _tcp_connect_and_activate(ip, port, auth_hex, server_name, duration=3):
    """Connect to game TCP server and send auth packet (activates account)."""
    try:
        reader, writer = await asyncio.open_connection(ip, int(port), ssl=False)
        debug_print(f"TCP connected to {server_name} {ip}:{port}")
        writer.write(bytes.fromhex(auth_hex))
        await writer.drain()
        debug_print(f"TCP auth sent to {server_name}")
        await asyncio.sleep(duration)
        writer.close()
        await writer.wait_closed()
        debug_print(f"TCP disconnected from {server_name}")
        return True
    except Exception as e:
        debug_print(f"TCP error {server_name} {ip}:{port} — {e}")
        return False

def _activate_via_tcp(account_id, jwt_token, timestamp, key_bytes, iv_bytes,
                      open_id, access_token, ml_url, session):
    """
    Full TCP activation flow (exactly as in genapi main.py):
    1. GetLoginData → get Online + Chat IP:Port
    2. Build auth token hex
    3. TCP connect to both servers simultaneously for 3 seconds
    Returns True if at least one TCP connection succeeded.
    """
    try:
        if not (key_bytes and iv_bytes and timestamp and ml_url):
            debug_print("TCP activation skipped: missing key/iv/timestamp/url")
            return False

        online_ip_port, chat_ip_port = _get_login_data_sync(
            ml_url, open_id, access_token, jwt_token, session
        )
        if not online_ip_port and not chat_ip_port:
            debug_print("TCP activation: no server IP returned from GetLoginData")
            return False

        auth_hex = _build_auth_token_hex(account_id, jwt_token, timestamp, key_bytes, iv_bytes)
        if not auth_hex:
            return False

        debug_print(f"TCP activating account {account_id} via {online_ip_port} + {chat_ip_port}")

        async def _run():
            tasks = []
            if online_ip_port and ":" in online_ip_port:
                ip, port = online_ip_port.split(":")
                tasks.append(_tcp_connect_and_activate(ip, port, auth_hex, "Online"))
            if chat_ip_port and ":" in chat_ip_port:
                ip, port = chat_ip_port.split(":")
                tasks.append(_tcp_connect_and_activate(ip, port, auth_hex, "Chat"))
            if tasks:
                results = await asyncio.gather(*tasks, return_exceptions=True)
                return any(r is True for r in results)
            return False

        # Run inside its own event loop (thread-safe)
        loop = asyncio.new_event_loop()
        try:
            result = loop.run_until_complete(_run())
        finally:
            loop.close()
        return result
    except Exception as e:
        debug_print(f"TCP activation error: {e}")
        return False

def _force_region_binding(region, jwt_token, session):
    try:
        url = ("https://loginbp.common.ggbluefox.com/ChooseRegion"
               if region.upper() in ["ME","TH"]
               else "https://loginbp.ggpolarbear.com/ChooseRegion")
        region_code = "RU" if region.upper() == "CIS" else region.upper()
        fields = {1: region_code}
        proto_data = run_async(CrEaTe_ProTo(fields))
        encrypted_data = encrypt_api(bytes(proto_data).hex())
        payload = bytes.fromhex(encrypted_data)
        headers = {
            'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 12; M2101K7AG Build/SKQ1.210908.001)",
            'Connection': "Keep-Alive", 'Accept-Encoding': "gzip",
            'Content-Type': "application/x-www-form-urlencoded", 'Expect': "100-continue",
            'Authorization': f"Bearer {jwt_token}", 'X-Unity-Version': "1.123.1",
            'X-GA': "v1 1", 'ReleaseVersion': "OB53",
        }
        response = session.post(url, data=payload, headers=headers, verify=False, timeout=15)
        return response.status_code == 200
    except:
        return False

def _select_veteran(region, jwt_token, session):
    try:
        url = ("https://clientbp.common.ggbluefox.com/ActiveBeginnerGuide"
               if region.upper() in ["ME","TH"]
               else "https://clientbp.ggpolarbear.com/ActiveBeginnerGuide")
        fields = {1: 3}
        proto_data = run_async(CrEaTe_ProTo(fields))
        encrypted_data = encrypt_api(bytes(proto_data).hex())
        payload = bytes.fromhex(encrypted_data)
        headers = {
            'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 12; M2101K7AG Build/SKQ1.210908.001)",
            'Connection': "Keep-Alive", 'Accept-Encoding': "gzip",
            'Content-Type': "application/x-www-form-urlencoded", 'Expect': "100-continue",
            'Authorization': f"Bearer {jwt_token}", 'X-Unity-Version': "1.123.1",
            'X-GA': "v1 1", 'ReleaseVersion': "OB53",
        }
        response = session.post(url, data=payload, headers=headers, verify=False, timeout=15)
        return response.status_code == 200
    except:
        return False

# =============================================================================
# 🔥 AUTO ACTIVATION INTEGRATION
# =============================================================================

ACTIVATED_COUNTER      = 0
FAILED_ACTIVATION_COUNTER = 0

def auto_activate_account(account_data):
    global ACTIVATED_COUNTER, FAILED_ACTIVATION_COUNTER
    if not Config.AUTO_ACT:
        return False
    try:
        # All silent — box already printed with final status
        activator = AutoActivator(max_workers=1, turbo_mode=True)
        success = activator.activate_account(account_data)
        with Config.LOCK:
            if success:
                ACTIVATED_COUNTER += 1
                save_activated_account(account_data)
                account_data['tcp_activated'] = True
            else:
                FAILED_ACTIVATION_COUNTER += 1
                save_failed_activation(account_data)
        return success
    except Exception as e:
        with Config.LOCK:
            FAILED_ACTIVATION_COUNTER += 1
        return False

# =============================================================================
# 💾 SAVE FUNCTIONS
# =============================================================================

def save_activated_account(account_data):
    try:
        activated_name = getattr(Config, 'CURRENT_ACTIVATED_BASE', 'activated')
        filename = os.path.join(Config.ACTIVATED_FOLDER, f"{activated_name}.json")
        entry = {
            'uid': account_data['uid'], 'password': account_data['password'],
            'account_id': account_data.get('account_id','N/A'),
            'name': account_data['name'], 'region': account_data.get('region','UNKNOWN'),
            'activated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        with get_file_lock(filename):
            lst = safe_json_load(filename, [])
            lst.append(entry)
            safe_json_save(filename, lst)
    except: pass

def save_failed_activation(account_data):
    try:
        region = account_data.get('region', 'UNKNOWN')
        filename = os.path.join(Config.FAILED_ACTIVATION_FOLDER, f"failed-{region}.json")
        entry = {
            'uid': account_data['uid'], 'password': account_data['password'],
            'account_id': account_data.get('account_id','N/A'),
            'name': account_data['name'], 'region': region,
            'failed_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        with get_file_lock(filename):
            lst = safe_json_load(filename, [])
            lst.append(entry)
            safe_json_save(filename, lst)
    except: pass

def save_jwt_token(account_data, jwt_token, region, is_ghost=False):
    try:
        filename = (os.path.join(Config.GHOST_FOLDER, "tokens-ghost.json") if is_ghost
                    else os.path.join(Config.TOKENS_FOLDER, f"tokens-{region}.json"))
        entry = {
            'uid': account_data["uid"], 'account_id': account_data.get("account_id","N/A"),
            'jwt_token': jwt_token, 'name': account_data["name"],
            'password': account_data["password"],
            'date_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'region': "KAWSAR" if is_ghost else region,
            'thread_id': account_data.get('thread_id','N/A')
        }
        with get_file_lock(filename):
            lst = safe_json_load(filename, [])
            existing = [t.get('account_id') for t in lst]
            if account_data.get("account_id","N/A") not in existing:
                lst.append(entry)
                safe_json_save(filename, lst)
                return True
        return False
    except: return False

def save_normal_account(account_data, region, is_ghost=False):
    try:
        if is_ghost:
            filename = os.path.join(Config.GHOST_ACCOUNTS_FOLDER, "ghost.json")
        else:
            json_base = getattr(Config, 'CURRENT_JSON_BASE', f'accounts-{region}')
            filename = os.path.join(Config.ACCOUNTS_FOLDER, f"{json_base}.json")
        entry = {
            'uid': account_data["uid"], 'password': account_data["password"],
            'account_id': account_data.get("account_id","N/A"), 'name': account_data["name"],
            'region': "KAWSAR" if is_ghost else region,
            'date_created': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'thread_id': account_data.get('thread_id','N/A')
        }
        with get_file_lock(filename):
            lst = safe_json_load(filename, [])
            existing = [a.get('account_id') for a in lst]
            if account_data.get("account_id","N/A") not in existing:
                lst.append(entry)
                safe_json_save(filename, lst)
                return True
        return False
    except: return False

def save_rare_account(account_data, rarity_type, reason, rarity_score, is_ghost=False):
    # ✅ FIX: score 10 এর নিচে হলে JSON ফাইলে save হবে না
    if rarity_score < 10:
        debug_print(f"Rare score {rarity_score} < 10 — not saved to file")
        return False
    try:
        filename = (os.path.join(Config.GHOST_RARE_FOLDER, "rare-ghost.json") if is_ghost
                    else os.path.join(Config.RARE_ACCOUNTS_FOLDER, f"rare-{account_data.get('region','UNKNOWN')}.json"))
        entry = {
            'uid': account_data["uid"], 'password': account_data["password"],
            'account_id': account_data.get("account_id","N/A"), 'name': account_data["name"],
            'region': "KAWSAR" if is_ghost else account_data.get('region','UNKNOWN'),
            'rarity_type': rarity_type, 'rarity_score': rarity_score, 'reason': reason,
            'date_identified': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'jwt_token': account_data.get('jwt_token',''), 'thread_id': account_data.get('thread_id','N/A')
        }
        with get_file_lock(filename):
            lst = safe_json_load(filename, [])
            existing = [a.get('account_id') for a in lst]
            if account_data.get("account_id","N/A") not in existing:
                lst.append(entry)
                safe_json_save(filename, lst)
                return True
        return False
    except: return False

def save_couples_account(account1, account2, reason, is_ghost=False):
    try:
        region = account1.get('region','UNKNOWN')
        filename = (os.path.join(Config.GHOST_COUPLES_FOLDER, "couples-ghost.json") if is_ghost
                    else os.path.join(Config.COUPLES_ACCOUNTS_FOLDER, f"couples-{region}.json"))
        entry = {
            'couple_id': f"{account1.get('account_id','N/A')}_{account2.get('account_id','N/A')}",
            'account1': {'uid': account1["uid"], 'password': account1["password"],
                         'account_id': account1.get("account_id","N/A"), 'name': account1["name"],
                         'thread_id': account1.get('thread_id','N/A')},
            'account2': {'uid': account2["uid"], 'password': account2["password"],
                         'account_id': account2.get("account_id","N/A"), 'name': account2["name"],
                         'thread_id': account2.get('thread_id','N/A')},
            'reason': reason, 'region': "KAWSAR" if is_ghost else region,
            'date_matched': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        with get_file_lock(filename):
            lst = safe_json_load(filename, [])
            existing = [c.get('couple_id') for c in lst]
            if entry['couple_id'] not in existing:
                lst.append(entry)
                safe_json_save(filename, lst)
                return True
        return False
    except: return False

# =============================================================================
# 👥 WORKER FUNCTIONS
# =============================================================================

RARE_COUNTER    = 0
COUPLES_COUNTER = 0
SUCCESS_COUNTER = 0

def print_registration_status(count, total, name, uid, password, account_id, region, is_ghost=False, api_label="OB53", tcp_activated=False, jwt_token=""):
    """Clean stacking box — perfect borders, long values wrap inside, NO outside prints"""
    C   = VISUAL.COLORS
    R   = C['reset']; B = C['bold']
    W   = 58   # total inner width (between │ and │)

    # ── Color palette ─────────────────────────────────────────────────
    HDR_C = '\033[38;5;46m'    # bright green  — header banner
    LBL_C = '\033[38;5;87m'    # cyan-white    — icon+key labels
    VAL_C = '\033[38;5;255m'   # pure white    — regular values
    ACC_C = '\033[38;5;226m'   # gold          — Account ID
    BDR_C = '\033[38;5;51m'    # bright cyan   — box borders
    TS_C  = '\033[38;5;252m'   # light grey    — timestamp
    JWT_C = '\033[38;5;248m'   # mid grey      — jwt token

    # ── Inner content width (excludes "│ " and " │" = 4 chars) ───────
    INNER = W - 4  # usable chars per line between borders

    def box_line(text_colored, text_plain):
        """Print one line padded to exactly W chars inside borders."""
        pad = max(0, INNER - len(text_plain))
        print(f"{BDR_C}│{R} {text_colored}{' '*pad} {BDR_C}│{R}")

    def row(icon, key, val, vc=VAL_C):
        """Print a key:value row; wraps value to next line(s) if too long."""
        label     = f"{icon} {key:<12}"  # fixed-width label ~15 chars
        label_len = len(label)
        val_s     = str(val)
        avail     = INNER - label_len     # chars left for value on same line

        if len(val_s) <= avail:
            # fits on one line
            plain = label + val_s
            colored = f"{LBL_C}{B}{label}{R}{vc}{val_s}{R}"
            box_line(colored, plain)
        else:
            # first line: label + first chunk
            chunk1 = val_s[:avail]
            plain1 = label + chunk1
            colored1 = f"{LBL_C}{B}{label}{R}{vc}{chunk1}{R}"
            box_line(colored1, plain1)
            # continuation lines: indent to align under value
            indent = " " * (label_len)
            rest   = val_s[avail:]
            avail2 = INNER - label_len
            while rest:
                chunk = rest[:avail2]
                rest  = rest[avail2:]
                plain2   = indent + chunk
                colored2 = f"{vc}{indent}{chunk}{R}"
                box_line(colored2, plain2)

    # ── Header ────────────────────────────────────────────────────────
    hdr_txt  = "🎉  SUCCESSFUL ACCOUNT GENERATED!"
    hdr_plain= "    SUCCESSFUL ACCOUNT GENERATED!"   # visual len approx
    print(f"{BDR_C}╔{'═'*W}╗{R}")
    hdr_pad  = max(0, INNER - len(hdr_plain))
    print(f"{BDR_C}║{R} {HDR_C}{B}{hdr_txt}{R}{' '*hdr_pad} {BDR_C}║{R}")
    print(f"{BDR_C}╠{'═'*W}╣{R}")

    # ── Data rows ─────────────────────────────────────────────────────
    row("🆔", "UID:",        str(uid))
    # Password: first 8 chars visible, rest filled with * to box width
    pwd_visible = 8
    pwd_label_len = len("🔑 Password:   ")  # approx label width in row()
    pwd_avail = INNER - 16  # chars available after label
    pwd_stars = max(0, pwd_avail - pwd_visible)
    pwd_display = str(password)[:pwd_visible] + ("*" * pwd_stars)
    row("🔑", "Password:",   pwd_display)
    row("👤", "Name:",       str(name))
    row("🎮", "Account ID:", str(account_id), ACC_C)

    ts_now = __import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    row("🕐", "Created At:", ts_now, TS_C)

    # JWT: first 8 chars visible, rest filled with * to box width
    jwt_src = jwt_token if jwt_token else password
    jwt_visible = 8
    jwt_stars = max(0, pwd_avail - jwt_visible)
    jwt_display = jwt_src[:jwt_visible] + ("*" * jwt_stars)
    row("🔒", "JWT Token:",  jwt_display, JWT_C)

    # ── Footer ────────────────────────────────────────────────────────
    print(f"{BDR_C}╚{'═'*W}╝{R}")
    print()

def generate_single_account(region, total_accounts, thread_id, session, is_ghost=False):
    global SUCCESS_COUNTER, RARE_COUNTER, COUPLES_COUNTER, BIO_SET_COUNTER
    global ACTIVATED_COUNTER, FAILED_ACTIVATION_COUNTER

    if EXIT_FLAG:
        return None

    with Config.LOCK:
        if SUCCESS_COUNTER >= total_accounts:
            return None

    account_result = create_acc(region, session, is_ghost)
    if not account_result:
        return None

    account_id = account_result.get("account_id", "N/A")
    jwt_token  = account_result.get("jwt_token", "")
    api_label  = account_result.get("api_label", "OB53")
    account_result['thread_id'] = thread_id

    # ── Bio (background, before box) ─────────────────────────────────
    if Config.AUTO_BIO:
        set_account_bio(account_result["uid"], account_result["password"],
                        Config.BIO_TEXT, region,
                        existing_jwt=account_result.get("jwt_token", ""))

    # ── Save & Activate (all background, before box) ──────────────────
    tcp_ok = account_result.get("tcp_activated", False)

    if is_ghost:
        save_normal_account(account_result, "GHOST", is_ghost=True)
        if jwt_token: save_jwt_token(account_result, jwt_token, "GHOST", is_ghost=True)
    else:
        save_normal_account(account_result, region)
        if jwt_token: save_jwt_token(account_result, jwt_token, region)

        if tcp_ok:
            with Config.LOCK:
                ACTIVATED_COUNTER += 1
            save_activated_account(account_result)
        elif Config.AUTO_ACT:
            auto_activate_account(account_result)

    # ── Rare / Couples check (background) ────────────────────────────
    is_rare, rarity_type, rarity_reason, rarity_score = check_account_rarity(account_result)
    if is_rare:
        with Config.LOCK: RARE_COUNTER += 1
        save_rare_account(account_result, rarity_type, rarity_reason, rarity_score, is_ghost)

    is_couple, couple_reason, partner_data = check_account_couples(account_result, thread_id)
    if is_couple and partner_data:
        with Config.LOCK: COUPLES_COUNTER += 1
        save_couples_account(account_result, partner_data, couple_reason, is_ghost)

    # ── Update counter THEN print box — after ALL work is done ────────
    with Config.LOCK:
        SUCCESS_COUNTER += 1
        current_count = SUCCESS_COUNTER

    # Final tcp_ok after possible auto_activate
    tcp_ok = account_result.get("tcp_activated", False) or (
        ACTIVATED_COUNTER > 0 and not is_ghost
    )

    print_registration_status(current_count, total_accounts, account_result["name"],
                              account_result["uid"], account_result["password"],
                              account_id, region, is_ghost, api_label,
                              tcp_activated=account_result.get("tcp_activated", False),
                              jwt_token=account_result.get("jwt_token", ""))

    return {"account": account_result}

def worker(region, total_accounts, thread_id, is_ghost=False):
    # Thread start/done suppressed — only account boxes are printed
    session = requests.Session()
    accounts_generated = 0
    while not EXIT_FLAG:
        with Config.LOCK:
            if SUCCESS_COUNTER >= total_accounts:
                break
        result = generate_single_account(region, total_accounts, thread_id, session, is_ghost)
        if result:
            accounts_generated += 1
        smart_delay()
    pass  # Thread done (suppressed)

# =============================================================================
# 📋 MENU FUNCTIONS
# =============================================================================

def generate_accounts_flow():
    global SUCCESS_COUNTER, RARE_COUNTER, COUPLES_COUNTER
    global ACTIVATED_COUNTER, FAILED_ACTIVATION_COUNTER, BIO_SET_COUNTER

    VISUAL.show_header(Config.USER_LEVEL)
    C = VISUAL.COLORS

    # ── Step 1: Ask for custom account name ────────────────────────────────────
    print(VISUAL.create_panel("👤 CUSTOM ACCOUNT NAME", "এখন জেনারেট হওয়া অ্যাকাউন্টের নাম দিন।\nEnter the name to use for generated accounts:"))
    while True:
        custom_name = input(f"\n{C['primary']}{C['bold']}✏️  Account Name: {C['reset']}").strip()
        if custom_name:
            Config.CUSTOM_NAME_PREFIX = custom_name
            break
        print_error("Name cannot be empty!")

    # ── Step 2: Ask for JSON filename ──────────────────────────────────────────
    print(VISUAL.create_panel("💾 JSON FILE NAME", "সেভ ফাইলের নাম দিন (শুধু নাম, .json ছাড়া)\nEnter JSON save file name (without .json):"))
    while True:
        json_base_name = input(f"\n{C['secondary']}{C['bold']}📄 JSON Name: {C['reset']}").strip()
        if json_base_name:
            break
        print_error("JSON name cannot be empty!")

    # ── Step 3: Region selection ───────────────────────────────────────────────
    regions_to_show = [r for r in Config.REGION_LANG.keys() if r != "BR"]
    region_menu = ""
    for i, region in enumerate(regions_to_show, 1):
        region_menu += f"{i}) {region}  ({Config.REGION_LANG[region]})\n"
    region_menu += f"{len(regions_to_show)+1}) 👻 GHOST Mode\n00) ⬅️  BACK\n000) 🚪 EXIT"

    print(VISUAL.create_panel("🌍 SELECT REGION", region_menu))

    while True:
        try:
            choice = input(f"\n{C['primary']}{C['bold']}🎯 Choose: {C['reset']}").strip().upper()
            if choice == "00": return
            elif choice == "000":
                print(f"\n{C['primary']}{C['bold']}👋 Goodbye!{C['reset']}")
                sys.exit(0)
            elif choice.isdigit():
                n = int(choice)
                if 1 <= n <= len(regions_to_show):
                    selected_region = regions_to_show[n - 1]; is_ghost = False; break
                elif n == len(regions_to_show) + 1:
                    selected_region = "BR"; is_ghost = True; break
            elif choice in regions_to_show:
                selected_region = choice; is_ghost = False; break
            elif choice == "GHOST":
                selected_region = "BR"; is_ghost = True; break
            else:
                print_error("Invalid option")
        except KeyboardInterrupt:
            safe_exit()

    VISUAL.show_header(Config.USER_LEVEL)
    account_count = Config.CUSTOM_TARGET if Config.USER_LEVEL in ["ADMIN","OWNER"] else 999999999
    thread_count  = Config.MAX_THREADS

    # Build JSON filename: name-region (e.g. test-bd)
    region_suffix = selected_region.lower()
    Config.CURRENT_JSON_BASE = f"{json_base_name}-{region_suffix}"
    Config.CURRENT_ACTIVATED_BASE = f"{json_base_name}-{region_suffix}-activated"

    user_level_display = f"{'👑' if Config.USER_LEVEL=='OWNER' else '⚡' if Config.USER_LEVEL=='ADMIN' else '👤'} {Config.USER_LEVEL}"
    custom_settings = (f"\n📝 Name Prefix: {Config.CUSTOM_NAME_PREFIX}\n🔑 Pass Prefix: {Config.CUSTOM_PASS_PREFIX}\n💎 Rarity Threshold: {Config.CUSTOM_RARITY_THRESHOLD}"
                       if Config.USER_LEVEL in ["ADMIN","OWNER"] else "")

    config_text = f"""🎯 Target    : {account_count}
⚡ Threads   : {thread_count}
🔌 APIs      : {API_COUNT}
📝 Auto Bio  : {'ON' if Config.AUTO_BIO else 'OFF'}
🔥 Auto-Act  : {'ON' if Config.AUTO_ACT else 'OFF'}
🌍 Region    : {'GHOST' if is_ghost else selected_region}
👤 Level     : {user_level_display}
🔄 Retries   : {Config.MAX_RETRIES}
🆕 Version   : OB53 — NEW API ENDPOINTS
👤 Acc Name  : {Config.CUSTOM_NAME_PREFIX}
💾 JSON File : {Config.CURRENT_JSON_BASE}.json
🔥 Activated : {Config.CURRENT_ACTIVATED_BASE}.json{custom_settings}"""

    print(VISUAL.create_panel("🚀 GENERATION CONFIG", config_text))
    print(f"\n{C['warning']}⏳ Starting in 3 seconds...{C['reset']}")
    time.sleep(3)

    SUCCESS_COUNTER = RARE_COUNTER = COUPLES_COUNTER = 0
    ACTIVATED_COUNTER = FAILED_ACTIVATION_COUNTER = BIO_SET_COUNTER = 0
    start_time = time.time()
    threads = []

    global GENERATION_SILENT
    GENERATION_SILENT = True
    print(f"\n{C['primary']}{C['bold']}🚀 Launching {thread_count} threads...{C['reset']}\n")
    for i in range(thread_count):
        t = threading.Thread(target=worker, args=(selected_region, account_count, i+1, is_ghost))
        t.daemon = True
        t.start()
        threads.append(t)

    try:
        while any(t.is_alive() for t in threads):
            time.sleep(1)
            with Config.LOCK:
                if SUCCESS_COUNTER >= account_count:
                    break
    except KeyboardInterrupt:
        EXIT_FLAG = True

    for t in threads:
        t.join(timeout=3)

    GENERATION_SILENT = False
    elapsed = time.time() - start_time
    final_stats = f"""📊 Generated : {SUCCESS_COUNTER}/{account_count}
💎 Rare      : {RARE_COUNTER}
💑 Couples   : {COUPLES_COUNTER}
🔥 Activated : {ACTIVATED_COUNTER}
❌ Failed    : {FAILED_ACTIVATION_COUNTER}
📝 Bio Set   : {BIO_SET_COUNTER}
⏱️  Time     : {elapsed:.2f}s
⚡ Speed     : {SUCCESS_COUNTER/elapsed:.2f} acc/s
🔌 Attempts  : {Config.ATTEMPTS}
👤 Level     : {Config.USER_LEVEL}"""
    print(VISUAL.create_panel("🎉 GENERATION COMPLETE!", final_stats))
    input(f"\n{C['warning']}{C['bold']}⏎ Press Enter to continue...{C['reset']}")

def admin_panel():
    if Config.USER_LEVEL == "USER":
        print_error("Access Denied! Admin/Owner only.")
        time.sleep(2); return
    while True:
        VISUAL.show_header(Config.USER_LEVEL)
        credits = CreditEditor.load_credits()
        C = VISUAL.COLORS
        admin_menu = f"""🔧 ULTIMATE ADMIN CONTROL PANEL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
👤 Level   : {Config.USER_LEVEL}
🔌 APIs    : {API_COUNT}

📝 CREDIT MANAGEMENT:
1) ✏️  Edit Primary Credit     (now: {credits['primary_credit']})
2) 📱 Edit Telegram Handles   (now: {credits['telegram1']}, {credits['telegram2']})
3) 🐙 Edit GitHub Link        (now: {credits['github']})
4) 📝 Edit Banner Text        (now: {credits['banner_text'][:25]}...)
5) 📝 Edit Bio Text           (now: {credits['bio_text'][:25]}...)
6) 💾 Save Credit Changes
7) 🔄 Restore Default Credits

⚙️ GENERATION SETTINGS:
8)  🎯 Name Prefix      (now: {Config.CUSTOM_NAME_PREFIX})
9)  🔑 Pass Prefix      (now: {Config.CUSTOM_PASS_PREFIX})
10) 💎 Rarity Threshold (now: {Config.CUSTOM_RARITY_THRESHOLD})
11) 🎯 Custom Target    (now: {Config.CUSTOM_TARGET})
12) ⚡ Max Threads      (now: {Config.MAX_THREADS})
13) 🔄 Max Retries      (now: {Config.MAX_RETRIES})

📊 SYSTEM CONTROLS:
14) 📈 API Statistics
15) 🗑️  Clear All Data
16) 💾 Backup System
17) 🔄 Reset Counters
18) 🔍 Toggle Debug
19) ⬅️  Back"""
        if Config.USER_LEVEL == "OWNER":
            admin_menu += "\n\n👑 OWNER EXCLUSIVE:\n20) ⚡ Force Generation Mode\n21) 🚀 Bypass Rate Limits\n22) 🔄 Custom API Priority"
        print(VISUAL.create_panel("🔧 ADMIN CONTROL", admin_menu, color='admin'))
        choice = input(f"\n{C['admin']}{C['bold']}⚡ Option: {C['reset']}").strip()

        if choice == "1":
            nc = input(f"{C['info']}New primary credit: {C['reset']}")
            credits['primary_credit'] = nc; CreditEditor.save_credits(credits)
            print_success("Updated!"); time.sleep(1)
        elif choice == "2":
            t1 = input(f"{C['info']}Telegram 1: {C['reset']}")
            t2 = input(f"{C['info']}Telegram 2: {C['reset']}")
            credits['telegram1'] = t1; credits['telegram2'] = t2
            CreditEditor.save_credits(credits); print_success("Updated!"); time.sleep(1)
        elif choice == "3":
            ng = input(f"{C['info']}GitHub URL: {C['reset']}")
            credits['github'] = ng; CreditEditor.save_credits(credits)
            print_success("Updated!"); time.sleep(1)
        elif choice == "4":
            nb = input(f"{C['info']}Banner text: {C['reset']}")
            credits['banner_text'] = nb; CreditEditor.save_credits(credits)
            print_success("Updated!"); time.sleep(1)
        elif choice == "5":
            nbio = input(f"{C['info']}Bio text: {C['reset']}")
            credits['bio_text'] = nbio; Config.BIO_TEXT = nbio
            CreditEditor.save_credits(credits); print_success("Updated!"); time.sleep(1)
        elif choice == "6":
            CreditEditor.save_credits(credits); print_success("Saved!"); time.sleep(1)
        elif choice == "7":
            d = {"primary_credit":"KAWSAR","github":"https://github.com/KAWSAR",
                 "telegram1":"@KAWSAR","telegram2":"@KAWSAR","display_name":"KAWSAR",
                 "banner_text":"⚡ POWERED BY KAWSAR ⚡",
                 "footer_text":"👤 CREDIT: KAWSAR | TELEGRAM: @KAWSAR,@KAWSAR | GITHUB: KAWSAR",
                 "bio_text":"[FF0000]🌈[FF7700]K[FFFF00]A[00FF00]W[00BFFF]S[8B00FF]A[FF0000]R[FF7700]_[FFFF00]C[00FF00]O[00BFFF]D[8B00FF]E[FF0000]X [FF7700]C[FFFF00]R[00FF00]E[00BFFF]A[8B00FF]T[FF0000]I[FF7700]O[FFFF00]N[FF0000]🌈"}
            CreditEditor.save_credits(d); Config.BIO_TEXT = d['bio_text']
            print_success("Defaults restored!"); time.sleep(1)
        elif choice == "8":
            Config.CUSTOM_NAME_PREFIX = input(f"{C['info']}Name prefix: {C['reset']}")
            print_success(f"Set: {Config.CUSTOM_NAME_PREFIX}"); time.sleep(1)
        elif choice == "9":
            Config.CUSTOM_PASS_PREFIX = input(f"{C['info']}Pass prefix: {C['reset']}")
            print_success(f"Set: {Config.CUSTOM_PASS_PREFIX}"); time.sleep(1)
        elif choice == "10":
            try:
                n = int(input(f"{C['info']}Rarity threshold (1-10): {C['reset']}"))
                if 1 <= n <= 10: Config.CUSTOM_RARITY_THRESHOLD = n; print_success(f"Set: {n}")
                else: print_error("Must be 1–10")
            except: print_error("Invalid input")
            time.sleep(1)
        elif choice == "11":
            try: Config.CUSTOM_TARGET = int(input(f"{C['info']}Target: {C['reset']}")); print_success(f"Set: {Config.CUSTOM_TARGET}")
            except: print_error("Invalid")
            time.sleep(1)
        elif choice == "12":
            try:
                n = int(input(f"{C['info']}Threads (1-64): {C['reset']}"))
                if 1 <= n <= 64: Config.MAX_THREADS = n; print_success(f"Set: {n}")
                else: print_error("Must be 1–64")
            except: print_error("Invalid")
            time.sleep(1)
        elif choice == "13":
            try:
                n = int(input(f"{C['info']}Retries (1-20): {C['reset']}"))
                if 1 <= n <= 20: Config.MAX_RETRIES = n; print_success(f"Set: {n}")
                else: print_error("Must be 1–20")
            except: print_error("Invalid")
            time.sleep(1)
        elif choice == "14":
            sr = (SUCCESS_COUNTER / Config.ATTEMPTS * 100) if Config.ATTEMPTS > 0 else 0
            st = f"Total: {Config.ATTEMPTS} | OK: {SUCCESS_COUNTER} | Failed: {Config.ATTEMPTS-SUCCESS_COUNTER} | Rate: {sr:.1f}% | APIs: {API_COUNT}"
            print(VISUAL.create_panel("📊 API STATS", st))
            input(f"\n{C['warning']}⏎ Press Enter...{C['reset']}")
        elif choice == "15":
            if input(f"{C['error']}Type CONFIRM to clear ALL data: {C['reset']}") == "CONFIRM":
                shutil.rmtree(Config.BASE_FOLDER)
                Config.create_folders()
                print_success("Cleared!")
            time.sleep(2)
        elif choice == "16":
            bp = CreditEditor.backup_current_file()
            print_success(f"Backup: {bp}") if bp else print_error("Backup failed")
            time.sleep(2)
        elif choice == "17":
            Config.SUCCESS = Config.RARE = Config.COUPLES = Config.ACTIVATED = Config.FAILED = Config.BIO = Config.ATTEMPTS = 0
            print_success("Counters reset!"); time.sleep(1)
        elif choice == "18":
            Config.DEBUG_MODE = not Config.DEBUG_MODE
            print_success(f"Debug: {'ON' if Config.DEBUG_MODE else 'OFF'}"); time.sleep(1)
        elif choice == "19":
            break
        elif choice == "20" and Config.USER_LEVEL == "OWNER":
            Config.FORCE_GENERATION = not Config.FORCE_GENERATION
            print_success(f"Force Gen: {Config.FORCE_GENERATION}"); time.sleep(1)
        elif choice == "21" and Config.USER_LEVEL == "OWNER":
            Config.BYPASS_RATE_LIMIT = not Config.BYPASS_RATE_LIMIT
            print_success(f"Bypass RL: {Config.BYPASS_RATE_LIMIT}"); time.sleep(1)
        elif choice == "22" and Config.USER_LEVEL == "OWNER":
            Config.CUSTOM_API_PRIORITY = not Config.CUSTOM_API_PRIORITY
            print_success(f"API Priority: {Config.CUSTOM_API_PRIORITY}"); time.sleep(1)
        else:
            print_error("Invalid option or insufficient privileges"); time.sleep(1)

def view_saved_accounts():
    VISUAL.show_header(Config.USER_LEVEL)
    folders = [Config.ACCOUNTS_FOLDER, Config.ACTIVATED_FOLDER,
               Config.RARE_ACCOUNTS_FOLDER, Config.COUPLES_ACCOUNTS_FOLDER]
    total = 0; results = ""
    for folder in folders:
        if os.path.exists(folder):
            for file in [f for f in os.listdir(folder) if f.endswith('.json')]:
                filepath = os.path.join(folder, file)
                try:
                    data = safe_json_load(filepath, [])
                    results += f"📄 {os.path.basename(folder)}/{file}: {len(data)} accounts\n"
                    total += len(data)
                except: pass
    results += f"\n📊 TOTAL: {total} accounts"
    print(VISUAL.create_panel("📁 SAVED ACCOUNTS", results))
    input(f"\n{VISUAL.COLORS['warning']}{VISUAL.COLORS['bold']}⏎ Press Enter...{VISUAL.COLORS['reset']}")

def show_stats():
    VISUAL.show_header(Config.USER_LEVEL)
    sr = (SUCCESS_COUNTER / Config.ATTEMPTS * 100) if Config.ATTEMPTS > 0 else 0
    stats = f"""SESSION STATISTICS
━━━━━━━━━━━━━━━━━━━━━━
✅ Generated  : {SUCCESS_COUNTER}
💎 Rare       : {RARE_COUNTER}
💑 Couples    : {COUPLES_COUNTER}
🔥 Activated  : {ACTIVATED_COUNTER}
❌ Failed     : {FAILED_ACTIVATION_COUNTER}
📝 Bio        : {BIO_SET_COUNTER}
🔌 Attempts   : {Config.ATTEMPTS}

PERFORMANCE
━━━━━━━━━━━━━━━━━━━━━━
🔌 Total APIs : {API_COUNT}
⚡ Success    : {sr:.1f}%
👤 Level      : {Config.USER_LEVEL}
🔄 Retries    : {Config.MAX_RETRIES}
⚡ Threads    : {Config.MAX_THREADS}"""
    if Config.USER_LEVEL in ["ADMIN","OWNER"]:
        stats += f"\n📝 Name Prefix: {Config.CUSTOM_NAME_PREFIX}\n🔑 Pass Prefix: {Config.CUSTOM_PASS_PREFIX}"
    print(VISUAL.create_panel("📈 STATISTICS", stats))
    input(f"\n{VISUAL.COLORS['warning']}{VISUAL.COLORS['bold']}⏎ Press Enter...{VISUAL.COLORS['reset']}")

def about():
    VISUAL.show_header(Config.USER_LEVEL)
    credits = CreditEditor.load_credits()
    about_text = f"""🔥 {credits['display_name']} ULTIMATE GENERATOR v12.0
💎 Created by : {credits['primary_credit']}
📱 Telegram   : {credits['telegram1']}, {credits['telegram2']}
🐙 GitHub     : {credits['github']}

✨ FEATURES:
• {API_COUNT} Working APIs (OB53 updated)
• New /api/v2/ JSON endpoints
• Protobuf-based MajorLogin
• ggpolarbear.com host (OB53)
• ULTIMATE ADMIN CONTROL PANEL
• 3 Access Levels USER / ADMIN / OWNER
• Auto Activation · Rare Finder · Couples
• Auto Bio Changer · Multi-threading
• Real-time statistics · Dark Gold UI

🔐 ACCESS LEVELS:
• USER  — Basic access
• ADMIN — Full control + credit editing
• OWNER — Ultimate + exclusive features

⚠️ DO NOT REMOVE CREDITS
🔒 Protected by KAWSAR"""
    print(VISUAL.create_panel("ℹ️  ABOUT", about_text))
    input(f"\n{VISUAL.COLORS['warning']}{VISUAL.COLORS['bold']}⏎ Press Enter...{VISUAL.COLORS['reset']}")

def main_menu():
    Config.create_folders()
    while True:
        VISUAL.show_header(Config.USER_LEVEL)
        C = VISUAL.COLORS
        menu = """1) 🚀 Generate Accounts
2) 📁 View Saved Accounts
3) 📊 Statistics
4) ℹ️  About"""
        if Config.USER_LEVEL in ["ADMIN","OWNER"]:
            menu += "\n5) 🔧 ULTIMATE ADMIN PANEL\n6) 🚪 Exit"
        else:
            menu += "\n5) 🚪 Exit"
        print(VISUAL.create_panel("📌 MAIN MENU", menu))
        choice = input(f"\n{C['primary']}{C['bold']}🎯 Choose: {C['reset']}").strip()
        if choice == "1":   generate_accounts_flow()
        elif choice == "2": view_saved_accounts()
        elif choice == "3": show_stats()
        elif choice == "4": about()
        elif choice == "5":
            if Config.USER_LEVEL in ["ADMIN","OWNER"]: admin_panel()
            else: print(f"\n{C['primary']}{C['bold']}👋 Goodbye!{C['reset']}"); sys.exit(0)
        elif choice == "6" and Config.USER_LEVEL in ["ADMIN","OWNER"]:
            print(f"\n{C['primary']}{C['bold']}👋 Goodbye!{C['reset']}"); sys.exit(0)
        else:
            print_error("Invalid option"); time.sleep(1)

# =============================================================================
# 🚀 MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        safe_exit()
    except Exception as e:
        print_error(f"Error: {e}")
        time.sleep(2)
        os.execv(sys.executable, [sys.executable] + sys.argv)
