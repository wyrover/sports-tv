#!/usr/bin/env python2.7
# encoding: utf-8
# Author: guodongdong <dd.guo@foxmail.com>
# Created Time: 2013年11月12日 星期二 20时39分41秒
import urlparse

from scrapy.exceptions import DropItem

class FilesOutputPipeline(object):
    """A pipeline for output items to files"""
    needed_keys = [
        "url",
        "title",
        "teams_time",
        "date",
    ]

    def process_item(self, item, spider):
        urls = item['title']
        result = {}
        for key in dict(item):
            values = item.get(key, [])
            if type(values) is not list:
                continue
            if len(values) < 1 and key in self.needed_keys:
                raise DropItem("need at least one value for %s" % key)
            if len(values) > 0:
            	result[key] = values[0]
        for key in result:
            item[key] = result[key]
        output= ""
        item['date'] = item['date'].split(" ")[0]
        item['url'] = urlparse.urljoin(item['base_url'], item['url'])
        tt_items = item['teams_time'].split(" ")
        if len(tt_items) > 0:
           item['race_time'] = tt_items[0]
        if len(tt_items) > 1:
           item['race'] = tt_items[1]
        if len(tt_items) == 5:
            team1_team2 = items[2]
            item['team1'], item['team2'] = team1_team2.split("-")
            print  "%s-%s" % (item['team1'], item['team2']) 
        if len(tt_items) == 6:
           item['team1'] = tt_items[2]
           item['team2'] = tt_items[4]
           print  "%s-%s" % (item['team1'], item['team2']) 
        #print tt_items
        for key in dict(item):
            value = item[key]
            if not value:
                continue
            if not output:
                output = "%s|||%s" % (key, item[key])
            else:
                output = "%s\t%s|||%s" % (output, key, item[key])
        output = "%s\n" % output
        output = output.encode("utf-8")
        open(spider.name, "a+").write(output)

def main():
    pass

if __name__ == "__main__":
    main()
