# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose
from texttest_fixture import List

lst = List()

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        sel_item = lst.itemsl()
        print(type(sel_item[0]))
        pre_change = lst.pre_change()
        gilded_rose = GildedRose(sel_item)
        gilded_rose.update_quality()
        for i in range(len(sel_item)):
            # try:
            self.assertEqual(9, sel_item[i].sell_in)
                # print("passed")
            # except AssertionError:
            #     print("{} Error, {} != {}, {}".format( "AssertionError", pre_change[i], sel_item[i].sell_in, sel_item[i].name))

class Ragna(unittest.TestCase):
    def test_hand(self):
        sel_item = lst.itemsl()
        days = 200
        for day in range(days):
            GildedRose(sel_item).update_quality()
            print(sel_item[1].sell_in, " ", sel_item[1].quality)
        # self.assertEqual(0, sel_item[3].quality)


if __name__ == '__main__':
    unittest.main()
