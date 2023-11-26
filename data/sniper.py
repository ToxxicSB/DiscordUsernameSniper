# imports
import selfcord, random, datetime, os, json, ctypes, time, psutil, asyncio#, aiohttp, requests
from colorama import Fore, Style
from selfcord.ext import commands

# define
version = '1.0.0'
ctypes.windll.kernel32.SetConsoleTitleW(f'ToxxicUsernameSniper | Connecting...') 
loop = asyncio.get_event_loop()

def current_time():
    return datetime.datetime.now().strftime("%d/%m·%H:%M")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def setup():
    ctypes.windll.kernel32.SetConsoleTitleW(f'Toxxic UsernameSniper | Setup')
    with open('./config.json', 'w') as fp:
        print(f"""{Fore.WHITE} ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
{Fore.RED} 
                                 ▄████████    ▄████████     ███     ███    █▄     ▄███████▄ 
                                ███    ███   ███    ███ ▀█████████▄ ███    ███   ███    ███ 
                                ███    █▀    ███    █▀     ▀███▀▀██ ███    ███   ███    ███ 
                                ███         ▄███▄▄▄         ███   ▀ ███    ███   ███    ███ 
                              ▀███████████ ▀▀███▀▀▀         ███     ███    ███ ▀█████████▀  
                                       ███   ███    █▄      ███     ███    ███   ███        
                                 ▄█    ███   ███    ███     ███     ███    ███   ███        
                               ▄████████▀    ██████████    ▄████▀   ████████▀   ▄████▀   v{version}

{Fore.WHITE} ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n""")
        token_here = input(f"{Fore.RED} ▸ {Style.BRIGHT}{Fore.BLACK}{current_time()}{Style.RESET_ALL}{Fore.YELLOW} [TOKEN]{Style.RESET_ALL}\n{Fore.RED} > {Fore.RESET}")
        password_here = input(f"{Fore.RED} ▸ {Style.BRIGHT}{Fore.BLACK}{current_time()}{Style.RESET_ALL}{Fore.YELLOW} [PASSWORD]{Style.RESET_ALL}\n{Fore.RED} > {Fore.RESET}")
        #ask key and value for the numKeys
        for nameValuePair in range(1):
            usernameCount = int(input(f"{Fore.RED} ▸ {Style.BRIGHT}{Fore.BLACK}{current_time()}{Style.RESET_ALL}{Fore.YELLOW} [HOW MANY USERNAMES]{Style.RESET_ALL}\n{Fore.RED} > {Fore.RESET}"))
            usernameList = []
            for value in range(usernameCount):
                usernameList.append(input(f"{Fore.RED} ▸ {Style.BRIGHT}{Fore.BLACK}{current_time()}{Style.RESET_ALL}{Fore.YELLOW} [ENTER USERNAME]{Style.RESET_ALL}\n{Fore.RED} > {Fore.RESET}"))
        setup_data = {
        "token": token_here,
        "password": password_here,
        "usernames": usernameList
        }
        json.dump(setup_data, fp, indent=4)
        clear()
        print(f"{Fore.RED}▸ {Style.BRIGHT}{Fore.BLACK}{current_time()}{Style.RESET_ALL}{Fore.GREEN} [SETTINGS]{Fore.RESET} settings can be changed at any time, please relaunch the Program")
        time.sleep(5)
        exit(0)
        

if os.path.exists('./config.json'):
    try:
        with open('config.json') as conf:
            config = json.load(conf)
            token = config.get('token')
            password = config.get('password')
            prefix = config.get('prefix')
            usernames = config.get('usernames')
    except:
        if os.path.getsize('./config.json') > 0:
            setup()    
else:
    setup()

#class CaptchaSolver(selfcord.CaptchaHandler):
#    async def fetch_token(data: dict, proxy: str, proxy_auth: aiohttp.BasicAuth) -> str:
#        token = token
#        return token
     
bot = selfcord.Client(status=selfcord.Status.offline, sync_presence=False) #captcha_handler=CaptchaSolver()

def startprint():
    clear()
    print(f'''{Fore.RESET}{Style.BRIGHT}{Fore.BLACK}                                             [github.com/toxxicsb]{Style.RESET_ALL}
{Fore.WHITE} ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
{Fore.RED}
                         ███      ▄██████▄  ▀████    ▐████▀ ▀████    ▐████▀  ▄█   ▄████████ 
                     ▀█████████▄ ███    ███   ███▌   ████▀    ███▌   ████▀  ███  ███    ███ 
                        ▀███▀▀██ ███    ███    ███  ▐███       ███  ▐███    ███▌ ███    █▀   
                         ███   ▀ ███    ███    ▀███▄███▀       ▀███▄███▀    ███▌ ███        
                         ███     ███    ███    ████▀██▄        ████▀██▄     ███▌ ███        
                         ███     ███    ███   ▐███  ▀███      ▐███  ▀███    ███  ███    █▄  
                         ███     ███    ███  ▄███     ███▄   ▄███     ███▄  ███  ███    ███ 
                        ▄████▀    ▀██████▀  ████       ███▄ ████       ███▄ █▀   ████████▀  
                 ▄• ▄▌.▄▄ · ▄▄▄ .▄▄▄   ▐ ▄  ▄▄▄· • ▌ ▄ ·. ▄▄▄ .    .▄▄ ·  ▐ ▄ ▪   ▄▄▄·▄▄▄ .▄▄▄  
                 █▪██▌▐█ ▀. ▀▄.▀·▀▄ █·•█▌▐█▐█ ▀█ ·██ ▐███▪▀▄.▀·    ▐█ ▀. •█▌▐███ ▐█ ▄█▀▄.▀·▀▄ █·
                 █▌▐█▌▄▀▀▀█▄▐▀▀▪▄▐▀▀▄ ▐█▐▐▌▄█▀▀█ ▐█ ▌▐▌▐█·▐▀▀▪▄    ▄▀▀▀█▄▐█▐▐▌▐█· ██▀·▐▀▀▪▄▐▀▀▄ 
                 ▐█▄█▌▐█▄▪▐█▐█▄▄▌▐█•█▌██▐█▌▐█ ▪▐▌██ ██▌▐█▌▐█▄▄▌    ▐█▄▪▐███▐█▌▐█▌▐█▪·•▐█▄▄▌▐█•█▌
                  ▀▀▀  ▀▀▀▀  ▀▀▀ .▀  ▀▀▀ █▪ ▀  ▀ ▀▀  █▪▀▀▀ ▀▀▀      ▀▀▀▀ ▀▀ █▪▀▀▀.▀    ▀▀▀ .▀  ▀                                                                    
                                                    v{version}
{Fore.WHITE} ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n'''+Fore.RESET)

