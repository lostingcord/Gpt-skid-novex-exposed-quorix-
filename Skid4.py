from assets import * # THIS IS NOT MY CODE NOVEX ALLOWED ME TO USE IT, I JUST REALISED ITS GPT LOL

r = '\033[90m'
lc = Fore.RESET
c = Fore.LIGHTGREEN_EX
g = Fore.LIGHTBLACK_EX
s = Fore.BLACK
x = Fore.GREEN
k = Fore.YELLOW

banner = f"""
                 
                                  _____ _   _                   _ 
                                 |   __| |_| |_ ___ ___ ___ ___| |
                                 |   __|  _|   | -_|  _| -_| .'| |
                                 |_____|_| |_|_|___|_| |___|__,|_|   
"""

timestamp = datetime.datetime.now().strftime(f'{c}[{c}{lc}%H:%M:%S{lc}{c}]{c}')

async def send_message(token, channel_id, message_content):
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    payload = {
        "content": message_content
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200 or response.status_code == 201:
            message_id = response.json()['id']
            print(f"{c}{c}[{c}{r}#{r}{c}]{c}{x} Message Sent Successfully")
            return message_id
        else:
            print(f"{c}{c}[{c}{r}#{r}{c}]{c}{c} Failed Sending Message")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error occurred with token ending in {token[-4:]}: {e}")
        return None

async def pin_message(token, channel_id, message_id):
    url = f"https://discord.com/api/v9/channels/{channel_id}/pins/{message_id}"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }

    try:
        response = requests.put(url, headers=headers)
        if response.status_code == 204:
            print(f"{c}{c}[{c}{r}#{r}{c}]{c}{x} Message Pinned")
        else:
            print(f"{c}{c}[{c}{r}#{r}{c}]{c}{c} Pin Failed")
    except requests.exceptions.RequestException as e:
        print(f"{c}{c}[{c}{r}#{r}{c}]{c}{c} Error")

async def send_and_pin_message(token, channel_id, message_content):
    message_id = await send_message(token, channel_id, message_content)
    if message_id:
        await pin_message(token, channel_id, message_id)

async def message_spammer():
    with open("assets/stats/tokens.txt", "r") as file:
        tokens = [line.strip() for line in file]

    os.system('cls'); print(Colorate.Horizontal(Colors.green_to_cyan, banner))
    channel_id = input(f"{datetime.datetime.now().strftime(f'{c}[{c}{lc}{c}{lc}%H:%M:%S{lc}{c}{lc}{c}]{c}')}{r} {c}[{c}{lc}Channel ID{lc}{c}]{c} {c}~/> {lc}")
    base_message_content = input(f"{datetime.datetime.now().strftime(f'{c}[{c}{lc}{c}{lc}%H:%M:%S{lc}{c}{lc}{c}]{c}')}{r} {c}[{c}{lc}Message{lc}{c}]{c} {c}~/> {lc}")
    os.system('cls'); print(Colorate.Horizontal(Colors.green_to_cyan, banner))

    with ThreadPoolExecutor(max_workers=10) as executor:
        while True:
            futures = []
            for token in tokens:
                message_content = f"{base_message_content} - {random.randint(1000, 9999)}"
                futures.append(executor.submit(asyncio.run, send_and_pin_message(token, channel_id, message_content)))
            for future in futures:
                await asyncio.sleep(0.5)
