import requests
import tls_client
import threading

r = requests.get("https://discord.com/api/v9/users/@me")

def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text
xsup = "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVzIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNi4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTYuMC4xOTM4LjY5IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTE2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjIyNTg3MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
session = tls_client.Session(
    client_identifier="chrome_116",
)
chrome_version = "116"


def create_group(token, groupname, output_lock):
            headers = {
                'authorization': token,
                "accept": "*/*",
                "accept-language": "en-GB",
                "content-type": "application/json",
                "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                "origin": "https://discord.com",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/537.36",
                "x-debug-options": "bugReporterEnabled",
                "x-super-properties": xsup
            }
            try:
                response_recipients = session.post('https://discord.com/api/v9/users/@me/channels', headers=headers, json={
                     "recipients": []
                })
                newjson = json.loads(response_recipients.content)
                id = newjson['id']
                time.sleep(0.2)
                payload = {
                    'name': groupname
                }
                response = session.patch(f'https://discord.com/api/v9/channels/{id}', headers=headers, json=payload)
                if response.status_code == 200:
                    with output_lock:
                        print(f"                          {white}({green}+{white}) {green} CREATED {white} | ", end='')
                        sys.stdout.flush()
                        Write.Print(groupname + "\n", Colors.purple_to_red, interval=0.000)
            except:
                with output_lock:
                    print(f"                          {white}({yellow}x{white}) {yellow} RATE LIMITED {white} | ", end='')
                    sys.stdout.flush()
                    Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)

def gcspammer():
            self = f"""                                 


                                   ██████╗ ██╗   ██╗ ██████╗ ██████╗ ██╗██╗  ██╗ {L}{L1}[?] Group Spammer {L}
                                  ██╔═══██╗██║   ██║██╔═══██╗██╔══██╗██║╚██╗██╔╝ {L}{L1}[?] {lol} Token(s) Loaded{L}
                                  ██║   ██║██║   ██║██║   ██║██████╔╝██║ ╚███╔╝ 
                                  ██║▄▄ ██║██║   ██║██║   ██║██╔══██╗██║ ██╔██╗ 
                                  ╚██████╔╝╚██████╔╝╚██████╔╝██║  ██║██║██╔╝ ██╗
                                   ╚══▀▀═╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝                                                                                                                                        
        """
            print(f"{Center.XCenter(vgratient(self, [178, 114, 242], [178, 114, 242]))}{RESET}") 

            token = input(f"                                        {white}({green}+{white}) {L1} Enter Token > {Fore.LIGHTBLACK_EX}[HIDDEN INPUT]{RESET}{Fore.BLACK} ")
            groupname = input(f"                                        {white}({green}+{white}) {L1} Group Name > ")
            howmany = input(f"                                        {white}({green}+{white}) {L1} Ammount > ")
            
            output_lock = threading.Lock()
            threads = []
            print()

            for i in range(int(howmany)):
                thread = threading.Thread(target=create_group, args=(token, groupname, output_lock))
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()