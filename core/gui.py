def showBanner():
	print(getBrightCyan("""

      _           _        __
     | |         (_)      / _|
  ___| |__   __ _ _ _ __ | |_ ___  _ __ __ _  ___ _ __
 / __| '_ \ / _` | | '_ \|  _/ _ \| '__/ _` |/ _ \ '__|
| (__| | | | (_| | | | | | || (_) | | | (_| |  __/ |
 \___|_| |_|\__,_|_|_| |_|_| \___/|_|  \__, |\___|_|
                                        __/ |
                                       |___/

---------------------------------------------------
V 2.0  ChainForger ~ proxy scraper for proxychains
---------------------------------------------------
"""))

def getWhite(text):
    return "\033[1;37m" + text + "\033[0m"

def getYellow(text):
    return "\033[1;33m" + text + "\033[0m"

def getBrightCyan(text):
    return "\033[1;36;40m" + text + "\033[0m"

def getBlue(text):
    return "\033[1;34m" + text + "\033[0m"

def getRed(text):
    return "\033[1;31m" + text + "\033[0m"

def getGreen(text):
    return "\033[1;32;40m" + text + "\033[0m"

def showInfo(text):
    print(getBlue("[#]"), text)

def showWarning(text):
    print(getYellow("[!]"), text)

def showSuccess(text):
    print(getGreen("[+]"), text)

def showError(text):
    print(getRed("[-]"), text)
