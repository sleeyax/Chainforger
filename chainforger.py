import argparse
from core.forger import Forger
from core.checker import Checker

example = """
Examples:
	python3 chainforger.py --filter http,socks --export exported.txt --timeout 5
	python3 chainforger.py --check exported.txt --export exported_checked.txt
"""
parser = argparse.ArgumentParser(description="Chainforger v2.0", epilog=example, formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("--filter", nargs='?', metavar="<socks,http,https>", help="Protocol filter (seperated by comma)")
parser.add_argument("--check", nargs='?', metavar="<proxies.txt>", help="File to check proxies from")
parser.add_argument("--export", nargs='?', metavar="<exported.txt>", help="Export proxies to file")
parser.add_argument("--timeout", nargs='?', metavar="<timeout>", help="Proxy timeout", const=10, type=int)
args = parser.parse_args()

if args.check != None and args.filter == None:
	checker = Checker(args.timeout, args.export)
	checker.checkProxyList(args.check)

if args.check == None:
	forger = Forger(args.timeout, args.filter, args.export)
	forger.start()
