import os
import random
import json
import requests
import time

# Function to clear screen based on OS
def clear_screen():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix-based OS (Linux/MacOS)
        os.system('clear')

# Function to generate random user agent
def generate_user_agent():
    os_list = ['Windows', 'Linux', 'iOS', 'Android']
    versions = ['8', '9', '10', '11', '12', '13', '14']
    devices = ['Samsung', 'Motorola', 'Xiaomi', 'Huawei', 'OnePlus']

    selected_os = random.choice(os_list)
    if selected_os == 'Android':
        version = random.choice(versions)
        device = random.choice(devices)
        user_agent = f"Mozilla/5.0 (Linux; Android {version}; {device}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36"
    else:
        user_agent = f"Mozilla/5.0 ({selected_os} NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"

    return user_agent + str(random.randint(1000000, 9999999))

# Function to print colored text
def print_colored(text, color):
    color_codes = {
        'green': '\033[32m',
        'red': '\033[31m',
        'yellow': '\033[33m',
        'blue': '\033[34m'
    }
    return f"{color_codes[color]}{text}\033[0m"

# Function to print banner
def print_banner():
    banner = """
-------------------------------------------------
    __  ______  ___    ______        __ 
  /  |/  / _ \/ _ \  /_  __/__ ____/ / 
 / /|_/ / , _/ ___/   / / / -_) __/ _ \
/_/  /_/_/|_/_/      /_/  \__/\__/_//_/           
-------------------------------------------------

     - NOT PIXEL VIP SCRIPT -
     - 100% ANTI-BAN -
     
- CREATE BY : MRP Tech
- Telegram: @mrptechofficial
- channel: https://t.me/mrptechofficial
 
- PX Points will be added to your account within 20 seconds.
- So Wait Sometimes.

-------------------------------------------------

"""
    print(print_colored(banner, 'green'))

# Check for users.json file
users_file = 'users.json'
if not os.path.exists(users_file):
    print(print_colored("Error: No users found! Please save a Telegram ID by running the command: python adduser.py\nFollow the on-screen instructions to add users.\n", 'red'))
    exit()

with open(users_file, 'r') as file:
    users = json.load(file)

user_points = {user_id: 0 for user_id in users}

# Function to generate random chat instance
def generate_chat_instance():
    return str(random.randint(10000000000000, 99999999999999))

# Function to make API request
def make_api_request(user_id, tg_id):
    url = f"https://api.adsgram.ai/adv?blockId=4853&tg_id={tg_id}&tg_platform=android&platform=Linux%20aarch64&language=en&chat_type=sender&chat_instance={generate_chat_instance()}&top_domain=app.notpx.app"
    
    user_agent = generate_user_agent()
    headers = {
        'Host': 'api.adsgram.ai',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'sec-ch-ua-platform': '"Android"',
        'User-Agent': user_agent,
        'sec-ch-ua': '"Android WebView";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'Accept': '*/*',
        'Origin': 'https://app.notpx.app',
        'X-Requested-With': 'org.telegram.messenger',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://app.notpx.app',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en,en-US;q=0.9'
    }

    response = requests.get(url, headers=headers)
    return response

# Function to extract reward value
def extract_reward(response):
    data = response.json()
    if data and 'banner' in data and 'trackings' in data['banner']:
        for tracking in data['banner']['trackings']:
            if tracking['name'] == 'reward':
                return tracking['value']
    return None

total_points = 0
first_run = True

while True:
    clear_screen()
    print_banner()

    if not first_run:
        for user_id, points in user_points.items():
            print("\n" + print_colored(f" ---> {user_id} +{points} PX", 'green'))
        print("\n" + print_colored(f"Total PX Earned [ +{total_points} ]\n", 'green'))

    rewards = {}
    headers = {}

    for user_id, user_data in users.items():
        tg_id = user_data['tg_id']
        
        print(print_colored("[ INFO ] Starting NOT PIXEL Engine", 'yellow'))
        print(print_colored(f"[ PROCESS ] Injecting V1 ---> TG ID | {user_id} ...", 'blue'))
        
        time.sleep(3)
        
        response = make_api_request(user_id, tg_id)
        
        if response.status_code == 200:
            reward = extract_reward(response)
            if reward:
                rewards[user_id] = reward
                headers[user_id] = response.headers
                print(print_colored(f"[ SUCCESS ] ++ Injected to {user_id}.", 'green'))
            else:
                print(print_colored("[ ERROR ] Ads watching limit reached.", 'red'))
                print(print_colored("[ SOLUTION ] Try VPN or wait for 24 hours.\nUse Proton VPN install it from play store.", 'green'))
                print(print_colored("[ REPORT ] If facing issue again and again Send Details and ScreenShot Contact Developer Telegram @mosibur_paik\n", 'yellow'))
                continue
        elif response.status_code == 403:
            print(print_colored("[ ERROR ] Seems like your IP address is banned", 'red'))
            print(print_colored("[ SOLUTION ] Use Proton VPN install it from play store.", 'yellow'))
            exit()
        else:
            if response.status_code == 400 and 'block_error' in response.text:
                print(print_colored("[ ERROR ] Ads Block error - Ignore it will be fixed automatically -", 'red'))
                continue
            print(print_colored(f"[ ERROR ] HTTP Error: {response.status_code}", 'red'))
            continue

    for i in range(20, 0, -1):
        print(f"\r-----> Cooldown {i} seconds left...", end="")
        time.sleep(1)
    print("\n")

    for user_id, reward in rewards.items():
        print(print_colored(f"[ PROCESS ] Injecting V2 ---> {user_id} ]", 'yellow'))
        
        req_headers = headers[user_id]
        
        response = requests.get(reward, headers=req_headers)
        http_code = response.status_code

        if http_code == 200:
            total_points += 16
            user_points[user_id] += 16
            print(print_colored(f"[ SUCCESS ] ++ {user_id} +16 PX", 'green'))
        else:
            print(print_colored(f"[ ERROR ] Failed to inject for {user_id}. HTTP Code: {http_code}", 'red'))

    first_run = False
