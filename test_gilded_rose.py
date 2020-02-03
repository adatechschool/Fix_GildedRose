# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose
from texttest_fixture import List

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        lst = List()
        sel_item = lst.itemsl()
        # print(len(sel_item))
        # items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(sel_item)
        gilded_rose.update_quality()
        for i in range(len(sel_item)):
            try:
                self.assertEqual(20, sel_item[i].sell_in)
            except AssertionError:
                print("Error, {}".format(sel_item[i].sell_in))

if __name__ == '__main__':
    unittest.main()
