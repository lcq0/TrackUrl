# from scrapy import cmdline
# cmdline.execute('scrapy crawl track_spider'.split())
from scrapy.cmdline import execute
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "track_spider"])