#!/usr/bin/env python2.6
# encoding: utf-8
# Author: guodongdong <dd.guo@foxmail.com>
# Created Time: 2013年10月15日 星期二 18时42分41秒
from scrapy.exceptions import DropItem
import json


class MongoDBPipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""

    # put all words in lowercase
    words_to_filter = ['politics', 'religion']

    def process_item(self, item, spider):
        with open("data", "a+") as handler:
            handler.write(json.dumps(dict(item)) + "\n")

def main():
    pass

if __name__ == "__main__":
    main()
