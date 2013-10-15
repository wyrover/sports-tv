from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from dirbot.items import Website


class DmozSpider(BaseSpider):
    name = "imeigu"
    allowed_domains = ["hq.imeigu.com"]
    start_urls = [
            "http://hq.imeigu.com/list.jsp?od=0&ac=0&pagex=%s" %i for i in
            range(1, 186)
    ]
    print start_urls

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
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
