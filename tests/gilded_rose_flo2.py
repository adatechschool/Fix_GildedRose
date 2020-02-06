# -*- coding: utf-8 -*-
import random

class GildedRose(object):

    def __init__(self, items, pactole = 0):
        self.items = items
        self.pactole = pactole
    
    def one_more_day(self):
        self.sell_objects(item)
        self.update_quality(item)
        self.inventaire(item)

    def inventaire(self, item):
        print("Inventaire du jour : \n")
        for item in self.items:
            print("%d - %s : valeur - %d, date de péremption - %d \n") % (item, item.name, item.quality, item.sell_in)

    def count_brie(self, item):
        count = 0
        for item in self.items:
            if item.name == "Aged Brie":
                count += 1
        return count
    
    def sell_objects(self, item):  
        for item in self.items:
            proba = random.randint(0, 100)
            if proba >= 95:
                pactole += item.quality
                del item
        print("vous gagnez" + str(self.pactole) + "pokédollars")
        

    def update_quality(self, item):
        nb_brie = self.count_brie()
        for item in self.items:
            x = 1
            if item.sell_in <= 0:
                x = 2
            if "Sulfuras" in item.name:
                item.quality = 80
            else:
                if item.name == "Aged Brie" and nb_brie < 6:
                    item.quality += 1
                elif "Backstage passes" in item.name:
                    self.backstage_price(item)
                elif "Conjured" in item.name:
                    item.quality -= 2*x
                else:
                    self.check_extremes(item, x)
            if "Sulfuras" not in item.name:
                item.sell_in -= 1

    def backstage_price(self, item):
        item.quality += 1
        if item.sell_in < 11:
            item.quality += 1
        if item.sell_in < 6:
            item.quality += 1
        if item.sell_in < 1:
            item.quality = 0

    def check_extremes(self, item, x):
        item.quality -= x
        if item.quality > 50:
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
