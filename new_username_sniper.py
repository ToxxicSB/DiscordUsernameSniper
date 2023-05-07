# imports
import random, requests, datetime, time, json, os
from colorama import Fore, Style

# define
def current_time():
    return datetime.datetime.now().strftime("%d/%m·%H:%M")
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# setup if theres no config file
def setup():
    with open('./config.json', 'w') as fp:
        print(f'''                    {Fore.GREEN}Setup Configs
                    {Fore.LIGHTBLACK_EX}Fill Out Info
{Fore.WHITE}───────────────[GITHUB.COM/TOXXICSB]───────────────\n'''+Fore.RESET)
        token_here = input(f"{Fore.RED} ▸ {Style.BRIGHT}{Fore.BLACK}{current_time()}{Style.RESET_ALL}{Fore.YELLOW} [TOKEN]{Style.RESET_ALL}\n{Fore.RED} > {Fore.RESET}")
        username_here = input(f"{Fore.RED} ▸ {Style.BRIGHT}{Fore.BLACK}{current_time()}{Style.RESET_ALL}{Fore.YELLOW} [USERNAME]{Style.RESET_ALL}\n{Fore.RED} > {Fore.RESET}")
        setup_data = {
        "token": token_here,
        "username": username_here
        }
        json.dump(setup_data, fp, indent=4)
        clear()
        print(f"{Fore.RED} ▸ {Style.BRIGHT}{Fore.BLACK}{current_time()}{Style.RESET_ALL}{Fore.GREEN} [SETTINGS] {Fore.RESET}Settings can be changed at any time, please relaunch the Script")
        time.sleep(5)
        exit(0)

# configs
if os.path.exists('./config.json'):
    try:
        with open('config.json') as conf:
            config = json.load(conf)
            token = config.get('token')
            username = config.get('username')
    except:
        if os.path.getsize('./config.json') > 0:
            setup()    
else:
    setup()

# tells user script is running
print(f'''            {Fore.GREEN}Script Running Successfully
             {Fore.LIGHTBLACK_EX}Do Not Close This Window
{Fore.WHITE}───────────────[GITHUB.COM/TOXXICSB]───────────────\n'''+Fore.RESET)

# info to send with request
headers = {
    'Authorization': token,
    'content-type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.60 Chrome/108.0.5359.215 Electron/22.3.2 Safari/537.36'
}    
payload = {'username': username}

# loop requests and responces
while True:
    r = requests.post('https://discord.com/api/v9/users/@me/pomelo', headers=headers, json=payload, timeout=10)
    if r.status_code == 200:
        print(f"{Fore.RED} ▸ {Style.BRIGHT}{Fore.BLACK}{current_time()}{Style.RESET_ALL}{Fore.GREEN} [SUCCESS] {Fore.YELLOW}200 - Claimed username.\n"+Fore.RESET)
        break
    elif r.status_code == 535:
        print(f"{Fore.RED} ▸ {Style.BRIGHT}{Fore.BLACK}{current_time()}{Style.RESET_ALL}{Fore.RED} [ERROR] {Fore.YELLOW}535 - Username taken.\n"+Fore.RESET)
        break
    elif r.status_code == 401:
        print(f"{Fore.RED} ▸ {Style.BRIGHT}{Fore.BLACK}{current_time()}{Style.RESET_ALL}{Fore.RED} [ERROR] {Fore.YELLOW}401 - Unauthorized.\n"+Fore.RESET)
        wait = random.randrange(3600, 5400)     
        time.sleep(wait)
    elif r.status_code == 429:
        print(f"{Fore.RED} ▸ {Style.BRIGHT}{Fore.BLACK}{current_time()}{Style.RESET_ALL}{Fore.RED} [ERROR] {Fore.YELLOW}429 - Too many attempts.\n"+Fore.RESET)
        wait = random.randrange(3600, 5400)     
        time.sleep(wait)
    else:
        print(f"{Fore.RED} ▸ {Style.BRIGHT}{Fore.BLACK}{current_time()}{Style.RESET_ALL}{Fore.RED} [ERROR] {Fore.YELLOW}{r.status_code} - Unknown error.\n"+Fore.RESET)
        wait = random.randrange(900, 1800)
        time.sleep(wait)