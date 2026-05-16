import requests
from pystyle import Colorate, Colors, Center
from colorama import Fore
import time

def main():
    banner = """

██████╗ ███████╗███╗   ███╗ ██████╗ ███╗   ██╗███████╗
██╔══██╗██╔════╝████╗ ████║██╔═══██╗████╗  ██║╚══███╔╝
██║  ██║█████╗  ██╔████╔██║██║   ██║██╔██╗ ██║  ███╔╝
██║  ██║██╔══╝  ██║╚██╔╝██║██║   ██║██║╚██╗██║ ███╔╝
██████╔╝███████╗██║ ╚═╝ ██║╚██████╔╝██║ ╚████║███████╗
╚═════╝ ╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝

              { [+] Creator Qhul }

    """

    print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(banner)))

    target = input(f"{Fore.RED}[+] Enter Target Site URL: ")
    amount = int(input(f"{Fore.MAGENTA}[+] Enter Amount Of Requests: "))

    for _ in range(amount):

        start = time.time()

        response = requests.get(url=target)

        end = time.time()

        ms = (end - start) * 1000

        if response.status_code == 200:
            print(f"{Fore.BLUE}[+] Request Sent | {ms:.2f} ms")

        elif response.status_code == 404 or response.status_code == 429:
            print(f"{Fore.RED}[-] Request Failed")

        else:
            print(f"{Fore.YELLOW}[!] Status Code: {response.status_code}")

    print(f"{Fore.GREEN}[+] Finished.")

main()
