from models.product import Product

class Stock():
    def __init__(self, product, count = 0, id = None):
        self.product = product
        self.count = count
        self.id = id

    def modify_count(self,value):
        self.count = self.count + value
    
    def get_markup_based_on_stock_count(self):
        markup = self.count*(self.product.sale_price-self.product.distributor_price)
        return markup


