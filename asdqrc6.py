import requests
import random
import string
import concurrent.futures
import os
import time
from colorama import Fore, Style, init

# تهيئة الألوان
init(autoreset=True)

# الرسمة باللون الأخضر
GREEN_ART = f"""{Fore.GREEN}
⠉⠉⠉⠉⠁⠀⠀⠀⠀⠒⠂⠰⠤⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠻⢤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠠⠀⠐⠒⠒⠀⠀⠈⠉⠉⠉⠉⢉⣉⣉⣉⣙⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡀⠤⠒⠒⠉⠁⠀⠀⠀⠀⠳⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⠛⠛⠉⠛⠛⠶⢦⣤⡐⢀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠁⠀⠀⠀⠀⠀⠀⠀⠈⠉⢳⣦⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⡤⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠛⠳⠶⢶⣦⠤⣄⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⣄⠉⠑⢄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡀⠀⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄
"""

BANNER = f"""
{GREEN_ART}
{Fore.RED}          _______  ______   _______  _______  _______  _______ _________
{Fore.RED}         (  ___  )(  ____ \ (  __  \ (  ___  )(  ____ )(  ____ \\__   __/
{Fore.RED}         | (   ) || (    \/ | (  \  )| (   ) || (    )|| (    \/   ) (   
{Fore.RED}         | (___) || (_____  | |   ) || |   | || (____)|| |         | |   
{Fore.WHITE}         |  ___  |(_____  ) | |   | || |   | ||     __)| |         | |   
{Fore.WHITE}         | (   ) |      ) | | |   ) || |   | || (\ (   | |         | |   
{Fore.WHITE}         | )   ( |/\____) | | (__/  )| (___) || ) \ \__| (____/\   | |   
{Fore.RED}         |/     \|\_______) (______/ (_______)|/   \__/(_______/   )_(   
{Fore.YELLOW}
{Fore.YELLOW}                    [ MISSION: DISCORD SNIPER V99 ]
{Fore.YELLOW}                    [ DEVELOPED BY: ASDQRC7       ]
{Fore.WHITE}______________________________________________________________________
"""

# قائمة User-Agents للتمويه الاحترافي
UA_LIST = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15"
]

def check_user():
    username = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(4))
    url = f"https://discord.com/api/v9/users/@me/suffixes?username={username}"
    
    headers = {
        "User-Agent": random.choice(UA_LIST),
        "Content-Type": "application/json",
        "Authorization": "undefined" # محاكاة طلب غير مسجل الدخول
    }

    try:
        # استخدام Session لرفع الأداء
        with requests.Session() as session:
            response = session.get(url, headers=headers, timeout=2)
            
            if response.status_code == 200:
                print(f"{Fore.GREEN}[⚡ HIT] ASDQRC7 -> {username}")
                with open("asdqrc7_found.txt", "a") as f:
                    f.write(f"{username}\n")
            elif response.status_code == 429:
                print(f"{Fore.YELLOW}[!] RATE LIMIT - SLOWING DOWN")
                time.sleep(1)
            else:
                print(f"{Fore.BLACK}[-] TAKEN: {username}")
    except:
        pass

def start():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(BANNER)
    # رفع القوة لـ 50 مسار (أقصى قدرة تحمل)
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        while True:
            executor.submit(check_user)

if __name__ == "__main__":
    start()
