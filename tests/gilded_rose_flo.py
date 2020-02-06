# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            variance = -1
            if 'Conjured' in item.name:
                variance -= 1
            if "Sulfuras" in item.name:
                variance = 0
            elif item.quality < 50:
                if item.sell_in >= 0:
                    if "Backstage passes" in item.name or item.name == "Aged Brie":
                        variance = -variance
                        if "Backstage passes" in item.name:
                            if item.sell_in < 11:
                                variance += 1
                            if item.sell_in < 6:
                                variance += 1
                            if item.sell_in < 1:
                                variance = 0
                else:
                    if "Backstage passes" in item.name:
                        item.quality = 0
                        variance = 0
                    if item.name == "Aged Brie":
                        variance = -variance
                    variance = variance * 2
            item.quality += variance       
            if item.quality > 50 and "Sulfuras" not in item.name:
                item.quality = 50
            if item.quality < 0:
                item.quality = 0

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
