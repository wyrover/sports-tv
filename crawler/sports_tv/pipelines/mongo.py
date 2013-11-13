#!/usr/bin/env python2.6
# encoding: utf-8
# Author: guodongdong <dd.guo@foxmail.com>
# Created Time: 2013年10月15日 星期二 18时42分41秒
from scrapy.exceptions import DropItem

class MongoDBPipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""

    def process_item(self, item, spider):
        for key in item :
            value = item[key]
            if type(value) is list and len(value) <1:
                return
        for key in item:
            value = item[key]
            if type(value) is list:
                value = value[0]
            print key, value,
        print "\n"

def main():
    pass

if __name__ == "__main__":
    main()
