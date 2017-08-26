import requests
import re
import argparse
import json

class Forger():
	"""def __init__(self, arg):
		super(Forge, self).__init__()
		self.arg = arg"""

	def banner(self):
		print ("""

      _           _        __                          
     | |         (_)      / _|                         
  ___| |__   __ _ _ _ __ | |_ ___  _ __ __ _  ___ _ __ 
 / __| '_ \ / _` | | '_ \|  _/ _ \| '__/ _` |/ _ \ '__|
| (__| | | | (_| | | | | | || (_) | | | (_| |  __/ |   
 \___|_| |_|\__,_|_|_| |_|_| \___/|_|  \__, |\___|_|   
                                        __/ |          
                                       |___/           

---------------------------------------------------
V 1.0
---------------------------------------------------
use >> file.txt to redirect output to a file. 
Example: python chainforger.py >> output.txt

type --help for more options
---------------------------------------------------
Format: type  host  port [user pass]
""")

	def start(self, filter = None):
		if filter != None:
			try:
				getattr(self, filter)()
				pass
			except Exception as e:
				print("Error: " + str(e))
				pass
		else:
			self.socks()
			self.http()
				
	def socks(self):
		r = requests.get("https://www.socks-proxy.net/", verify=False)
		html = r.text
		matches = re.findall(r"(\d+?\.\d+?\.\d+?\.\d+).*?(\d{1,5}).*?(Socks\d)", html)
		for match in matches:
			print(match[2].lower() + "	" + match[0] + "	" + match[1])

		headers = {
		"Referer" : "https://hidester.com/proxylist/",
		"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
		"Accept" : "application/json, text/plain, */*"
		}
		for i in range(0,5):
			try:
				r = requests.get("https://hidester.com/proxydata/php/data.php?mykey=data&offset=" + str(i) + "&limit=10&orderBy=latest_check&sortOrder=DESC&country=&port=&type=12&anonymity=7&ping=7&gproxy=2", headers=headers, verify=False)
				json = r.json()
				for json_array in json:
					print(json_array["type"].lower() + "	" + json_array["IP"] + "	" + str(json_array["PORT"]))
			except Exception as e:
				print("Error: " + str(e))
				pass
	
	def http(self):
		r = requests.get("https://free-proxy-list.net/", verify=False)
		html = r.text
		matches = re.findall(r"(\d+?\.\d+?\.\d+?\.\d+).*?(\d{1,5}).*?(no)", html)
		for match in matches:
			print("http" + "	" + match[0] + "	" + match[1])

		headers = {
		"Referer" : "https://hidester.com/proxylist/",
		"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
		"Accept" : "application/json, text/plain, */*"
		}
		
		for i in range(0,5):
			try:
				r = requests.get("https://hidester.com/proxydata/php/data.php?mykey=data&offset=" + str(i) + "&limit=10&orderBy=latest_check&sortOrder=DESC&country=&port=&type=1&anonymity=7&ping=7&gproxy=2", headers=headers, verify=False)
				json = r.json()
				for json_array in json:
					print(json_array["type"].lower() + "	" + json_array["IP"] + "	" + str(json_array["PORT"]))
			except Exception as e:
				print("Error: " + str(e))
				pass

parser = argparse.ArgumentParser(description="Chainforger v1.0")
parser.add_argument("--f", nargs='?', metavar="<protocol>", help="Filter for socks or http only")
args = parser.parse_args()
requests.packages.urllib3.disable_warnings()

forger = Forger()
forger.banner()

if args.f != None:
	forger.start(args.f)
else:
	forger.start()
