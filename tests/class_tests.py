import unittest
from models.brand import Brand
from models.product_type import ProductType
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
        name_1 = "Smartphone"
        name_2 = "charger"
        self.type_1 = ProductType(name_1)
    
    def test_product_type_name(self):
        expected = "DumbPhone"
        actual = self.type_1.name
        self.assertEqual(expected,actual)

        



    