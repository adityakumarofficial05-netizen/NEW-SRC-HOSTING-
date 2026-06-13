import os
import sys
import time
import json
import threading
import requests
import urllib3
import SpecialFriend_pb2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

urllib3.disable_warnings()


GUEST_UID = "4785573108"
GUEST_PASSWORD = "ADI-33FO9W0B"


AeSkEy = b'Yg&tc%DEuh6%Zc^8'
AeSiV  = b'6oyZDr22E3ychjM%'
BASE_URL = "https://client.ind.freefiremobile.com"

C = "\033[1;36m"
G = "\033[1;32m"
R = "\033[1;31m"
Y = "\033[1;33m"
W = "\033[1;37m"
B = "\033[1m"
S = "\033[0m"

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def draw_line():
    print(f"{C}══════════════════════════════════════════════════════{S}")

def banner():
    clear()
    ascii_art = f"""{C}
  ███████╗ ██████╗  ██╗ ██████╗  ███████╗ ██╗   ██╗
  ██╔════╝ ██╔══██╗ ██║ ██╔══██╗ ██╔════╝ ╚██╗ ██╔╝
  ███████╗ ██████╔╝ ██║ ██║  ██║ █████╗    ╚████╔╝ 
  ╚════██║ ██╔═══╝  ██║ ██║  ██║ ██╔══╝     ╚██╔╝  
  ███████║ ██║      ██║ ██████╔╝ ███████╗    ██║   
  ╚══════╝ ╚═╝      ╚═╝ ╚═════╝  ╚══════╝    ╚═╝   {S}"""
    print(ascii_art) 
    draw_line()
    print(f"{W}{B}             FF DYNAMIC DUO INFO EXTRACTOR{S}")
    draw_line()

def show_credits():
    draw_line()
    print(f"\n {C}[★] {W}Developer : {C}@spideyabd And @INDRAJIT_1M{S}")
    print(f" {C}[★] {W}Join      : {G}t.me/SPIDEYFREEFILES{S}")
    print(f" {C}[★] {W}Join      : {G}t.me/INDRAJITFREEAPI{S}\n")

def enc(d):
    return AES.new(AeSkEy, AES.MODE_CBC, AeSiV).encrypt(pad(d, 16))

def dec(d):
    try:
        return unpad(AES.new(AeSkEy, AES.MODE_CBC, AeSiV).decrypt(d), 16)
    except:
        return d

def build_uid_protobuf(uid):
    def to_varint(n):
        res = bytearray()
        while n >= 0x80:
            res.append((n & 0x7f) | 0x80)
            n >>= 7
        res.append(n)
        return bytes(res)
    return enc(b"\x08" + to_varint(int(uid)))

def format_timestamp(ts):
    try:
        return time.strftime('%B %d, %Y at %I:%M %p', time.localtime(ts))
    except (ValueError, TypeError):
        return "Invalid Timestamp"

def fetch_jwt_token():
    url = f"https://ff-jwt-gen-api.lovable.app/api/public//token?uid={GUEST_UID}&password={GUEST_PASSWORD}"
    try:
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            return response.json().get("token")
    except:
        return None
    return None

def decode_protobuf_data(binary_data):
    try:
        if not binary_data or len(binary_data) < 2:
            return None, "Empty Response"

        response = SpecialFriend_pb2.SpecialFriendResponse()
        response.ParseFromString(binary_data)

        if not response.HasField("duo_info"):
            return None, "No Dynamic Duo info found"

        duo = response.duo_info
        score = duo.score

        if score < 101: calc_level = 1
        elif score < 301: calc_level = 2
        elif score < 501: calc_level = 3
        elif score < 801: calc_level = 4
        elif score < 1201: calc_level = 5
        else: calc_level = 6

        calc_status = "Active" if getattr(duo, "status", 0) == 2 else "Inactive"

        result = {
            "partner_uid": str(duo.partner_uid),
            "level": calc_level,
            "score": score,
            "days_active": duo.days_active,
            "time_created": format_timestamp(duo.creation_timestamp),
            "creation_timestamp": duo.creation_timestamp,
            "status": calc_status
        }
        return result, "Success"
    except Exception as e:
        return None, f"Parsing Error: {str(e)}"

