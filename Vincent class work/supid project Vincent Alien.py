import math
class package_price:
    def __init__(self,weight,price_list):
        self.prices = price_list
        self.weight = weight

    def cacualte_package_price(self):
            sum_price = 0
            for price in self.prices:
                weight_interval = price[1] - price[0]
                if self.weight >= weight_interval: sum_price += weight_interval * price[2]
                else: sum_price += self.weight * price[2]
                self.weight -= weight_interval
                if self.weight <= 0: break;
            return sum_price


