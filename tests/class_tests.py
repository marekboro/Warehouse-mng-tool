import unittest
from models.brand import Brand
from models.product_type import ProductType
from models.product import Product

# from models.product import Product


class TestBrand(unittest.TestCase):
    def setUp(self):
        name_1 = "Shang-Tsung"
        description_1 = "description of Shang-tsung"
        warranty_details_1 = "Its all out of warranty baby"

        name_2 = "Who-Why"
        description_2 = "description of Who-Why"
        warranty_details_2 = "We hear everything and thats a guarantee!"

        self.brand_1 = Brand(name_1, description_1, warranty_details_1, None)
        self.brand_2 = Brand(name_2, description_2, warranty_details_2, None)

    def test_name_of_brand(self):
        expected = "Shang-Tsung"
        actual = self.brand_1.name
        self.assertEqual(expected, actual)

    def test_description_of_brand(self):
        # expected = "Description of Sonya Blade"
        expected = "description of Who-Why"
        actual = self.brand_2.description
        self.assertEqual(expected, actual)

    def test_warranty_details_of_brand(self):
        # expected = "we cover all damage"
        expected = "We hear everything and thats a guarantee!"
        actual = self.brand_2.warranty_details
        self.assertEqual(expected, actual)


class TestProductType(unittest.TestCase):
    def setUp(self):
        name = "Smartphone"
        self.type = ProductType(name)

    def test_product_type_name(self):
        expected = "Smartphone"
        actual = self.type.name
        self.assertEqual(expected, actual)


class TestProduct(unittest.TestCase):
    def setUp(self):
        product_name = "Universe 51"
        type_name = "Dumbphone"                         # to create product_type
        product_type = ProductType(
            type_name
            )                          # PRODUCT_TYPE
        brand_name = "Dapple"                           # to create brand
        brand_description = "ScroogeMcDuck"             # to create brand
        brand_warranty_details = "AllOutOfWarranty"     # to create brand
        product_brand = Brand(
            brand_name,
            brand_description,
            brand_warranty_details
            )                           # BRAND
        product_description = "Is a phone and a computor"
        product_distributor_price = 100
        product_sale_price = 400
        product_warranty_length = 365

        self.product1 = Product(
            product_name,
            product_type,
            product_brand,
            product_description,
            product_warranty_length,
            product_distributor_price,
            product_sale_price,
        )

    def test_product_name(self):
        expected = "Galaxy_1"                       #should Fail
        expected = "Universe 51"                    #shouls Pass
        actual = self.product1.name
        self.assertEqual(expected, actual)

    def test_product_type_name(self):
        expected = "SmartPhone"                     #should Fail
        expected = "Dumbphone"                      #shouls Pass
        actual = self.product1.product_type.name
        self.assertEqual(expected, actual)

    def test_product_brand_name(self):
        expected = "Pear"                           #should Fail
        expected = "Dapple"                         #shouls Pass
        actual = self.product1.brand.name
        self.assertEqual(expected, actual)

    def test_product_brand_description(self):
        expected = "Whats that now"                 #should Fail
        expected = "ScroogeMcDuck"                  #shouls Pass
        actual = self.product1.brand.description
        self.assertEqual(expected, actual)

    def test_product_brand_warranty_details(self):
        expected = "Galaxy_1"                       #should Fail
        expected = "AllOutOfWarranty"               #shouls Pass
        actual = self.product1.brand.warranty_details
        self.assertEqual(expected, actual)

    def test_product_description(self):
        expected = "Galaxy_1"                       #should Fail
        expected = "Is a phone and a computor"     #shouls Pass
        actual = self.product1.description
        self.assertEqual(expected, actual)

    
    def test_product_warranty_length(self):
        expected = 730                              #should Fail
        expected = 365                             #shouls Pass
        actual = self.product1.warranty_length
        self.assertEqual(expected, actual)

    
    def test_product_distributor_price(self):
        expected = 104                              #should Fail
        expected = 100                             #shouls Pass
        actual = self.product1.distributor_price
        self.assertEqual(expected, actual)
    
    def test_product_sale_price(self):
        expected = 300                              #should Fail
        expected = 400                             #shouls Pass
        actual = self.product1.sale_price
        self.assertEqual(expected, actual)



    











    # def test_(self):
    #     expected =            #should Fail
    #     expected =            #shouls Pass
    #     actual =
    #     self.assertEqual(expected,actual)

