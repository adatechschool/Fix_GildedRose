from new_gilded_rose import *

items = [
    ["normal_items", "+5 Dexterity Vest", 10, 20],
    ["cheese", "Aged Brie", 2, 0],
    ["cheese", "Comte", 2, 10],
    ["cheese", "Bleu", 20, 0],
    ["legendary", "Sulfuras", 2, 10],
    ["elixir", "Elixir of Wrath", 2, 20],
    ["ticket", "Backstage passes to a TAFKAL80ETC concert", 30, 12],
    ["conjured", "Conjured Mana Cake", 3, 6],
    ["banane", "Conjured Mana Cake", 3, 6]
]

gldr = GildedRose(items)

# print(product_out)

if __name__ == "__main__":
    print ("OMGHAI!")
    days = 100
    import sys
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        product_out = gldr.update_quality()
        print("-------- day %s --------" % day)
        for item in product_out:
            print("{}:\n\tsell in day: {}\n\tquality: {}\n".format(item[1], item[2], item[3]))
        print("")
        # GildedRose(items).update_quality()
