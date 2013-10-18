#!/usr/bin/env python2.6
# encoding: utf-8
# Author: guodongdong <dd.guo@foxmail.com>
# Created Time: 2013年10月15日 星期二 18时42分41秒
from scrapy.exceptions import DropItem

class FilterOtherPipeline(object):
    """
    A pipeline for filtering out items not contains zuqiu and nba
    for zhibo8.com
    """

    def process_item(self, item, spider):
        url = item['url']
        if not (url.startswith("http://www.zhibo8.cc/zhibo/zuqiu") or
                url.startswith("http://www.zhibo8.cc/zhibo/nba")) :
            raise DropItem("drop other races")
        return item

def main():
    pass

if __name__ == "__main__":
    main()
