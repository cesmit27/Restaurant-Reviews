import sys
sys.path.append(r'D:/WebScraper')

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from WebScraper.spiders.restaurant_data_spider import RestaurantDataSpider

process = CrawlerProcess(get_project_settings())
process.crawl(RestaurantDataSpider)
process.start()
