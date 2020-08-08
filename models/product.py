class Product():
    def __init__(self, name, product_type, brand, description, warranty, distributor_price, sale_price, id = None):
        self.name = name
        self.product_type = product_type
        self.brand = brand
        self.description = description
        self.distributor_price = distributor_price
        self.sale_price = sale_price
        self.warranty = warranty
        self.id = id
        