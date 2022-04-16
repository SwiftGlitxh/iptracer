import ipinfo,time
import subprocess,sys
import pkg_resources
try:
  subprocess.call(['clear'])
except:
  subprocess.call(['cls'],shell=True)
required = {'ipinfo'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed
print('[!] Checking modules...\n')
for x in required:
	if not missing:
		print("[+]",*required,sep="\n")
	if missing:
		print("\033[1;31m[!]\033[0;37m",*required,sep="\n")

if missing:
	install = input('\n[?] Would you like to install the missing packages?: ')
	if install == "y":
		python = sys.executable
		subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
	elif install == "n":
		exit()
print('''
  \033[31m _\033[37m       _                           
  \033[31m(_)\033[37m_ __ | |_ _ __ __ _  ___ ___ _ __ 
  | | '_ \| __| '__/ _` |/ __/ _ \ '__|
  | | |_) | |_| | | (_| | (_|  __/ |   
  |_| .__/ \__|_|  \__,_|\___\___|_|   
    |_|                             
=======================================\n  ''')

plus = "\033[1;32m[+]\033[0;37m"
access_token = 'fa105f98af196e'
handler = ipinfo.getHandler(access_token)
ip_address = input(">> Enter a IP to track: ")

try:
	details = handler.getDetails(ip_address)
except AttributeError:
	print("[!] IP was not availble")

banner = "\n[!] Gathering Information"
x = len(banner)
print(banner)
print("="*x)
while True:
	try:
		print(f"\n{plus} IP Addr: {details.ip}")
		time.sleep(0.8)
		print(f"{plus} Country: {details.country}")
		time.sleep(0.8)
		print(f"{plus} City: {details.city}")
		time.sleep(0.8)
		print(f"{plus} Longitude: {details.loc}")
		time.sleep(0.8)
		print(f"{plus} Postal Code: {details.postal}")
		time.sleep(0.8)
		print(f"{plus} Region: {details.region}")
		time.sleep(0.8)
		print(f"{plus} Timezone: {details.timezone}")
		print('\n\033[1;37m[!]\033[0;37m Scan complete')
		break
	except AttributeError:
		print("\033[1;31m[!] ERROR tracing IP\033[0;37m")
		break
