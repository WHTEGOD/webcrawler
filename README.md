# Universal Web Crawler

## Overview
The Universal Web Crawler is a Python-based web scraping tool developed using the Scrapy framework. This crawler is designed to traverse web pages, extract specific data, and store it for further analysis or use. It is highly configurable, allowing users to specify the start URLs and the domains to crawl.

## Features
- Crawls through specified URLs and follows links to scrape data.
- Extracts page information such as URL, title, and body content.
- Outputs scraped data in JSON or CSV format.
- Configurable start URLs and allowed domains.

## Technologies Used
- Programming Language: Python
- Framework: Scrapy
- Libraries/Modules: Scrapy

## Getting Started

### Prerequisites
- Python 3.x
- Scrapy (Install via pip)

```bash
pip install Scrapy
```

### Clone the Repository
```bash
git clone https://github.com/WHTEGOD/universal-web-crawler.git
cd universal-web-crawler
```

### Running the Spider
To run the spider, use the following command:

```bash
scrapy crawl universal_spider -a start_urls="http://example.com" -a allowed_domains="example.com" -o output.json
```
- Replace `http://example.com` with your target URL.
- The data will be saved in `output.json`.
- In the Code if You don't enter the Target URL then there is already selected Target Domain [toscrape.com] and URL [http://books.toscrape.com/]

### Customization
You can modify the `UniversalSpider` class in `universal_spider.py` to change the data you want to scrape or the logic of the spider.

## Code Explanation
The main components of the spider are:

- Spider Class: Inherits from `CrawlSpider` and defines crawling behavior.
- Rules: Specify how to follow links and which items to parse.
- Parse Item Method: Extracts data from the pages and yields it.

## Example Output
The crawler will yield output in JSON format similar to the following:

```json
[
    {"title": "Ollo", "price": "£12.84", "stock": ""},
    {"title": "Libertarianism for Beginners", "price": "£51.33", "stock": ""},
    {"title": "It's Only the Himalayas", "price": "£45.17", "stock": ""},
]

```

## Future Enhancements
- Implement error handling for failed requests.
- Add support for crawling JavaScript-heavy websites.
- Enable parallel or distributed crawling.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [Scrapy Documentation](https://docs.scrapy.org)
- [Python Official Documentation](https://docs.python.org)

```