def fetch_with_loader(target_uid):
    """Fetches data concurrently while animating the loader for zero lag."""
    result_data = {"jwt_token": None, "response": None, "error": None}
    
    def worker():
        try:
            jwt = fetch_jwt_token()
            result_data["jwt_token"] = jwt
            if jwt:
                headers = {
                    "Authorization": f"Bearer {jwt}",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11)",
                    "X-GA": "v1 1",
                    "ReleaseVersion": "OB53",
                    "Connection": "Keep-Alive"
                }
                payload = build_uid_protobuf(target_uid)
                resp = requests.post(
                    f"{BASE_URL}/GetSpecialFriendList", 
                    headers=headers, 
                    data=payload, 
                    timeout=15, 
                    verify=False
                )
                result_data["response"] = resp
        except Exception as e:
            result_data["error"] = e

    t = threading.Thread(target=worker)
    t.start()
    
    spinner =['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    bar_length = 30
    print()
    i = 0.0
    spin_idx = 0
    
    while t.is_alive():
        percent = min(99, int(i))
        spin = spinner[spin_idx % len(spinner)]
        filled = int(bar_length * percent / 100)
        bar = '█' * filled + '░' * (bar_length - filled)
        
        sys.stdout.write(f"\r {C}[{spin}] {W}FETCHING: {C}[{W}{bar}{C}] {G}{percent}%{S}")
        sys.stdout.flush()
        
        time.sleep(0.05)
        spin_idx += 1
        if i < 99:
            i += 1.5
            
    filled = bar_length
    bar = '█' * filled
    sys.stdout.write(f"\r {C}[✔] {W}FETCHING: {C}[{W}{bar}{C}] {G}100%{S}")
    sys.stdout.flush()
    print("\n")
    
    return result_data

def main():
    os.system("")
    
    while True:
        banner()
        print(f"\n {W}[#] {C}Instruction:{W} Enter Target Player UID.")
        print(f" {W}[#] {C}Command:{W} Type 'Q' to exit the application.\n")
        
        target_uid = input(f"{Y} [>] {W}Enter Target UID: {S}").strip()

        if target_uid.upper() == 'Q' or target_uid.upper() == 'EXIT':
            break

        if not target_uid.isdigit():
            print(f"\n{R}[!] Error: UID must contain only numbers.{S}\n")
            print(f"{C} [➔] Press[ENTER] to try a different UID...{S}")
            input()
            continue

        try:
            fetch_result = fetch_with_loader(target_uid)
            
            if fetch_result.get("error"):
                raise fetch_result["error"]
                
            jwt_token = fetch_result.get("jwt_token")
            
            if not jwt_token:
                print(f"{R} [!] System Error: Failed to generate API token.{S}\n")
                show_credits()
                print(f"{C} [➔] Press [ENTER] to restart...{S}")
                input()
                continue

            response = fetch_result.get("response")

            if response and response.status_code == 200:
                decrypted_data = dec(response.content)
                parsed_data, error_msg = decode_protobuf_data(decrypted_data)
                
                if parsed_data:
                    banner()
                    
                    print(f"\n{G} [✓] {B}{W}DUO DETAILS RETRIEVED{S}\n")
                    
                    print(f" {C}[◆] Partner UID  :{W} {parsed_data.get('partner_uid')}")
                    print(f" {C}[◆] Intimacy Score  :{Y} {parsed_data.get('score')}{S}")
                    print(f" {C}[◆] Duo Level    :{Y} Level {parsed_data.get('level')}{S}")
                    print(f" {C}[◆] Days Active  :{G} {parsed_data.get('days_active')} Days{S}")
                    print(f" {C}[◆] Created On   :{W} {parsed_data.get('time_created')}")
                    
                    status_val = parsed_data.get('status')
                    status_col = G if status_val == 'Active' else R
                    print(f" {C}[◆] Duo Status   :{status_col} {status_val}{S}")
                    
                    show_credits()
                    
                    print(f"{C} [➔] Search completed successfully.{S}")
                    print(f"{W} [➔] Press[ENTER] to perform another lookup...{S}")
                    input()
                else:
                    print(f"{R}[✗] No records found for the UID: {W}{target_uid}{S}")
                    print(f"{R}    Reason: {error_msg}{S}\n")
                    show_credits()
                    
                    print(f"{C} [➔] Please check the UID and try again.{S}")
                    print(f"{W}[➔] Press [ENTER] to return to search...{S}")
                    input()

            elif response and response.status_code == 500:
                print(f"{R}[✗] Server Error (500) for UID: {W}{target_uid}{S}")
                print(f"{R}    Reason: Invalid UID, Private Profile, or Expired Token.{S}\n")
                show_credits()
                
                print(f"{C} [➔] Please check the UID and try again.{S}")
                print(f"{W} [➔] Press [ENTER] to return to search...{S}")
                input()
            else:
                status_code = response.status_code if response else "Unknown"
                print(f"{R}[✗] Failed: HTTP {status_code} for UID: {W}{target_uid}{S}\n")
                show_credits()
                
                print(f"{C} [➔] Please check the connection and try again.{S}")
                print(f"{W}[➔] Press [ENTER] to return to search...{S}")
                input()

        except Exception as e:
            print(f"{R} [!] System Error: Connection could not be established.{S}\n")
            show_credits()
            
            print(f"{W} [➔] Press [ENTER] to restart...{S}")
            input()

    clear()
    draw_line()
    print(f"\n{G} [★] Wishing you a wonderful journey ahead. Goodbye!{S}")
    print(f"{W}     Keep shining, stay strong, and be well until next time.{S}\n")
    draw_line()
    
    print()
    print(f"{C}═══════════════════ SESSION CLOSED ═══════════════════{S}\n")
    sys.exit()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{R} [!] Session interrupted by user.{S}")
        sys.exit()
