import re, requests, sys
from .gui import *
class Checker:
	def __init__(self, timeout = 10, exportFileName = None):
		self.timeout = timeout
		self.exportFileName = exportFileName

	def showStatus(self):
		if self.timeout != None:
			showInfo("Proxy timeout: " + str(self.timeout) + "s")

		if self.exportFileName != None:
			showInfo("Exporting to: " + self.exportFileName)
		else:
			showWarning("No output file selected. Use '--export' or ignore this message")
		
		print()

	def checkProxyList(self, fileToCheck):
		showBanner()
		showInfo("Checking your proxies...")
		self.showStatus()

		file = open(fileToCheck, "r")
		for line in file:
			if re.match(r"http[s]*|socks\d", line):
				data = self.parseArray(line.rstrip())
				self.checkProxy(data["protocol"], data["ip"], data["port"])

	def parseArray(self, line):
		match = re.match(r"(.+?)	(\d{1,4}\.\d{1,4}\.\d{1,4}\.\d{1,4})	(\d+)", line)

		if match == False:
			print("Error: Proxylist does not match proxychains format!")
			sys.exit(1)
		
		return {
			"protocol": match.group(1),
			"ip": match.group(2),
			"port": match.group(3)
        }

	def checkProxy(self, protocol, ip, port):
		
		if protocol == "http":
			proxy = {"http": "http://" + ip}

		if protocol == "https":
			proxy = {"https" : "http://" + ip}

		if protocol == "socks4":
			proxy = {"https" : "socks4://" + ip, "http" : "socks4://" + ip}

		if protocol == "socks5":
			proxy = {"https" : "socks5://" + ip, "http" : "socks5://" + ip}


		try:
			r = requests.get("https://api.ipify.org/", proxies=proxy, timeout=self.timeout)
			
			if r.status_code == 200:
				print(getGreen("[OK]:"), protocol, ip, port)
				
				if self.exportFileName != None:
					self.writeToFile(self.exportFileName, protocol + "	" + ip + "	" + port)
				
				return True
			else:
				print(getRed("[ERROR]:"), protocol, ip, port + "[Dead proxy]")
				return False
		except Exception as e:
			print(getRed("[ERROR]:"), protocol, ip, port + "[Can't connect]")
			return False
		except KeyboardInterrupt:
			showWarning("Stopping application...")
			sys.exit(0)
		
	def writeToFile(self, filename, text):
		file = open(filename, "a")
		file.write(text + "\n")
		file.close()
