import requests, re, json, time
from .checker import Checker
from .gui import *
requests.packages.urllib3.disable_warnings()

class Forger:
	def __init__(self, timeout = 10, _filter = None, export = None):
		self.proxyCount = 0
		self.filter = _filter
		self.fileName = export
		self.timeout = timeout
		self.otf = True

	def disableOtf(self):
		self.otf = False

	def start(self):
		showBanner()
		showInfo("ChainForger is forging proxies...")
		self.showStatus()
		try:
			if self.filter != None:
				try:
					splitted = self.filter.split(',')
					for split in splitted:
						getattr(self, split)()
				except Exception as e:
					showError("Error: " + str(e) + " (Maybe you specified an invalid filter? See '--help' for more info)")
			else:
				self.http()
				self.https()
				self.socks()
				self.all()
		except KeyboardInterrupt:
			showWarning("Stopping application...")

		showInfo("Total amount of proxies scraped: " + str(self.proxyCount))

	def showStatus(self):
		if self.filter != None:
			showInfo("Applied filter: " + self.filter)
		if self.fileName != None:
			showInfo("Exporting proxies to: " + self.fileName)
		else:
			showWarning("No export file selected. Use '--export' or ignore this message")
		if self.timeout != None:
			showInfo("Proxy timeout: " + str(self.timeout) + "s")
		else:
			showWarning("No proxy timeout set. Defaulting to 10s, use '--timeout' or ignore this message")
		if self.otf:
			showInfo("On-the-fly proxy checking is enabled")
		else:
			showInfo("On-the-fly proxy checking is disabled")
		
		print()

	def writeToFile(self, filename, text):
		file = open(filename, "a")
		file.write(text + "\n")
		file.close()

	def printProxy(self, protocol, ip, port):
		proxy = protocol + "	" + ip + "	" + port
		
		checker = Checker(self.timeout)

		if self.otf == True:
			if checker.checkProxy(protocol, ip, port) == False:
				return
		else:
			print(proxy)
		
		if self.fileName != None:
			self.writeToFile(self.fileName, proxy)
			

	def socks(self):
		r = requests.get("https://www.socks-proxy.net/", verify=False, allow_redirects=False)
		html = r.text
		matches = re.findall(r"(\d+?\.\d+?\.\d+?\.\d+).*?(\d{1,5}).*?(Socks\d)", html)
		for match in matches:
			self.printProxy(match[2].lower(), match[0], match[1])
			self.proxyCount += 1

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
					self.printProxy(json_array["type"].lower(), json_array["IP"], str(json_array["PORT"]))
					self.proxyCount += 1
			except Exception as e:
				print("# Error: " + str(e))
				pass

	def http(self):
		r = requests.get("https://free-proxy-list.net/", verify=False, allow_redirects=False)
		html = r.text
		matches = re.findall(r"(\d+?\.\d+?\.\d+?\.\d+).*?(\d{1,5}).*?(no)", html)
		for match in matches:
			self.printProxy("http", match[0], match[1])
			self.proxyCount += 1

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
					self.printProxy(json_array["type"].lower(), json_array["IP"], str(json_array["PORT"]))
					self.proxyCount += 1
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
					self.printProxy(protocol, ip, str(port))
					self.proxyCount += 1
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
				self.printProxy("https", match[0], match[1])
				self.proxyCount += 1
			pass
		except Exception as e:
			print("# Error: " + str(e))
			pass
