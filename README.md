# Chainforger
A proxy scraper for proxychains

# Features
- [x] Scrape http, https, socks4 and socks5
- [x] Check proxies on-the-fly or from a file
- [x] Currently 1000+ proxies scrapable!

# Requirements
- Python 3.4+
- Requests module

# Installation
install requests module
```
pip install requests
```
(optional) when scraping socks, install requests socks extension:
```
pip install requests[socks]
```
run chainforger
```
python chainforger.py --help
```

# Screenshots
<img src='https://i.imgur.com/6qsANQi.png'/><br>

<img src='https://i.imgur.com/NhStkA4.png' /><br />

<img src='https://i.imgur.com/yfiZJu3.png' /><br />

# Changelog
- Version 1.0
    - First release
- Version 1.1
    - HTTPS support
    - Fancy colors
    - More scraping websites
    - Add '#' before error lines
- Version 1.2
    - Filter HTTPS
    - Built-in proxychecker (consider this in alpha)
    - Better project structure & general clean up
- Version 2.0
    - Code cleanup
    - Export proxies the right way
    - Custom export filename & proxy timeout
    - Check proxy immediately after scraping
    - Better GUI
- Version 2.1
    - Shorter arguments
    - Turn off on-the-fly proxy checking with '--no-otf' flag
    - Check if file exists when using '--check'
    - Don't check proxies with specified protocol by using '--filter' with '--check'

# TODO
- Export proxies (automatically) to proxychains config
- Add more scrapable resources