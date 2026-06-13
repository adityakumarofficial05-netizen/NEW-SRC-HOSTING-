# owner = @Itz_Jahid_X
# CHANNEL = @Jahid_x_Empire
"""
PREMIUM MULTI‑REGION ACTIVATOR – STYLISH EDITION (FIXED)
- Real FreeFire API (guest token → major login → get login data)
- 64 workers, 3s timeout, zero retries
- Stylish ASCII banner, live progress, result boxes
- Supports custom path or auto-scan
"""

import os
import sys
import json
import glob
import time
import threading
import requests
import base64
from concurrent.futures import ThreadPoolExecutor, as_completed
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import urllib3
from datetime import datetime
from colorama import Fore, Style, init
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# ---------- initialize color ----------
init(autoreset=False)
C = Fore.CYAN
M = Fore.MAGENTA
W = Fore.WHITE
R = Style.RESET_ALL
G = Fore.GREEN
RED = Fore.RED
Y = Fore.YELLOW
B = Style.BRIGHT
D = Style.DIM

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ========== EMBEDDED PROTOBUF ==========
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13MajorLoginRes.proto\"\x87\x05\n\rMajorLoginRes\x12\x12\n\naccount_id\x18\x01 \x01(\x03\x12\x13\n\x0block_region\x18\x02 \x01(\t\x12\x13\n\x0bnoti_region\x18\x03 \x01(\t\x12\x11\n\tip_region\x18\x04 \x01(\t\x12\x19\n\x11\x61gora_environment\x18\x05 \x01(\t\x12\x19\n\x11new_active_region\x18\x06 \x01(\t\x12\r\n\x05token\x18\x08 \x01(\t\x12\x0b\n\x03ttl\x18\t \x01(\x05\x12\x12\n\nserver_url\x18\n \x01(\t\x12\x16\n\x0e\x65mulator_score\x18\x0c \x01(\x03\x12\x32\n\tblacklist\x18\r \x01(\x0b\x32\x1f.MajorLoginRes.BlacklistInfoRes\x12\x31\n\nqueue_info\x18\x0f \x01(\x0b\x32\x1d.MajorLoginRes.LoginQueueInfo\x12\x0e\n\x06tp_url\x18\x10 \x01(\t\x12\x15\n\rapp_server_id\x18\x11 \x01(\x03\x12\x0f\n\x07\x61no_url\x18\x12 \x01(\t\x12\x0f\n\x07ip_city\x18\x13 \x01(\t\x12\x16\n\x0eip_subdivision\x18\x14 \x01(\t\x12\x0b\n\x03kts\x18\x15 \x01(\x03\x12\n\n\x02\x61k\x18\x16 \x01(\x0c\x12\x0b\n\x03\x61iv\x18\x17 \x01(\x0c\x1aQ\n\x10\x42lacklistInfoRes\x12\x12\n\nban_reason\x18\x01 \x01(\x05\x12\x17\n\x0f\x65xpire_duration\x18\x02 \x01(\x03\x12\x10\n\x08\x62\x61n_time\x18\x03 \x01(\x03\x1a\x66\n\x0eLoginQueueInfo\x12\r\n\x05\x41llow\x18\x01 \x01(\x08\x12\x16\n\x0equeue_position\x18\x02 \x01(\x03\x12\x16\n\x0eneed_wait_secs\x18\x03 \x01(\x03\x12\x15\n\rqueue_is_full\x18\x04 \x01(\x08\x62\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'MajorLoginRes_pb2', _globals)
MajorLoginRes = _globals['MajorLoginRes']
# ========== END PROTOBUF ==========

