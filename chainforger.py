import argparse
from core.forger import Forger
from core.checker import Checker

example = """
Examples:
	python3 chainforger.py --filter http,socks --export exported.txt --timeout 5
	python3 chainforger.py --check exported.txt --export exported_checked.txt
	python3 chainforger.py --check exported.txt --filter socks4,socks5 --export checked_proxies_without_socks4-5.txt
"""
parser = argparse.ArgumentParser(description="Chainforger v2.1", epilog=example, formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("--filter", "-f", nargs='?', metavar="<socks,http,https>", help="Protocol filter (seperated by comma)")
parser.add_argument("--check", "-c", nargs='?', metavar="<proxies.txt>", help="File to check proxies from")
parser.add_argument("--export", "-e", nargs='?', metavar="<exported.txt>", help="Export proxies to file")
parser.add_argument("--timeout", "-t", nargs='?', metavar="<timeout>", help="Proxy timeout", const=10, type=int)
parser.add_argument("--no-otf", help="Disable on-the-fly proxy checking", const=True, action="store_const")
args = parser.parse_args()

if args.check != None:
	checker = Checker(args.timeout, args.export)
	if args.filter != None:
		checker.setFilter(args.filter)
	checker.checkProxyList(args.check)

if args.check == None:
	forger = Forger(args.timeout, args.filter, args.export)
	if args.no_otf != None:
		forger.disableOtf()
	forger.start()