async def title():
    while True:
            cpuavg = psutil.cpu_percent(interval=1)
            mem = psutil.virtual_memory()[2]
            ctypes.windll.kernel32.SetConsoleTitleW(f'Toxxic UsernameSniper v{version} | [{cpuavg}% - {mem}mb]')
            await asyncio.sleep(5)

async def pomelo():
    for username in usernames:
        usernameTaken = await bot.check_pomelo_username(username)
        if usernameTaken == False:
            if bot.user.is_pomelo:
                await bot.user.edit(username=username, password=password)
                print(f"{Fore.RED} ▸ {Style.BRIGHT}{Fore.BLACK}{current_time()}{Style.RESET_ALL}{Fore.GREEN} [SUCCESS] {Fore.YELLOW}200 - Claimed '{username}' username.\n"+Fore.RESET)
            else:
                await bot.user.edit(pomelo=True, username=username, password=password)
                print(f"{Fore.RED} ▸ {Style.BRIGHT}{Fore.BLACK}{current_time()}{Style.RESET_ALL}{Fore.GREEN} [SUCCESS] {Fore.YELLOW}200 - Converted and claimed '{username}' username.\n"+Fore.RESET)
            break   
        if usernameTaken == True:
            print(f"{Fore.RED} ▸ {Style.BRIGHT}{Fore.BLACK}{current_time()}{Style.RESET_ALL}{Fore.RED} [ERROR] {Fore.YELLOW}535 - Username '{username}' taken.\n"+Fore.RESET)
            wait = random.randrange(15, 60)     
            time.sleep(wait)

@bot.event
async def on_connect():
    loop.create_task(title())
    startprint()
    bot.loop.create_task(pomelo())

@bot.event
async def on_error(error): 
    error_str = str(error)
    error = getattr(error, 'original', error)
    errormsg = f"{Fore.RED}▸ {Style.BRIGHT}{Fore.BLACK}{current_time()}{Style.RESET_ALL} {Fore.RED}[ERROR] {Fore.YELLOW}"
    if isinstance(error, selfcord.CaptchaRequired):
        print(f"{errormsg}Discord error: CaptchaRequired{Fore.RESET}")
    elif isinstance(error, selfcord.errors.Forbidden):
       print(f"{errormsg}Discord error: {error}{Fore.RESET}")  
    else:
        print(f"{errormsg}{error_str}{Fore.RESET}")

# info to send with request
#username =
#headers = {
#    'Authorization': token,
#    'content-type': 'application/json',
#    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.60 Chrome/108.0.5359.215 Electron/22.3.2 Safari/537.36'
#}    
#payload = {'username': username}
# loop requests and responces
#while True:
#    r = requests.post('https://discord.com/api/v9/users/@me/pomelo', headers=headers, json=payload, timeout=10)
#    if r.status_code == 200:
#        print(f"{Fore.RED} ▸ {Style.BRIGHT}{Fore.BLACK}{current_time()}{Style.RESET_ALL}{Fore.GREEN} [SUCCESS] {Fore.YELLOW}200 - Claimed username.\n"+Fore.RESET)
#        break
#    elif r.status_code == 535:
#        print(f"{Fore.RED} ▸ {Style.BRIGHT}{Fore.BLACK}{current_time()}{Style.RESET_ALL}{Fore.RED} [ERROR] {Fore.YELLOW}535 - Username taken.\n"+Fore.RESET)
#        break
#    elif r.status_code == 401:
#        print(f"{Fore.RED} ▸ {Style.BRIGHT}{Fore.BLACK}{current_time()}{Style.RESET_ALL}{Fore.RED} [ERROR] {Fore.YELLOW}401 - Unauthorized.\n"+Fore.RESET)
#        wait = random.randrange(3600, 5400)     
#        time.sleep(wait)
#    elif r.status_code == 429:
#        print(f"{Fore.RED} ▸ {Style.BRIGHT}{Fore.BLACK}{current_time()}{Style.RESET_ALL}{Fore.RED} [ERROR] {Fore.YELLOW}429 - Too many attempts.\n"+Fore.RESET)
#        wait = random.randrange(3600, 5400)     
#        time.sleep(wait)
#    else:
#        print(f"{Fore.RED} ▸ {Style.BRIGHT}{Fore.BLACK}{current_time()}{Style.RESET_ALL}{Fore.RED} [ERROR] {Fore.YELLOW}{r.status_code} - Unknown error.\n"+Fore.RESET)
#        wait = random.randrange(900, 1800)
#        time.sleep(wait)

try:
    bot.run(token, reconnect=True, log_handler=None)
except Exception as e:
    print(e)
    os.system('pause >NUL')