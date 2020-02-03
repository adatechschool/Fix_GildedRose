# -*- coding: utf-8 -*-
from __future__ import print_function

from gilded_rose import *

stats = [
    ["Ragna", 0 , 80]
]

items = [
    Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
    Item(name="Aged Brie", sell_in=2, quality=0),
    Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
    Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
    Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
    Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
    Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
    Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
    Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
    ]

class List:
    def __init__(self):
        return

    def pre_change(self):
        itm_list = [10, 2, 5, 0, -1, 1, 10, 5, 3]
        return itm_list

    def itemsl(self):
        itm_list = items
        return itm_list

    def days(self):
            days = 100
            import sys
            if len(sys.argv) > 1:
                days = int(sys.argv[1]) + 1
            for day in range(days):
                print("-------- day %s --------" % day)
                for item in items:
                    print(item)
                print("")
                GildedRose(items).update_quality()



if __name__ == "__main__":
    print ("OMGHAI!")
    days = 1
    import sys
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        GildedRose(items).update_quality()
