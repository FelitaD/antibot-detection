# Test technique NetVeille

## Content
### Architecture
It is a [Scrapy crawler](https://docs.scrapy.org/en/latest/index.html).
### Description
The target website has several anti-bot detection techniques for which the crawler will implement a solution:

| Antibot technique       | Solution                          | Technology implemented   |
|-------------------------|-----------------------------------|--------------------------|
| Browser Fingerprinting  | Headless Browser                  | [Splash](https://github.com/scrapy-plugins/scrapy-splash)                   |
| IP-rate limiting        | Rotating proxies                  | [Zyte Smart Proxy Manager](https://scrapy-zyte-smartproxy.readthedocs.io/en/latest/) |
| Banning Data center IPs | Residential IPs                   | [Zyte Smart Proxy Manager](https://scrapy-zyte-smartproxy.readthedocs.io/en/latest/) |
| Requests rate           | Slow crawling speed               | [Scrapy Auto-throttling](https://docs.scrapy.org/en/latest/topics/autothrottle.html)   |
| Headers                 | Rotate User-Agents                | [Scrapy-fake-useragent](https://github.com/alecxe/scrapy-fake-useragent)                      |
| TLS Fingerprinting      | Forge and rotate TLS fingerprints |                          |
## Run the spider

### Prerequesites

- Install python 3
- Install Docker to run Splash server
- Run virtual environment

    
`pip3 install virtualenv`

`virtualenv venv`

`source venv/bin/activate`

- Install requirements

`pip3 install -r requirements.txt`

- Run Splash server in docker container.

### Start crawler

Go to directory containing the `.cfg` file

`cd clean`

Run the spider

`scrapy crawl cultura`