# ---------- global stats for live updates ----------
PRINT_LOCK = threading.Lock()
STATS_LOCK = threading.Lock()
successful_count = 0
failed_count = 0
total_processed = 0

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def render_banner():
    print(f"{C}{B}╭───────────────────────────────────────────────╮")
    print(f"│  {M}██╗{C}██╗  ██╗███████╗    {W}██╗   ██╗██████╗   {C}│")
    print(f"│  {M}╚═╝{C}╚██╗██╔╝██╔════╝    {W}██║   ██║╚════██╗  {C}│")
    print(f"│     {C}╚███╔╝ {M}█████╗      {W}██║   ██║ █████╔╝  {C}│")
    print(f"│     {C}██╔██╗ {M}██╔══╝      {W}╚██╗ ██╔╝ ╚═══██╗  {C}│")
    print(f"│    {C}██╔╝╚██╗███████╗     {W}╚████╔╝ ██████╔╝  {C}│")
    print(f"│    {C}╚═╝  ╚═╝╚══════╝      {W}╚═══╝  ╚═════╝   {C}│")
    print(f"│       {W}PREMIUM REAL ACTIVATOR v3              {C}│")
    print(f"╰───────────────────────────────────────────────╯{R}")

def live_loading_animation(duration=2.0):
    steps = [
        "BOOTING CROSS-PLATFORM SYSTEM",
        "LOADING SYSTEM REQUISITES",
        "PREPARING THREAD WORKER POOLS",
        "STABILIZING MEMORY ALLOCATION"
    ]
    spinner = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    width = 24
    start_time = time.time()
    print(f"\n{C}{B}╭───────────────────༻ INITIALIZING ༺───────────────────╮{R}")
    idx = 0
    while True:
        elapsed = time.time() - start_time
        percent = min(elapsed / duration, 1.0)
        step_idx = min(int(percent * len(steps)), len(steps) - 1)
        current_step = steps[step_idx]
        filled = int(width * percent)
        bar = "█" * filled + "░" * (width - filled)
        sym = spinner[idx % len(spinner)]
        idx += 1
        line = f" {sym} {C}{current_step:<30} {Y}{int(percent * 100):3}% {G}{bar}{R}"
        sys.stdout.write(f"\r{C}║{R}{line:<52}{C}║{R}")
        sys.stdout.flush()
        if percent >= 1.0:
            break
        time.sleep(0.06)
    print(f"\n{C}{B}╰──────────────────────────────────────────────────────╯{R}\n")
    time.sleep(0.15)

def print_result_box(task_id, uid, success, execution_time):
    status_color = G if success else RED
    status_text = " [ SUCCESSFUL ] " if success else " [  FAILED  ]  "
    icon = "★" if success else "⚠"
    lines = [
        f"{C}╭───────────────────────────────────────────────╮",
        f"│ {W}TASK ID   │{R} {Y}{task_id:<32}{C}│",
        f"│ {W}ACCOUNT   │{R} {M}{uid[:30]:<32}{C}│",
        f"│ {W}STATUS    │{R} {status_color}{icon}{status_text:<31}{C}│",
        f"│ {W}LATENCY   │{R} {Y}{execution_time:.2f}s{R:<31}{C}│",
        f"╰───────────────────────────────────────────────╯"
    ]
    output = "\n".join(lines) + "\n"
    with PRINT_LOCK:
        sys.stdout.write(output)
        sys.stdout.flush()

