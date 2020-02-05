#!/usr/bin/env python

from code_gr.new_gilded_rose import GildedRose, Item

items = [
    ["common_items", "+5 Dexterity Vest", 9, 20],
    ["cheese", "Aged Brie", 2, 0],
    ["cheese", "Comte", 2, 10],
    ["cheese", "Bleu", 20, 0],
    ["legendary", "Sulfuras", 2, 9000],
    ["elixir", "Elixir of Wrath", 2, 20],
    ["ticket", "Backstage passes to a {} concert".format("lmao"), 30, 50],
    ["conjured", "Conjured Mana Cake", 3, 6],
    ["badsanane", "Conjured Mana Cake", 3, 6],
    ["badsasdanane", "Conjured Mana Cake", 3, 6],
    ["asdasdasuisghdasigdsaiudas", "Conjured Mana Cake", 3, 6],
]

def daily_output():
    gldr = GildedRose(items)
    days = 3
    import sys
    errors = []
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        print("-------- day {} --------\n".format(day))
        product_out = gldr.update_quality(day)
        for item in product_out:
            if len(item) != 1:
                print("{}:\n\tsell in day: {}\n\tquality: {}\n".format(item[1], item[2], item[3]))
            elif len(item) == 1:
                if item[0] not in errors:
                    errors += item
            else:
                print("An error has occured.")
    print("------------------------\n")
    for err in errors:
        print("The type '{}' is invalid!\n".format(err))


if __name__ == "__main__":
    daily_output()
