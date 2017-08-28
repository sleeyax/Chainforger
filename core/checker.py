import re, requests
class Checker():

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
V 1.2	Proxychains proxy checker [alpha]
---------------------------------------------------\033[0m
\033[1;37m
Chainforger will now check your proxies...
\033[0m
""")
	def __init__(self):
		self.timeout = 10

	def check(self, file, timeout):
		self.banner()

		if timeout != None:
			print("Dead proxy timeout: " + timeout + " seconds")
			self.timeout = int(timeout)

		file = open(file, "r")
		for line in file:
			if re.match(r"http[s]*|socks\d", line):
				self.format(line.rstrip())

	def format(self, line):
		match = re.match(r"(.+?)	(\d{1,4}\.\d{1,4}\.\d{1,4}\.\d{1,4})	(\d+)", line)
		if match:
			self.check_response(match.group(1), match.group(2), match.group(3))

	def check_response(self, protocol, ip, port):
		try:
			if protocol == "http":
				proxy = {"http" : "http://" + ip}
				r = requests.get("https://api.ipify.org/", proxies=proxy, timeout=self.timeout)

			if protocol == "https":
				proxy = {"https" : "http://" + ip}
				r = requests.get("https://api.ipify.org/", proxies=proxy, timeout=self.timeout)

			if protocol == "socks4":
				proxy = {"https" : "socks4://" + ip, "http" : "socks4://" + ip}
				r = requests.get("https://api.ipify.org/", proxies=proxy, timeout=self.timeout)

			if protocol == "socks5":
				proxy = {"https" : "socks5://" + ip, "http" : "socks5://" + ip}
				r = requests.get("https://api.ipify.org/", proxies=proxy, timeout=self.timeout)

			if r.status_code == 200:
				print("[OK]: " + protocol, ip, port)
				self.fwrite(protocol + "	" + ip + "	" + port)
			else:
				print("[ERROR]: " + protocol, ip, port + "[Dead proxy]")
			pass
		except Exception as e:
			print("[ERROR]" + protocol, ip, port + "[Can't connect]")
			pass
		
	def fwrite(self, line):
		file = open("exported_proxies.txt", "w") # TODO: add date or custom name
		file.write(line)
		file.close()