#!/usr/bin/env python

from code_gr.decay_types import Decay

class GildedRose():
    def __init__(self, item_lst):
        self.item_lst = item_lst #structure = [type, name, sell_in, quality]
        self.dcy = Decay()
        return

    def update_quality(self):
        for product in range(len(self.item_lst)):
            prod_name = "prod_" + str(self.item_lst[product][0])
            try:
                method = getattr(self, prod_name)
                prodct_change_ret = method(product)
                self.item_lst[product] = prodct_change_ret
            except AttributeError:
                self.item_lst[product] = [self.item_lst[product][0]]
        return self.item_lst

    def prod_common_items(self, it):
        prod_pre_change = self.item_lst[it]
        res_normal = self.dcy.normal_dc(prod_pre_change[2], prod_pre_change[3]) #go calc the stuff
        prod_pre_change[2], prod_pre_change[3] = res_normal[0], res_normal[1] #replace the results
        prdct_print = Item(prod_pre_change)
        prodct_change_ret = prdct_print.out_prodction_text()
        return prodct_change_ret

    def prod_cheese(self, it):
        prod_pre_change = self.item_lst[it]
        res_cheese = self.dcy.cheese_dc(prod_pre_change[2], prod_pre_change[3]) #go calc the stuff
        prod_pre_change[2], prod_pre_change[3] = res_cheese[0], res_cheese[1] #replace the results
        prodct = Item(prod_pre_change)
        prodct_change_ret = prodct.out_prodction_text()
        return prodct_change_ret

    def prod_elixir(self, it):
        prod_pre_change = self.item_lst[it]
        res_normal = self.dcy.normal_dc(prod_pre_change[2], prod_pre_change[3]) #go calc the stuff
        prod_pre_change[2], prod_pre_change[3] = res_normal[0], res_normal[1] #replace the results
        prdct_print = Item(prod_pre_change)
        prodct_change_ret = prdct_print.out_prodction_text()
        return prodct_change_ret

    def prod_legendary(self, it):
        prod_pre_change = self.item_lst[it]
        res_normal = self.dcy.legendary_dc(prod_pre_change[2], prod_pre_change[3]) #go calc the stuff
        prod_pre_change[2], prod_pre_change[3] = res_normal[0], res_normal[1] #replace the results
        prdct_print = Item(prod_pre_change)
        prodct_change_ret = prdct_print.out_prodction_text()
        return prodct_change_ret

    def prod_ticket(self, it):
        prod_pre_change = self.item_lst[it]
        res_normal = self.dcy.ticket_dc(prod_pre_change[2], prod_pre_change[3]) #go calc the stuff
        prod_pre_change[2], prod_pre_change[3] = res_normal[0], res_normal[1] #replace the results
        prdct_print = Item(prod_pre_change)
        prodct_change_ret = prdct_print.out_prodction_text()
        return prodct_change_ret

    def prod_conjured(self, it):
        prod_pre_change = self.item_lst[it]
        res_cheese = self.dcy.conj_dc(prod_pre_change[2], prod_pre_change[3]) #go calc the stuff
        prod_pre_change[2], prod_pre_change[3] = res_cheese[0], res_cheese[1] #replace the results
        prodct = Item(prod_pre_change)
        prodct_change_ret = prodct.out_prodction_text()
        return prodct_change_ret


class Item:
    def __init__(self, product_table):
        self.type = product_table[0]
        self.name = product_table[1]
        self.sell_in = product_table[2]
        self.quality = product_table[3]

    def out_prodction_text(self):
        output_product = [self.type, self.name, self.sell_in, self.quality]
        return output_product
