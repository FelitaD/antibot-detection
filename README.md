# Test technique NetVeille

## Content
### Architecture
It is a [Scrapy crawler](https://docs.scrapy.org/en/latest/index.html) using [Splash](https://github.com/scrapy-plugins/scrapy-splash) to render javascript.
### Description
The target website has several anti-bot detection techniques for which the crawler will implement a solution:

| Antibot technique       | Solution                          | Technology implemented   |
|-------------------------|-----------------------------------|--------------------------|
| Browser Fingerprinting  | Headless Browser                  | Splash                   |
| IP-rate limiting        | Rotating proxies                  | Zyte Smart Proxy Manager |
| Banning Data center IPs | Residential IPs                   |                          |
| TLS Fingerprinting      | Forge and rotate TLS fingerprints |                          |

## Implementation

### 0. Prerequesites

- Install python 3
- Install Docker to run Splash server
- Run virtual environment

    
    pip3 install virtualenv
    virtualenv venv
    source venv/bin/activate

- Install requirements

    
    pip3 install -r requirements.txt

### 1. Headless browsing and JS rendering with Splash

    pip3 install scrapy-splash
    docker run -p 8050:8050 scrapinghub/splash

### 2. 
