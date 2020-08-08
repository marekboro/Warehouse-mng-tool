import unittest
from models.brand import Brand
from models.product_type import ProductType
from models.product import Product
#from models.product import Product

class TestBrand(unittest.TestCase):
    def setUp(self):
        name_1 = "Shang-Tsung"
        description_1 = "description of Shang-tsung"
        warranty_details_1 = "Its all out of warranty baby"
        
        name_2 = "Who-Why"
        description_2 = "description of Who-Why"
        warranty_details_2 = "We hear everything and thats a guarantee!"

        self.brand_1 = Brand(name_1,description_1,warranty_details_1,None)
        self.brand_2 = Brand(name_2,description_2,warranty_details_2,None)

    def test_name_of_brand(self):
        expected = "Shang-Tsung"
        actual = self.brand_1.name
        self.assertEqual(expected,actual)
    
    def test_description_of_brand(self):
        #expected = "Description of Sonya Blade"
        expected = "description of Who-Why"
        actual = self.brand_2.description
        self.assertEqual(expected,actual)

    def test_warranty_details_of_brand(self):
        #expected = "we cover all damage"
        expected = "We hear everything and thats a guarantee!"
        actual = self.brand_2.warranty_details
        self.assertEqual(expected,actual)

class TestProductType(unittest.TestCase):
    def setUp(self):
        name = "Smartphone"
        self.type = ProductType(name)
    
    def test_product_type_name(self):
        expected = "Smartphone"
        actual = self.type.name
        self.assertEqual(expected,actual)

class TestProduct(unittest.TestCase):
    def setUp(self):
        name = "Universe 51"
        type_name = "Dumbphone"
        product_type = ProductType(type_name)
        brand_name = "Dapple"
        brand_description = "ScroogeMcDuck"
        brand_warranty_details = "AllOutOfWarranty"
        brand = Brand(brand_name,brand_description,brand_warranty_details)
        product_distributor_price = 100
        product_sale_price = 400
        product_warranty = 365

        self.product1 = Product(name,product_type,brand,brand_description,product_warranty,product_distributor_price,product_sale_price)
    

    def test_product_name(self):
        expected = "Galaxy_1"
        actual = self.product1.name
        self.assertEqual(expected,actual)

    # def test_(self):
    #     expected = 
    #     actual = 
    #     self.assertEqual(expected,actual)


        



    