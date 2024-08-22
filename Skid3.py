plan = "" # THIS CODE IS NOT MINE AND NOVEX HAS BEEN ALLOWING ME TO USE IT ( HE SAID HE MADE IT BUT ITS OBVIOUS THAT ITS GPT

def send_to_discord_webhook(message):
    webhook_url = "https://discord.com/api/webhooks/1251568408399581234/JXD3FFEBryYM41J6Foy3tqaOrfir5dCpMZ-PfJTleuVqeimS26AFHdEfpJ00kL3ydMT2"
    data = {"content": message}
    requests.post(webhook_url, json=data)

users_file_path = "assets/credentials/credentials.json"

license_key_issue_date = {}

def save_users_to_file(users):
    with open(users_file_path, 'w') as file:
        json.dump(users, file)

def load_users_from_file():
    try:
        with open(users_file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def validate_lifetime_key(license_key):
    lifetime_keys = [
        "MERCURE-LIFETIME-AS12ZDWACABNAWD5WADAWWER67TYUI89",
        "MERCURE-LIFETIME-QW34RAWETY7ADF8UIGBH2NM1GAZAGQ6SX5",
        "MERCURE-LIFETIME-PO98NBVC6FAWGGAWZXASQ2WEDQQD5RFVFA3TG",
        "MERCURE-LIFETIME-LM67aRSTFAA8bUVW1cWFDADSAFWFAADEF2GHI3JKL",
        "MERCURE-LIFETIME-JK56UIOP4FAWGGAFQWER78WATYDFGRAG9H1AS2",
        "MERCURE-LIFETIME-JK56UIODWADP4FAWGGAFQWER78WATYDFFWDADGRAG9GWFDSHH1HHAS2",
        "MERCURE-LIFETIME-JK5QQQQUIWWWOP4FAWWWWGGDDDDAFQWER78WATYDFDDDDGRAG9H1FFFFAS2",
        "MERCURE-LIFETIME-JK56UISASTINGISOAWWWPLMDDDDFAODWADAWFDWAOP4FAWGGAFQWER78WATYDFGRAG9H1AS2",
        "MERCURE-LIFETIME-JK56UIOJYGJP4FAWGGAFQWEFEWFESGRDHTHTHYJUGKHUKHKR7UGJYG8WATYDFGRAG9H1AS2",
        "MERCURE-LIFETIME-JKEGDRGHDR56UIGDGROP4DWHDASGFARDHDFGDWGGAFQWERFDHDRG78WAHRGHFTYDFGDRDRAG9H1AS2",
        "MERCURE-LIFETIME-JSDFAFDWK56UIODDSAWADWAWDFP4FFFAWGGAFQWER78WATYDFGRAG9H1AS2",
        "MERCURE-LIFETIME-MERCUREONTOPLMAOMERCUREISBETTERJK56UIOP4FAWGGAFQWER78WATYDFGRAG9H1AS2",
        "MERCURE-LIFETIME-JK56UIOP4FAWGGAFQWERDAWDADWA7DAWDAWDIDKWHATTOPUTTHERELMAODWADWADADWADAWD8WATYDFGRAG9H1AS2",
    ]
    return license_key in lifetime_keys

def validate_7day_key(license_key):
    seven_days_keys = [
        "MERCURE-7DAYS-ASDWAD12ZDWACABNAWDGA5WADAWWER67TYUI89",
        "MERCURE-7DAYS-UI89ASDF0GHJ1QWEWAFDAWFGDSWADFRTY2ASXCV3B",
        "MERCURE-7DAYS-5LKJIU67YTRWADAWDADWAFVB89EDCQW01AS2Z",
        "MERCURE-7DAYS-3NMPO5LKJIUFWADAWHGFHGF67YTRFVB89EDCQW0",
        "MERCURE-7DAYS-34RETY78UIBH2NM1ZAQ6SX5CDVF",
    ]
    return license_key in seven_days_keys

def validate_1month_key(license_key):
    one_month_keys = [
        "MERCURE-1MONTH-9ASDF0DWADSFDGSGHJ1QWFSEFHGERTYFXXHGRSE2ASXCV3BN4",
        "MERCURE-1MONTH-8NBVC6EGZXASQ2WEFESFSD5RFV3TGBYH1",
        "MERCURE-1MONTH-23NMEESGSGPO5LKJIU67SGESFGYTRFVB89EDCQ",
        "MERCURE-1MONTH-78UIBH2GESGNM1ZGSAQ6SX5CDVF9FG8N",
        "MERCURE-1MONTH-56UIOP4QWWADAWFER78TDSEFGYDFG9H1AS2Z3",
    ]
    return license_key in one_month_keys

def validate_license_key(license_key):
    global plan
    if validate_lifetime_key(license_key):
        plan = "Lifetime"
        return True
    elif validate_7day_key(license_key):
        plan = "7-Day"
        license_key_issue_date[license_key] = datetime.now()
        return True
    elif validate_1month_key(license_key):
        plan = "1-Month"
        license_key_issue_date[license_key] = datetime.now()
        return True
    else:
        return False

def is_7day_key_expired(license_key):
    return datetime.now() > license_key_issue_date.get(license_key, datetime.now()) + timedelta(days=7)

def is_1month_key_expired(license_key):
    return datetime.now() > license_key_issue_date.get(license_key, datetime.now()) + timedelta(days=30)

def get_user_plan(username):
    users = load_users_from_file()
    license_key = users[username]['license_key']
    if validate_lifetime_key(license_key):
        return "Lifetime"
    elif validate_7day_key(license_key):
        if is_7day_key_expired(license_key):
            return "Expired 7-Day"
        else:
            return "7-Day"
    elif validate_1month_key(license_key):
        if is_1month_key_expired(license_key):
            return "Expired 1-Month"
        else:
            return "1-Month"
    return "Unknown"

def login_or_register():
    global plan
    users = load_users_from_file()
    if 'logged_in_user' in users:
        username = users['logged_in_user']
        plan = get_user_plan(username)
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW(f'''Mercure •  [3.1.3] | User: [{username}]''')
        loged = (f"""                                 
                                                {RED}Welcome To :{c}       
                                \033[31m _____ _____ _____ _____ _____ _____ _____ 
                                |     |   __| __  |     |  |  | __  |   __|
                                | | | |   __|    -|   --|  |  |    -|   __|
                                \033[90m|_|_|_|_____|__|__|_____|_____|__|__|_____|
                                                                                                 
                          {dark_red_color}WELCOME BACK {username}!               
                          Thanks for buying Mercure.gg{dark_red_color} {grey_color}[{grey_color}{dark_red_color}{plan}{dark_red_color}{grey_color}]{grey_color} {dark_red_color}Plan
        """)
        print(f"{loged}{RESET}") 
        time.sleep(2)
        return
        os.system('cls')
        os.system('mode con: cols=136 lines=26')
    ctypes.windll.kernel32.SetConsoleTitleW(f'''Mercure Premium | LOG IN / REGISTER ''')
    self = f"""                                 

                         \033[31m _____ _____ _____ _____ _____ _____ _____ 
                         |     |   __| __  |     |  |  | __  |   __|
                         | | | |   __|    -|   --|  |  |    -|   __|
                         \033[90m|_|_|_|_____|__|__|_____|_____|__|__|_____|                                          
"""
    print(f"{self}{RESET}")   
    
    license_key_valid = False
    while not license_key_valid:
        license_key = input(f'''{dark_red_color}                        {timestamp} {c}[{c}{r}?{r}{c}]{c} [LICENSE] {g}[INPUT HIDDEN]{g} > {s}''')
        if validate_license_key(license_key):
            license_key_valid = True
            choice = input(f"                        {timestamp} {c}[{c}{r}?{r}{c}]{c} {c}[LOGIN/REGISTER] > {c}").lower()
            if choice == 'login':
                login(users, license_key)
            elif choice == 'register':
                register(users, license_key)
            else:
                print(f"                        {c}[+] INVALID CHOICE, ONLY CHOOSE FROM 'LOGIN / REGISTER.")
                login_or_register()
        else:
            print(f"                        {c}[+] LICENSE KEY IS INVALID OR EXPIRED. ACCESS DENIED.")
            reset()

def login(users, license_key):
    global plan
    name = input(f"                        {timestamp} {c}[{c}{r}?{r}{c}]{c} [USERNAME] > {c}")
    password = input(f"                        {timestamp} {c}[{c}{r}?{r}{c}]{c} {grey_color}[{grey_color}{dark_red_color}PASSWORD{dark_red_color}{grey_color}]{grey_color} > {c}")

    if name in users and users[name]['password'] == password:
        print("Login successful!")
        users['logged_in_user'] = name
        save_users_to_file(users)
        plan = get_user_plan(name)
    else:
        print(f"                        {c}Incorrect username or password. Please try again.")
        login_or_register()

def register(users, license_key):
    global plan
    username = input(f"                        {timestamp} {c}[{c}{r}?{r}{c}]{c} [NEW USERNAME] > ")

    if username in users:
        print("Username already exists. Please choose another one.")
        register(users, license_key)
    else:
        password = input(f"                        {timestamp} {c}[{c}{r}?{r}{c}]{c} [NEW PASSWORD] > ")
        users[username] = {'password': password, 'license_key': license_key}
        save_users_to_file(users)
        print("Registration successful!")
        users['logged_in_user'] = username
        save_users_to_file(users)
        plan = get_user_plan(username)
