from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
import time

from sports_tv.items.sport import Sport


class Zhiobo8Spider(BaseSpider):
    name = "zhibo8"
    allowed_domains = ["www.zhibo8.cc"]
    start_urls = [
            "http://www.zhibo8.cc/",
    ]
    item_type = "sport"

    def parse(self, response):
        """
        """
        hxs = HtmlXPathSelector(response)
        boxes = hxs.select("//div[@class='box']")
        print "get %s days" % len(boxes)
        items = []
        for box in boxes:
            title_bar = box.select("./div[@class='titlebar']")
            if not title_bar:
                continue
            date = title_bar.select("./h2/text()").extract()
            content = box.select("./div[@class='content']/ul")
            print "date %s" % date
            races = content.select("./li")
            print "get %s reaces for date %s" % (len(races), date)
            for race in races:
                item = Sport()
                link = race.select("./a[1]/@href").extract()
                title = race.select("./a[1]/text()").extract()
                teams = race.select("./text()").extract()
                item['team1'] = "team1"
                item['team2'] = "team2"
                item['time'] = int(time.time())
                item['date'] = 20131014,
                item["url"] = link
                item["title"] = title
                item["date"] = date
                print item
                items.append(item)
        return items
