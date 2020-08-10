#import repositories.product_repository as product_repository

class Product():
    def __init__(self, name, product_type, brand, description, distributor_price, sale_price, warranty_length, id = None):
        self.name = name
        self.product_type = product_type
        self.brand = brand
        self.description = description
        self.distributor_price = distributor_price
        self.sale_price = sale_price
        self.warranty_length = warranty_length
        self.id = id
        
    def get_markup(self):
        return self.sale_price - self.distributor_price

    
