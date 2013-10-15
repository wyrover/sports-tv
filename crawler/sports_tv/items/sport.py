#!/usr/bin/env python2.6
# encoding: utf-8
# Author: guodongdong <dd.guo@foxmail.com>
# Created Time: 2013年10月15日 星期二 18时35分12秒
from scrapy.item import Item, Field

class Sport(Item):
    team1 = Field()
    team2 = Field()
    date = Field()
    time = Field()
    title = Field()
    url = Field()

def main():
    pass

if __name__ == "__main__":
    main()
