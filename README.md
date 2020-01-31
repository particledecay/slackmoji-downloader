# slackmoji-downloader
Automatically download emojis for Slack.

slackmoji-downloader is a [Scrapy](https://scrapyproject.com) project for crawling a website and downloading the emojis from it. This project was born out of a need to obtain all of the emojis from [slackmojis.com](https://slackmojis.com) in order to bulk upload to Slack.

## Installation
Using Python 3:
```bash
pip install -r requirements.txt
```

## Usage
```bash
scrapy crawl slackmojis
```

## Roadmap
- Add more websites to crawl that contain Slack emojis
- Add a USER_AGENT string and potentially rate limit requests (to be a good netizen)
- Handle name conflicts when downloading files
- Bulk upload directly to Slack (oooohhhhhh!)
- Proper logging
- Tests
