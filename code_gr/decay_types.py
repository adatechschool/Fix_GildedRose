#!/usr/bin/env python

class Decay():
    def __init__(self):
        return

    def normal_dc(self, sell_in_calc, quality_calc):
        sell_in_calc -= 1
        if sell_in_calc >= 0 and quality_calc > 0:
            quality_calc -= 1
        elif sell_in_calc < 0 and quality_calc > 0:
            quality_calc -= 2
        else:
            quality_calc = 0
        list_normal_calc = [sell_in_calc, quality_calc]
        return list_normal_calc

    def cheese_dc(self, sell_in_calc, quality_calc):
        sell_in_calc -= 1
        if quality_calc < 50:
            quality_calc += 1
        list_cheese_calc = [sell_in_calc, quality_calc]
        return list_cheese_calc

    def legendary_dc(self, sell_in_calc, quality_calc):
        sell_in_calc -= 1
        list_legendary_calc = [sell_in_calc, quality_calc]
        return list_legendary_calc

    def ticket_dc(self, sell_in_calc, quality_calc):
        sell_in_calc -= 1
        if sell_in_calc >= 11:
            quality_calc -= 1
        elif 5 < sell_in_calc < 11:
            quality_calc -= 2
        elif sell_in_calc <= 5:
            quality_calc -= 3
        if sell_in_calc < 0 or quality_calc < 0:
            quality_calc = 0
        list_legendary_calc = [sell_in_calc, quality_calc]
        return list_legendary_calc

    def conj_dc(self, sell_in_calc, quality_calc):
        sell_in_calc -= 1
        if sell_in_calc >= 0 and quality_calc > 0:
            quality_calc -= 2
        elif sell_in_calc < 0 and quality_calc > 0:
            quality_calc -= 4
            quality_calc
        else:
            quality_calc = 0
        list_normal_calc = [sell_in_calc, quality_calc]
        return list_normal_calc
