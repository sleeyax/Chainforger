# Chainforger
A proxy scraper for proxychains
<img src='https://i.imgur.com/jkedgCy.png'/>

# Features
- [x] Scrape http, https, socks4 and socks5
- [x] Built-in proxy checker (alpha)
- [x] Currently 1000+ proxies scrapable!
- [x] Apply filter for http, https or socks

# Requirements
- Python 3.4 or above
- The requests module
# Installation
install requests module
```
pip install requests
```
install built-in proxy checker requirements
```
pip install requests[socks]
```
run chainforger
```
python chainforger.py --help
```

# Screenshots
<img src='https://i.imgur.com/Obv8Eci.png' /><br />
<img src='https://i.imgur.com/3KYeG4n.png' /><br />

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
