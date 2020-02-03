# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose
from texttest_fixture import List

lst = List()

class GildedRoseTest(unittest.TestCase):
    def test_brie(self):
        # sel_item = lst.itemsl()
        days = 200
        items = []
        items += [Item("Aged Brie", 0, -30)]
        gilded_rose = GildedRose(items)
        for day in range(days):
            GildedRose(items).update_quality()
        self.assertEqual(50, items[0].quality)

    def test_hand(self):
        days = 200
        items = []
        items += [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        for day in range(days):
            GildedRose(items).update_quality()
            if items[0].quality != 80:
                break
        self.assertEqual(80, items[0].quality)

    def test_mana(self):
        days = 10
        items = []
        items += Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
        gilded_rose = GildedRose(items)
        for day in range(days):
            GildedRose(items).update_quality()
            if items[0].sell_in == 0:
                break
        self.assertEqual(0, items[0].quality)
        # supposed to decrement by 2 on every iteration, only decrements by 1

    def test_dex(self):
        days = 100
        items = []
        items += Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        for day in range(days):
            first_it = items[0].quality
            GildedRose(items).update_quality()
            if items[0].sell_in <= 0:
                if first_it == items[0].quality + 2:
                    decr = 2
        self.assertEqual(2, decr)
        self.assertEqual(0, items[0].quality)

    def test_tickets(self):
        days = 200
        items = []
        items += Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        counter = 0
        for day in range(days):
            GildedRose(items).update_quality()
            if items[0].quality > counter:
                counter = items[0].quality
            elif items[0].quality == 0:
                break
        self.assertEqual(50, counter)
        self.assertEqual(0, items[0].quality)

    def test_elixir(self):
        days = 200
        items = []
        items += Item(name="Elixir of the Mongoose", sell_in=5, quality=50),
        for day in range(days):
            first_it = items[0].quality
            GildedRose(items).update_quality()
            if items[0].sell_in <= 0:
                if first_it == items[0].quality + 2:
                    decr = 2
        self.assertEqual(2, decr)
        self.assertEqual(0, items[0].quality)

if __name__ == '__main__':
    unittest.main()
