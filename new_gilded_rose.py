class GildedRose():
    def __init__(self, item_lst):
        self.item_lst = item_lst
        return

    def update_quality(self):
        for product in range(len(self.item_lst)):
            prod_name = "prod_" + str(self.item_lst[product][0])
            try:
                method = getattr(self, prod_name)
                prodct_change_ret = method(product)
                self.item_lst[product] = prodct_change_ret
                # print(self.item_lst)
            except AttributeError:
                print("{} is an invalid type!".format(self.item_lst[product][0]))
        return self.item_lst

    def prod_normal_items(self, it):
        prodct = Item(self.item_lst[it])
        prodct_change_ret = prodct.__repr__()
        return prodct_change_ret

    def prod_cheese(self, it):
        prod_pre_change = self.item_lst[it]
        if prod_pre_change[3] < 50:
            prod_pre_change[3] += 1
        prodct = Item(prod_pre_change)
        prodct_change_ret = prodct.__repr__()
        return prodct_change_ret

    def prod_elixir(self, it):
        prodct = Item(self.item_lst[it])
        prodct_change_ret = prodct.__repr__()
        return prodct_change_ret

    def prod_legendary(self, it):
        prodct = Item(self.item_lst[it])
        prodct_change_ret = prodct.__repr__()
        return prodct_change_ret

    def prod_ticket(self, it):
        prodct = Item(self.item_lst[it])
        prodct_change_ret = prodct.__repr__()
        return prodct_change_ret

    def prod_conjured(self, it):
        prodct = Item(self.item_lst[it])
        prodct_change_ret = prodct.__repr__()
        return prodct_change_ret


class Item:
    def __init__(self, product_table):
        self.type = product_table[0]
        self.name = product_table[1]
        self.sell_in = product_table[2]
        self.quality = product_table[3]

    def __repr__(self):
        output_product = [self.type, self.name, self.sell_in, self.quality]
        return output_product
