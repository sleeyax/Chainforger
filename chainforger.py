import argparse
from core.forger import Forger
from core.checker import Checker

parser = argparse.ArgumentParser(description="Chainforger v1.2")
parser.add_argument("-f", nargs='?', metavar="<socks,http,https>", help="Filter for socks, http or https (seperated by comma)")
parser.add_argument("--check", nargs='?', metavar="<proxies.txt>", help="Check proxies (use -t to set timeout)")
parser.add_argument("-t", nargs='?', metavar="<timeout>", help="Set timeout for proxychecker")
args = parser.parse_args()

if args.f != None:
	forger = Forger()
	forger.start(args.f)
	
if args.check != None:
	checker = Checker()
	if args.t != None:
		checker.check(args.check, args.t)
	else:
		checker.check(args.check, None)

if args.check == None and args.f == None:
	forger = Forger()
	forger.start(None)
