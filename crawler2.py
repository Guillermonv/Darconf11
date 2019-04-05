import re
from itertools import islice

from crawler import Crawler, Request

RE_TITLE = re.compile(r'<title>([^<]+)</title>', re.S | re.I)

class TestCrawler(Crawler):
    def task_generator(self):
        for host in islice(open('docs/domains.txt'), 100):
            host = host.strip()
            if host:
                yield Request('http://%s/' % host, tag='page')

    
bot = TestCrawler(concurrency=10)
bot.run()