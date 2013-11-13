# encoding: utf-8

import time
import urlparse

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from sports_tv.items.sport import Sport


class Zhiobo8Spider(BaseSpider):
    name = "zhibo8"
    allowed_domains = ["www.zhibo8.cc"]
    start_urls = [
            "http://www.zhibo8.cc/",
    ]
    item_type = "sport"
    src = "直播吧"

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
                if len(link) < 1:
                    continue
                link = link[0]
                title = race.select("./a[1]/text()").extract()
                teams = race.select("./text()").extract()
                if len(teams) > 0:
                    teams = teams[0]
                else:
                    teams = ""
                for b in race.select("./b/text()").extract():
                    if len(b) > 0:
                        teams = "%s %s" % (teams, b)
                teams = teams.split(" ")
                hour_min = teams[0]
                item['time'] = hour_min
                if len(teams) > 2:
                    race_type = teams[2]
                    item['race_type'] = race_type
                if len(teams) > 5:
                    item['team1'] = teams[3:]
                    item['team2'] = teams[5:]
                item['date'] = 20131014,
                item["url"] = urlparse.urljoin(response.url, link)
                item["title"] = title
                item["date"] = date
                item['src'] = self.src
                item['type'] = self.item_type
                items.append(item)
        return items