# ---------- Real Activator Class (API logic) ----------
class RealActivator:
    def __init__(self, max_workers=64):
        self.key = bytes([89,103,38,116,99,37,68,69,117,104,54,37,90,99,94,56])
        self.iv = bytes([54,111,121,90,68,114,50,50,69,51,121,99,104,106,77,37])
        self.regions = {
            'IND': {'guest_url': 'https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant',
                    'major_login_url': 'https://loginbp.common.ggbluefox.com/MajorLogin',
                    'get_login_data_url': 'https://client.ind.freefiremobile.com/GetLoginData',
                    'client_host': 'client.ind.freefiremobile.com'},
            'BD': {'guest_url': 'https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant',
                   'major_login_url': 'https://loginbp.ggpolarbear.com/MajorLogin',
                   'get_login_data_url': 'https://clientbp.ggpolarbear.com/GetLoginData',
                   'client_host': 'clientbp.ggpolarbear.com'},
            'PK': {'guest_url': 'https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant',
                   'major_login_url': 'https://loginbp.ggpolarbear.com/MajorLogin',
                   'get_login_data_url': 'https://clientbp.ggpolarbear.com/GetLoginData',
                   'client_host': 'clientbp.ggpolarbear.com'},
            'NA': {'guest_url': 'https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant',
                   'major_login_url': 'https://loginbp.ggpolarbear.com/MajorLogin',
                   'get_login_data_url': 'https://clientbp.ggpolarbear.com/GetLoginData',
                   'client_host': 'clientbp.ggpolarbear.com'},
            'LK': {'guest_url': 'https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant',
                   'major_login_url': 'https://loginbp.ggpolarbear.com/MajorLogin',
                   'get_login_data_url': 'https://clientbp.ggpolarbear.com/GetLoginData',
                   'client_host': 'clientbp.ggpolarbear.com'},
            'ID': {'guest_url': 'https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant',
                   'major_login_url': 'https://loginbp.ggpolarbear.com/MajorLogin',
                   'get_login_data_url': 'https://clientbp.ggpolarbear.com/GetLoginData',
                   'client_host': 'clientbp.ggpolarbear.com'},
            'TH': {'guest_url': 'https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant',
                   'major_login_url': 'https://loginbp.ggpolarbear.com/MajorLogin',
                   'get_login_data_url': 'https://clientbp.common.ggbluefox.com/GetLoginData',
                   'client_host': 'clientbp.common.ggbluefox.com'},
            'VN': {'guest_url': 'https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant',
                   'major_login_url': 'https://loginbp.ggpolarbear.com/MajorLogin',
                   'get_login_data_url': 'https://clientbp.ggpolarbear.com/GetLoginData',
                   'client_host': 'clientbp.ggpolarbear.com'},
            'BR': {'guest_url': 'https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant',
                   'major_login_url': 'https://loginbp.ggpolarbear.com/MajorLogin',
                   'get_login_data_url': 'https://clientbp.ggpolarbear.com/GetLoginData',
                   'client_host': 'clientbp.ggpolarbear.com'},
            'ME': {'guest_url': 'https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant',
                   'major_login_url': 'https://loginbp.common.ggbluefox.com/MajorLogin',
                   'get_login_data_url': 'https://clientbp.ggpolarbear.com/GetLoginData',
                   'client_host': 'clientbp.ggpolarbear.com'}
        }
        self.max_workers = max_workers
        self.session = requests.Session()
        adapter = requests.adapters.HTTPAdapter(pool_connections=200, pool_maxsize=200, max_retries=0)
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)
        self.session.verify = False
        self.session.headers.update({'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36'})
        self.successful = 0
        self.failed = 0
        self.successful_accounts = []
        self.stats_lock = threading.Lock()
        self.global_region = None
        self.stop_execution = False
        self.unauthorized_count = 0
        self.max_unauthorized_before_stop = 15

    def encrypt_api(self, plain_text):
        try:
            plain = bytes.fromhex(plain_text)
            cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
            return cipher.encrypt(pad(plain, AES.block_size)).hex()
        except:
            return None

    def parse_my_message(self, serialized_data):
        try:
            res = MajorLoginRes()
            res.ParseFromString(serialized_data)
            return res.token, res.ak.hex() if res.ak else None, res.aiv.hex() if res.aiv else None
        except:
            return None, None, None

    def guest_token(self, uid, password, region):
        if self.stop_execution:
            return None, None
        cfg = self.regions.get(region, self.regions['IND'])
        data = {
            "uid": str(uid), "password": password, "response_type": "token",
            "client_type": "2", "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
            "client_id": "100067"
        }
        try:
            resp = self.session.post(cfg['guest_url'], data=data, timeout=3)
            if resp.status_code == 200:
                j = resp.json()
                return j.get('access_token'), j.get('open_id')
            elif resp.status_code == 401:
                with self.stats_lock:
                    self.unauthorized_count += 1
                    if self.unauthorized_count >= self.max_unauthorized_before_stop:
                        self.stop_execution = True
        except:
            pass
        return None, None

    def major_login(self, access_token, open_id, region):
        if self.stop_execution:
            return None
        cfg = self.regions.get(region, self.regions['IND'])
        headers = {
            'X-Unity-Version': '2018.4.11f1', 'ReleaseVersion': 'OB53',
            'Content-Type': 'application/x-www-form-urlencoded', 'X-GA': 'v1 1',
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9)',
            'Host': 'loginbp.ggpolarbear.com', 'Connection': 'Keep-Alive'
        }
        # Fixed: split long hex string into multiple lines
        hex_payload = (
            "1a13323032352d30372d33302031313a30323a3531220966726565206669726528013a07312e31"
            "34322e32422c416e64726f6964204f5320372e312e32202f204150492d323320284e3247343848"
            "2f373030323530323234294a0848616e6468656c645207416e64726f69645a045749464960c00c68"
            "840772033332307a1f41524d7637205646507633204e454f4e20564d48207c2032343635207c2034"
            "80019a1b8a010f416472656e6f2028544d292036343092010d4f70656e474c20455320332e319a01"
            "2b476f6f676c657c31663361643662372d636562342d343934622d383730622d6231646163643732"
            "30393131a2010c3139372e312e31322e313335aa0102656eb2012039393661363239646263646233"
            "39363462653662363937386635643831346462ba010134c2010848616e6468656c64ca011073616d"
            "73756e6720534d2d473935354eea0140666639306330376562393831356166333061343362346139"
            "663631393531366530653463373033623434303932353136643064656661346365663531663261f0"
            "0101ca0207416e64726f6964d2020457494649ca0320373432386232353364656663313634303138"
            "63363461316562626665626466e003daa907e803899b07f003bf0ff803ae088004999b078804daa9"
            "079004999b079804daa907c80403d204262f646174612f6170702f636f6d2e6474732e6672656566"
            "69726574682d312f6c69622f61726de00401ea044832303837663631633139663537663261663465"
            "376665666630623234643964397c2f646174612f6170702f636f6d2e6474732e6672656566697265"
            "74682d312f626173652e61706bf00403f804018a050233329a050a32303139313138363933a80503"
            "b205094f70656e474c455332b805ff7fc00504e005dac901ea0507616e64726f6964f2055c4b7173"
            "4854394748625876574c6668437950416c52526873626d43676542557562555551317375746d5255"
            "36634e30524f3751453141486e496474385963784d614c575437636d4851322b7374745279377830"
            "663935542b6456593d8806019006019a060134a2060134b2061e40001147550d0c074f530b4d5c58"
            "4d57416657545a065f2a091d6a0d5033"
        )
        payload_template = bytes.fromhex(hex_payload)
        OLD_OPEN_ID = b"996a629dbcdb3964be6b6978f5d814db"
        OLD_ACCESS_TOKEN = b"ff90c07eb9815af30a43b4a9f6019516e0e4c703b44092516d0defa4cef51f2a"
        payload = payload_template.replace(OLD_OPEN_ID, open_id.encode())
        payload = payload.replace(OLD_ACCESS_TOKEN, access_token.encode())
        encrypted = self.encrypt_api(payload.hex())
        if not encrypted:
            return None
        final = bytes.fromhex(encrypted)
        try:
            resp = self.session.post(cfg['major_login_url'], headers=headers, data=final, timeout=3)
            if resp.status_code == 200 and len(resp.content):
                return resp.content
        except:
            pass
        return None

    def GET_PAYLOAD_BY_DATA(self, jwt_token, new_access_token, region):
        try:
            payload_b64 = jwt_token.split('.')[1]
            payload_b64 += '=' * ((4 - len(payload_b64) % 4) % 4)
            decoded = json.loads(base64.urlsafe_b64decode(payload_b64))
            external_id = decoded['external_id']
            sig_md5 = decoded['signature_md5']
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            hex_template = (
                "1a13323032352d30372d33302031313a30323a3531220966726565206669726528013a07312e31"
                "34322e32422c416e64726f6964204f5320372e312e32202f204150492d323320284e3247343848"
                "2f373030323530323234294a0848616e6468656c645207416e64726f69645a045749464960c00c68"
                "840772033332307a1f41524d7637205646507633204e454f4e20564d48207c2032343635207c2034"
                "80019a1b8a010f416472656e6f2028544d292036343092010d4f70656e474c20455320332e319a01"
                "2b476f6f676c657c31663361643662372d636562342d343934622d383730622d6231646163643732"
                "30393131a2010c3139372e312e31322e313335aa0102656eb2012039393661363239646263646233"
                "39363462653662363937386635643831346462ba010134c2010848616e6468656c64ca011073616d"
                "73756e6720534d2d473935354eea0140666639306330376562393831356166333061343362346139"
                "663631393531366530653463373033623434303932353136643064656661346365663531663261f0"
                "0101ca0207416e64726f6964d2020457494649ca0320373432386232353364656663313634303138"
                "63363461316562626665626466e003daa907e803899b07f003bf0ff803ae088004999b078804daa9"
                "079004999b079804daa907c80403d204262f646174612f6170702f636f6d2e6474732e6672656566"
                "69726574682d312f6c69622f61726de00401ea044832303837663631633139663537663261663465"
                "376665666630623234643964397c2f646174612f6170702f636f6d2e6474732e6672656566697265"
                "74682d312f626173652e61706bf00403f804018a050233329a050a32303139313138363933a80503"
                "b205094f70656e474c455332b805ff7fc00504e005dac901ea0507616e64726f6964f2055c4b7173"
                "4854394748625876574c6668437950416c52526873626d43676542557562555551317375746d5255"
                "36634e30524f3751453141486e496474385963784d614c575437636d4851322b7374745279377830"
                "663935542b6456593d8806019006019a060134a2060134b2061e40001147550d0c074f530b4d5c58"
                "4d57416657545a065f2a091d6a0d5033"
            )
            template = bytes.fromhex(hex_template)
            payload = template.replace(b"2025-07-30 11:02:51", now.encode())
            payload = payload.replace(b"ff90c07eb9815af30a43b4a9f6019516e0e4c703b44092516d0defa4cef51f2a", new_access_token.encode())
            payload = payload.replace(b"996a629dbcdb3964be6b6978f5d814db", external_id.encode())
            payload = payload.replace(b"7428b253defc164018c604a1ebbfebdf", sig_md5.encode())
            enc = self.encrypt_api(payload.hex())
            return bytes.fromhex(enc) if enc else None
        except:
            return None

    def GET_LOGIN_DATA(self, jwt_token, payload, region):
        if self.stop_execution:
            return False
        cfg = self.regions.get(region, self.regions['IND'])
        headers = {
            'Authorization': f'Bearer {jwt_token}',
            'X-Unity-Version': '2018.4.11f1', 'X-GA': 'v1 1',
            'ReleaseVersion': 'OB53', 'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9)',
            'Host': cfg['client_host'], 'Connection': 'close'
        }
        try:
            resp = self.session.post(cfg['get_login_data_url'], headers=headers, data=payload, timeout=3)
            if resp.status_code == 200:
                return True
            elif resp.status_code == 401:
                with self.stats_lock:
                    self.unauthorized_count += 1
                    if self.unauthorized_count >= self.max_unauthorized_before_stop:
                        self.stop_execution = True
        except:
            pass
        return False

    def activate_single_account(self, acc, task_id):
        start = time.time()
        if self.stop_execution:
            return False
        uid = acc['uid']
        pwd = acc['password']
        region = self.global_region if self.global_region else acc.get('region', 'IND')
        if region not in self.regions:
            region = 'IND'
        access, open_id = self.guest_token(uid, pwd, region)
        if not access:
            elapsed = time.time() - start
            print_result_box(task_id, uid, False, elapsed)
            with self.stats_lock:
                self.failed += 1
            return False
        maj = self.major_login(access, open_id, region)
        if not maj:
            elapsed = time.time() - start
            print_result_box(task_id, uid, False, elapsed)
            with self.stats_lock:
                self.failed += 1
            return False
        jwt, _, _ = self.parse_my_message(maj)
        if not jwt:
            elapsed = time.time() - start
            print_result_box(task_id, uid, False, elapsed)
            with self.stats_lock:
                self.failed += 1
            return False
        payload = self.GET_PAYLOAD_BY_DATA(jwt, access, region)
        if not payload:
            elapsed = time.time() - start
            print_result_box(task_id, uid, False, elapsed)
            with self.stats_lock:
                self.failed += 1
            return False
        ok = self.GET_LOGIN_DATA(jwt, payload, region)
        elapsed = time.time() - start
        if ok:
            print_result_box(task_id, uid, True, elapsed)
            with self.stats_lock:
                self.successful += 1
                self.successful_accounts.append({
                    'uid': uid, 'password': pwd, 'region': region,
                    'name': acc.get('name', 'Unknown'),
                    'account_id': acc.get('account_id', 'N/A')
                })
        else:
            print_result_box(task_id, uid, False, elapsed)
            with self.stats_lock:
                self.failed += 1
        return ok

    # ---------- File Loading with custom path ----------
    def select_source_path(self):
        print(f"{C}{B}╭───────────────────────────────────────────────╮")
        print(f"│         {W}SYSTEM STORAGE PATH SELECTOR{C}          │")
        print(f"├───────────────────────────────────────────────┤")
        print(f"│  {Y}1. Auto-Scan Directory{C} (Any local .json/.txt) │")
        print(f"│  {Y}2. Custom Path Location{C} (Specific file/folder)│")
        print(f"╰───────────────────────────────────────────────╯{R}")
        choice = input(f"{C}{B}🎯 Mode Selection (1/2): {R}").strip()
        if choice == '2':
            print(f"\n{D}{W}💡 Path Example (Android): /sdcard/Download/my_database.json{R}")
            path = input(f"{C}📂 System Path: {R}").strip()
            path = path.replace('"', '').replace("'", "")
            if not os.path.exists(path):
                print(f"{RED}❌ File path error. Specified directory does not exist.{R}")
                return None
            return path
        else:
            return os.getcwd()

    def load_accounts_from_path(self, path):
        accounts = []
        files = []
        if os.path.isfile(path):
            files = [path]
        elif os.path.isdir(path):
            files = glob.glob(os.path.join(path, '*.json')) + glob.glob(os.path.join(path, '*.txt'))
        else:
            return accounts

        if not files:
            print(f"{RED}❌ No .json or .txt files found in {path}{R}")
            return accounts

        print(f"{G}🔍 Found {len(files)} file(s) in {path}{R}")
        for filepath in files:
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read().strip()
                if not content:
                    continue
                if filepath.endswith('.json'):
                    try:
                        data = json.loads(content)
                        if isinstance(data, list):
                            for item in data:
                                acc = self._extract_account(item)
                                if acc:
                                    accounts.append(acc)
                        elif isinstance(data, dict):
                            if 'account1' in data and 'account2' in data:
                                for key in ['account1', 'account2']:
                                    acc = self._extract_account(data[key])
                                    if acc:
                                        accounts.append(acc)
                            else:
                                acc = self._extract_account(data)
                                if acc:
                                    accounts.append(acc)
                    except:
                        pass
                else:  # .txt
                    lines = content.splitlines()
                    for line in lines:
                        line = line.strip()
                        if not line:
                            continue
                        sep = ':' if ':' in line else ' ' if ' ' in line else None
                        if sep:
                            parts = line.split(sep, 1)
                            if len(parts) == 2:
                                uid = parts[0].strip()
                                pwd = parts[1].strip()
                                if uid and pwd:
                                    accounts.append({'uid': uid, 'password': pwd, 'name': 'Unknown', 'account_id': 'N/A', 'region': 'IND'})
            except Exception as e:
                print(f"{Y}⚠️ Error reading {filepath}: {e}{R}")
        unique = []
        seen = set()
        for acc in accounts:
            key = (acc['uid'], acc['password'])
            if key not in seen:
                seen.add(key)
                unique.append(acc)
        print(f"{G}✨ Verified {len(unique)} unique database records successfully.{R}\n")
        return unique

    def _extract_account(self, obj):
        if not isinstance(obj, dict):
            return None
        uid = obj.get('uid') or obj.get('user') or obj.get('username') or obj.get('email')
        pwd = obj.get('password') or obj.get('pass')
        if uid and pwd:
            return {
                'uid': str(uid),
                'password': str(pwd),
                'name': obj.get('name', 'Unknown'),
                'account_id': obj.get('account_id', 'N/A'),
                'region': obj.get('region', 'IND')
            }
        return None

    def select_region_mode(self):
        print(f"\n{C}{B}🌍 REGION SELECTION{R}")
        print("1. Single region for ALL accounts")
        print("2. Keep each account's original region")
        choice = input(f"{C}🎯 Choice (1/2): {R}").strip()
        if choice == '1':
            regions = list(self.regions.keys())
            print(f"\n{C}Available regions:{R}")
            for i, r in enumerate(regions, 1):
                print(f"  {i}. {r}")
            reg_choice = input(f"{C}🎯 Select number: {R}").strip()
            if reg_choice.isdigit() and 1 <= int(reg_choice) <= len(regions):
                self.global_region = regions[int(reg_choice)-1]
                print(f"{G}✅ Using region: {self.global_region}{R}")
            else:
                self.global_region = 'IND'
                print(f"{Y}⚠️ Fallback IND{R}")
        else:
            self.global_region = None
            print(f"{C}ℹ️ Using per‑account region (default IND){R}")

    def save_results(self):
        tag = self.global_region if self.global_region else 'MULTI'
        filename = f'success-{tag}.json'
        with open(filename, 'w') as f:
            json.dump(self.successful_accounts, f, indent=2)
        print(f"\n{C}💾 Saved {len(self.successful_accounts)} accounts to {filename}{R}")

    def run(self, accounts):
        total = len(accounts)
        if total == 0:
            print(f"{RED}❌ No accounts to process{R}")
            return
        live_loading_animation(duration=1.6)
        print(f"{C}🚀 Deploying task pipeline with {self.max_workers} thread pools...{R}\n")
        start_time = time.time()
        self.stop_execution = False
        self.unauthorized_count = 0

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {executor.submit(self.activate_single_account, acc, i+1): acc for i, acc in enumerate(accounts)}
            for fut in as_completed(futures):
                if self.stop_execution:
                    print(f"\n{RED}🛑 Stopped due to 401 errors{R}")
                    break

        total_time = time.time() - start_time
        self.save_results()

        # Final summary
        summary_lines = [
            f" {W}Total Accounts   │{R} {Y}{total}{R}",
            f" {G}Successful       │{R} {G}{self.successful}{R}",
            f" {RED}Failed           │{R} {RED}{self.failed}{R}",
            f" {W}Total Time       │{R} {Y}{total_time:.2f}s{R}",
            f" {C}Speed            │{R} {M}{total/total_time:.1f} acc/s{R}",
            f" {C}Success Rate     │{R} {M}{self.successful/total*100:.1f}%{R}"
        ]
        print(f"\n{C}{B}╭─────────────────༺ FINAL REPORT ༻─────────────────╮")
        for line in summary_lines:
            print(f"║{R}{line:<63}{C}║")
        print(f"╰───────────────────────────────────────────────────────╯{R}")

def main():
    clear_screen()
    render_banner()
    activator = RealActivator(max_workers=64)
    source_path = activator.select_source_path()
    if source_path is None:
        print(f"{RED}❌ No valid source selected. Exiting.{R}")
        return
    accounts = activator.load_accounts_from_path(source_path)
    if accounts:
        activator.select_region_mode()
        activator.run(accounts)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}👋 Program shut down gracefully by system user.{R}")
        sys.exit(0)