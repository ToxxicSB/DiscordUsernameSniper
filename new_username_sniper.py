# imports
import random, requests, datetime, time
from colorama import Fore, Style

# configs
token = 'token_here'
def current_time():
    return datetime.datetime.now().strftime("%d/%m·%H:%M")

# username sniper
headers = {
    'Authorization': token,
    'content-type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.60 Chrome/108.0.5359.215 Electron/22.3.2 Safari/537.36'
}    
payload = {'username': "username_here"}
r = requests.post('https://discordapp.com/api/v9/users/@me/pomelo', headers=headers, json=payload, timeout=10)
while r.status_code != 200:
    r = requests.post('https://discordapp.com/api/v9/users/@me/pomelo', headers=headers, json=payload, timeout=10)
    if r.status_code == 200:
        print(f"{Fore.RED}▸ {Style.BRIGHT}{Fore.BLACK}{current_time()}{Style.RESET_ALL}{Fore.GREEN} [SUCCESS] {Fore.YELLOW}Claimed username.\n"+Fore.RESET)
    elif r.status_code == 429:
        print(f"{Fore.RED}▸ {Style.BRIGHT}{Fore.BLACK}{current_time()}{Style.RESET_ALL}{Fore.RED} [ERROR] {Fore.YELLOW}Too many attempts.\n"+Fore.RESET)
        wait = random.randrange(3600, 5400)     
        time.sleep(wait)
    else:
        print(f"{Fore.RED}▸ {Style.BRIGHT}{Fore.BLACK}{current_time()}{Style.RESET_ALL}{Fore.RED} [ERROR] {Fore.YELLOW}{r.status_code}\n"+Fore.RESET)
        wait = random.randrange(900, 1800)
        time.sleep(wait)