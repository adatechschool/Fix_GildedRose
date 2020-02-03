# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)

    def test_ragnaros1(self):
        items = []
        for i in range(3000):
            items += [Item("Sulfuras, Hand of Ragnaros", i, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        for i in items:
            self.assertEquals(80, items[0].quality)

    def test_backstage_pass(self):
        items = []
        items += [Item("Backstage passes to a TAFKAL80ETC concert",  20, 20)]
        items += [Item("Backstage passes to a TAFKAL80ETC concert",  10, 20)]
        items += [Item("Backstage passes to a TAFKAL80ETC concert",  9, 20)]
        items += [Item("Backstage passes to a TAFKAL80ETC concert",  5, 20)]
        items += [Item("Backstage passes to a TAFKAL80ETC concert",  4, 20)]
        items += [Item("Backstage passes to a TAFKAL80ETC concert",  0, 20)]
        items += [Item("Backstage passes to a TAFKAL80ETC concert",  -1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(21, items[0].quality)
        for i in range(1, 3):
            self.assertEquals(22, items[i].quality)
        for i in range(3, 5):
            self.assertEquals(23, items[i].quality)
        for i in range(5, 7):
            self.assertEquals(0, items[i].quality)

    

if __name__ == '__main__':
    unittest.main()