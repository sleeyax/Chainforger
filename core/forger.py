import requests, re, json, time
requests.packages.urllib3.disable_warnings()

class Forger():
	def __init__(self,):
		self.pcount = 0

	def banner(self):
		print ("""\033[1;33m

      _           _        __
     | |         (_)      / _|
  ___| |__   __ _ _ _ __ | |_ ___  _ __ __ _  ___ _ __
 / __| '_ \ / _` | | '_ \|  _/ _ \| '__/ _` |/ _ \ '__|
| (__| | | | (_| | | | | | || (_) | | | (_| |  __/ |
 \___|_| |_|\__,_|_|_| |_|_| \___/|_|  \__, |\___|_|
                                        __/ |
                                       |___/

---------------------------------------------------
V 1.2
---------------------------------------------------\033[0m
\033[1;37m
use >> file.txt to redirect output to a file.
Example: python chainforger.py >> output.txt

type --help for more options\033[0m
\033[1;33m
---------------------------------------------------\033[0m
\033[1;37m
Format: type  host  port [user pass]\033[0m
""")

	def start(self, filter):
		self.banner()
		if filter != None:
			try:
				splitted = filter.split(',')
				for split in splitted:
					getattr(self, split)()
				pass
			except Exception as e:
				print("# Error: " + str(e))
				pass
		else:
			self.http()
			self.https()
			self.socks()
			self.all()

		print("# Amount of proxies: " + str(self.pcount))

	def socks(self):
		r = requests.get("https://www.socks-proxy.net/", verify=False, allow_redirects=False)
		html = r.text
		matches = re.findall(r"(\d+?\.\d+?\.\d+?\.\d+).*?(\d{1,5}).*?(Socks\d)", html)
		for match in matches:
			print(match[2].lower() + "	" + match[0] + "	" + match[1])
			self.pcount += 1

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
					self.pcount += 1
			except Exception as e:
				print("# Error: " + str(e))
				pass

	def http(self):
		r = requests.get("https://free-proxy-list.net/", verify=False, allow_redirects=False)
		html = r.text
		matches = re.findall(r"(\d+?\.\d+?\.\d+?\.\d+).*?(\d{1,5}).*?(no)", html)
		for match in matches:
			print("http" + "	" + match[0] + "	" + match[1])
			self.pcount += 1

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
					self.pcount += 1
			except Exception as e:
				print("# Error: " + str(e))
				pass

	def all(self):
		for i in range(0, 500, 20): # 7220 max
			try:
				r = requests.get("http://proxydb.net/?protocol=http&protocol=https&protocol=socks4&protocol=socks5&offset=" + str(i))

				html = r.text
				matches = re.findall(r"var x = '(\d{1,4}\.\d{1,4}\.\d{1,4})'.*?var y = '(.+?)'.*?var p = (-*\d+).*?(-*\d+).*?#(.+?)\"", html, re.DOTALL)
				for match in matches:
					x = match[0][::-1]
					y = match[1]
					z = int(match[2])
					p = z + int(match[3])

					ip = x + y
					port = p
					protocol = match[4]
					print(protocol + "	" + ip + "	" + str(port))
					self.pcount += 1
				time.sleep(3)

			except Exception as e:
				print("# Error: " + str(e))
			pass

	def https(self):
		try:
			r = requests.get("https://www.sslproxies.org/", verify=False, allow_redirects=False)
			html = r.text
			matches = re.findall(r"(\d+?\.\d+?\.\d+?\.\d+).*?(\d{1,5}).*?(no)", html)
			for match in matches:
				print("https" + "	" + match[0] + "	" + match[1])
				self.pcount += 1
			pass
		except Exception as e:
			print("# Error: " + str(e))
			pass