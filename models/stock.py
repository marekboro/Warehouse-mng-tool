

class Stock():
    #def __init__(self, product, count = 0, id = None):
    def __init__(self, product, count1 = 0, basket =0, id = None):
        self.product = product
        self.count1 = count1
        self.basket= basket
        self.id = id

    def modify_count(self,value):
        self.count1 = self.count1 + value
    
    def get_markup_based_on_stock_count(self):
        markup = self.count1*(self.product.sale_price-self.product.distributor_price)
        return markup

    def get_markup_based_on_basekt_count(self):
        markup = self.basket*(self.product.sale_price-self.product.distributor_price)
        return markup


