import os
import sys
import time
import requests
import json
from colorama import init, Fore, Back, Style

init(autoreset=True)

class HexaAuthClient:
    def __init__(self, api_url, app_secret):
        self.api_url = api_url
        self.app_secret = app_secret
    
    def validate_license(self, license_key, hwid):
        data = {
            "app_key": self.app_secret,
            "license_key": license_key,
            "hwid": hwid
        }
        
        try:
            response = requests.post(self.api_url, json=data, timeout=10)
            return response.json()
        except Exception as e:
            return {"status": "error", "message": f"API connection error: {str(e)}"}

def get_hwid():
    import platform
    import hashlib
    
    system_info = f"{platform.node()}{platform.processor()}{platform.system()}"
    return hashlib.sha256(system_info.encode()).hexdigest()[:32]

def center_text(text):
    import shutil
    terminal_width = shutil.get_terminal_size().columns
    text_width = len(text)
    padding = (terminal_width - text_width) // 2
    return ' ' * padding + text

def print_banner():
    print(center_text("LUXISDEV"))
    print(center_text("--------------------"))

def print_loading():
    loading_chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    for i in range(20):
        print(f"\r{Fore.CYAN}Loading {loading_chars[i % len(loading_chars)]}", end="", flush=True)
        time.sleep(0.1)
    print(f"\r{Fore.GREEN}✓ Ready!{Style.RESET_ALL}")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print_banner()
    print()
    client = HexaAuthClient("https://hexaauth.alwaysdata.net/api.php", "secret_key_goes_here") # secret key goes here.
    
    print()
    
    while True:
        try:
            license_key = input(center_text(f"{Fore.CYAN}enter license key: {Style.RESET_ALL}"))
            
            if not license_key.strip():
                print(f"{Fore.RED}License key cannot be empty!{Style.RESET_ALL}")
                continue
            
            print(f"\n{center_text(f'{Fore.YELLOW}Validating license...{Style.RESET_ALL}')}")
            print_loading()
            
            hwid = get_hwid()
            
            result = client.validate_license(license_key, hwid)
            
            if result.get("status") == "success":
                print(f"\n{center_text(f'{Fore.GREEN}License validated successfully!{Style.RESET_ALL}')}")
                
                data = result.get("data", {})
                print(f"\n{center_text(f'{Fore.CYAN}HWID: {Fore.WHITE}{hwid}')}")
                
                time_left = data.get('RemainingTime', 'N/A')
                status = data.get('Status', 'N/A')
                
                if time_left != 'N/A' and isinstance(time_left, int):
                    days = time_left // 86400
                    hours = (time_left % 86400) // 3600
                    minutes = (time_left % 3600) // 60
                    seconds = time_left % 60
                    time_left = f"{days}d {hours}h {minutes}m {seconds}s"
                
                print(center_text(f"{Fore.CYAN}Time Left: {Fore.WHITE}{time_left}"))
                print(center_text(f"{Fore.CYAN}Status: {Fore.WHITE}{status}"))
                
                print(f"\n{center_text(f'{Fore.GREEN}Starting system...{Style.RESET_ALL}')}")
                time.sleep(2)
                break
                
            else:
                print(f"\n{center_text(f'{Fore.RED}License validation failed!{Style.RESET_ALL}')}")
                print(center_text(f"{Fore.RED}Error: {result.get('message', 'Unknown error')}{Style.RESET_ALL}"))
                print(center_text(f"{Fore.YELLOW}Press Enter to try again...{Style.RESET_ALL}"))
                input()
                continue
                
        except KeyboardInterrupt:
            print(f"\n{center_text(f'{Fore.YELLOW}Exiting...{Style.RESET_ALL}')}")
            sys.exit(0)
        except Exception as e:
            print(f"\n{center_text(f'{Fore.RED}Unexpected error: {str(e)}{Style.RESET_ALL}')}")
            print(center_text(f"{Fore.YELLOW}Press Enter to try again...{Style.RESET_ALL}"))
            input()
            continue
    
    print(f"\n{center_text(f'{Fore.GREEN}System ready!{Style.RESET_ALL}')}")
    print(center_text(f"{Fore.CYAN}Main system will be added here...{Style.RESET_ALL}"))

if __name__ == "__main__":
    main()
