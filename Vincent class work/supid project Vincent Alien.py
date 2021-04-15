 def __init__(self,price_list):#constructor only preset the price_list primeter
        self.prices = price_list
        self.weight = int(input("please enter the weight of your package: "))

    def change_weight(self,weight):#function for modify the weight primeter
        self.weight = weight

    def add_interval(self,interval_from,interval_to,price):#add new price interval
        new_interval = [int(interval_from),int(interval_to),price]
        for i in range(len(self.prices)):
            if i[1]<new_interval[0] or i[0]>new_interval[1]:
                self.prices.insert(i,new_interval)

    def cacualte_package_price(self):#caculate the package's price
        sum_price = 0
        for price in self.prices:
            weight_interval = price[1] - price[0]
            if self.weight >= weight_interval: sum_price += weight_interval * price[2]
            else: sum_price += self.weight * price[2]
            self.weight -= weight_interval
            if self.weight <= 0: break;
        return sum_price

price_list = [[2,6,1.50],[6,10,4.00]]
test = package_price(price_list)
print("the price is: ",test.cacualte_package_price())



