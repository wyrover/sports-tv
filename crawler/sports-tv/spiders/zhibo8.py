from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from dirbot.items import Website


class Zhiobo8Spider(BaseSpider):
    name = "zhibo8"
    allowed_domains = ["www.zhibo8.cc"]
    start_urls = [
            "http://www.zhibo8.cc/",
    ]

    def parse(self, response):
        """
        """
        hxs = HtmlXPathSelector(response)
        rows = hxs.select('//tr[@id]')
        items = []

        for row in rows:
            item = Website()
            item['stockcode'] = row.select("./td[1]/a/text()").extract()
            item['stockname'] = row.select("./td[2]/a/text()").extract()
            item['current_price'] = row.select("./td[3]/text()").extract()
            item['percentage'] = row.select("./td[4]/text()").extract()
            item['year_percentage'] = row.select("./td[5]/text()").extract()
            item['marketCapital'] = row.select("./td[6]/text()").extract()
            item['pe'] = row.select("./td[7]/text()").extract()
            item['volume'] = row.select("./td[8]/text()").extract()
            item['stockcode_link'] = row.select("./td[1]/a/@href").extract()
            items.append(item)

        return items
