import requests
import json
import hashlib
import hmac
import binascii
import datetime
import time
import os
import subprocess
import sys
from datetime import timezone

ACCESS_KEY = "add_your_VMOS_access_key"
SECRET_KEY = "add_your_VMOS_secret_key"
PAD_CODE = "add_your_VMOS_PAD_CODE"

FF_PACKAGE = "com.dts.freefireth"
FF_APK_URL = "https://dl.cdn.freefiremobile.com/live/package/FreeFire.apk"

AUTOCLICKER_PACKAGE = "com.truedevelopersstudio.automatictap.autoclicker"
AUTOCLICKER_APK_URL = "https://github.com/Shyamnpl/RDPv2/releases/download/v4.0/AutoClicker.apk"

GUEST_UID = "5054283688"
GUEST_PASSWORD = "gggh-AXI60NE1"
GUEST_FILE_PATH = "/storage/emulated/0/com.garena.msdk/guest100067.dat"

# FIXED CONFIG CONTENT - Valid JSON for AutoClicker
CONFIG_CONTENT = {
    "targets": [
        {"delayUnit": 1, "delayValue": 3, "duration": 0, "type": 0, "xPos": 207, "xPos1": -1, "yPos": 335, "yPos1": -1},
        {"delayUnit": 0, "delayValue": 300, "duration": 0, "type": 0, "xPos": 1047, "xPos1": -1, "yPos": 650, "yPos1": -1},
        {"delayUnit": 1, "delayValue": 4, "duration": 0, "type": 0, "xPos": 1060, "xPos1": -1, "yPos": 494, "yPos1": -1},
        {"delayUnit": 0, "delayValue": 300, "duration": 0, "type": 0, "xPos": 1195, "xPos1": -1, "yPos": 496, "yPos1": -1}
    ],
    "antiDetection": False,
    "id": 0,
    "name": "Configbeta",
    "numberOfCycles": 10,
    "stopConditionChecked": 0,
    "timeValue": 300
}

GUEST_ACCOUNT = {
    "id": "id",
    "password": "Password",
    "account_id": "id",
    "name": "name of your id",
    "region": "region",
    "status": "activated"
}

# VMOS Cloud ADB settings (default local connection)
VMOS_ADB_HOST = "127.0.0.1"
VMOS_ADB_PORT = "5555"

def run_adb(cmd, connect_first=False):
    if connect_first:
        subprocess.run(f"adb connect {VMOS_ADB_HOST}:{VMOS_ADB_PORT}", shell=True, capture_output=True)
        time.sleep(2)
    full_cmd = f"adb -s {VMOS_ADB_HOST}:{VMOS_ADB_PORT} {cmd}"
    try:
        result = subprocess.run(full_cmd, shell=True, capture_output=True, text=True, timeout=30)
        return result.stdout.strip(), result.stderr.strip(), result.returncode
    except:
        return "", "Timeout", -1

def tap(x, y):
    run_adb(f"shell input tap {x} {y}")
    time.sleep(0.5)

def wait(seconds):
    time.sleep(seconds)

def connect_vmos():
    print("[*] Connecting to VMOS Cloud...")
    stdout, stderr, code = run_adb("devices", connect_first=True)
    if f"{VMOS_ADB_HOST}:{VMOS_ADB_PORT}" in stdout and "device" in stdout:
        print("[+] Connected to VMOS Cloud")
        return True
    else:
        print("[!] VMOS Cloud not reachable. Make sure VMOS is running and ADB over network enabled.")
        return False

def install_apk(url, package):
    apk_path = f"/tmp/{package}.apk"
    stdout, _, _ = run_adb(f"shell pm list packages | grep {package}")
    if package in stdout:
        print(f"- {package} already installed.")
        return True
    print(f"- Installing {package} ...")
    response = requests.get(url, stream=True)
    with open(apk_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    run_adb(f"install -r {apk_path}")
    os.remove(apk_path)
    print(f"- {package} installed.")
    return True

def inject_guest_file():
    print("- Injecting guest account file (overwriting if exists)...")
    guest_data = {
        "uid": GUEST_ACCOUNT["id"],
        "password": GUEST_ACCOUNT["password"],
        "account_id": GUEST_ACCOUNT["account_id"],
        "name": GUEST_ACCOUNT["name"],
        "region": GUEST_ACCOUNT["region"],
        "status": GUEST_ACCOUNT["status"]
    }
    with open("/tmp/guest.dat", "w") as f:
        json.dump(guest_data, f)
    run_adb("shell mkdir -p /storage/emulated/0/com.garena.msdk/")
    run_adb(f"push /tmp/guest.dat {GUEST_FILE_PATH}")
    run_adb("shell chmod 644 " + GUEST_FILE_PATH)
    os.remove("/tmp/guest.dat")
    print("- Guest file injected.")

def inject_config():
    print("- Injecting config.txt into Downloads folder (overwriting if exists)...")
    config_str = json.dumps(CONFIG_CONTENT)
    with open("/tmp/config.txt", "w") as f:
        f.write(config_str)
    run_adb("push /tmp/config.txt /storage/emulated/0/Downloads/config.txt")
    os.remove("/tmp/config.txt")
    print("- config.txt injected.")

def setup_autoclicker():
    print("\n## Starting AutoClicker configuration sequence...")
    steps = [
        (585,1011), (234,329), (587,510), (380,953), (64,107),
        (260,744), (681,133), (425,115), (61,90), (180,450),
        (187,673), (455,230)
    ]
    for x,y in steps:
        tap(x,y)
        wait(1)
    print("## AutoClicker configuration complete!")

def open_freefire():
    print("\n## Opening Free Fire...")
    run_adb(f"shell am force-stop {FF_PACKAGE}")
    wait(2)
    run_adb(f"shell monkey -p {FF_PACKAGE} 1")
    wait(8)
    guest_steps = [(320,1160), (360,800), (371,1242), (572,794)]
    for x,y in guest_steps:
        tap(x,y)
        wait(2)
    print("## Free Fire opened and logged in!")

def press_keys():
    print("\n## Buttons")
    keys = ['F', 'Q', 'A', 'START', '3', '4', '5', '6', '7', '8', '9', '0']
    for key in keys:
        print(f"- {key}")
        if key == 'START':
            run_adb("shell input keyevent KEYCODE_ENTER")
        else:
            run_adb(f"shell input keyevent KEYCODE_{key}")
        time.sleep(0.3)

def start_farming(cycles=10):
    print(f"\n## Starting farming for {cycles} cycles...")
    for cycle in range(cycles):
        print(f"\n### Cycle {cycle + 1}/{cycles}")
        tap(455, 230)
        wait(5)
        for remaining in range(300, 0, -30):
            print(f"\r    Match ends in {remaining} seconds...", end="", flush=True)
            time.sleep(30)
        print("\r    Match ends in 0 seconds...    ")
        tap(1195, 496)
        wait(3)
        print(f"### Cycle {cycle + 1} complete")
    print("\n## Farming completed!")

def main():
    print("\n# VMOS Cloud Auto Level-Up Script")
    print("# For Garena Free Fire\n")
    if not connect_vmos():
        return
    install_apk(FF_APK_URL, FF_PACKAGE)
    install_apk(AUTOCLICKER_APK_URL, AUTOCLICKER_PACKAGE)
    inject_guest_file()
    inject_config()
    setup_autoclicker()
    open_freefire()
    press_keys()
    start_farming(cycles=10)
    print("\n# Script finished successfully!")
    print(f"# Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()