import pdb

from models.product_type import ProductType
from models.brand import Brand
from models.product import Product
import repositories.product_type_repository as product_type_repository
import repositories.brand_repository as brand_repository
import repositories.product_repository as product_repository


def clear_all_tables():
    product_repository.delete_all()
    product_type_repository.delete_all()
    brand_repository.delete_all()

def setup_product_types():
    product_type_name_1 = "Le-Phonette"
    global product_type_1
    product_type_1 = ProductType(product_type_name_1)
    product_type_name_2= "Le-Phonne"
    global product_type_2
    product_type_2 = ProductType(product_type_name_2)
    product_type_name_3 = "Zz Charger"
    global product_type_3 # = ProductType(product_type_name_3)
    product_type_3 = ProductType(product_type_name_3)
    product_type_name_4 = "Some accessory"
    global product_type_4 #= ProductType(product_type_name_4)
    product_type_4 = ProductType(product_type_name_4)

    product_type_repository.save(product_type_1)        
    product_type_repository.save(product_type_2)
    product_type_repository.save(product_type_3)
    product_type_repository.save(product_type_4)


# # # # # # updating by ID
# new_name_for_product1 = "it works"
# new_id = product_type_1.id
# new_product_1 = ProductType(new_name_for_product1,new_id)
# product_type_repository.update(new_product_1)
# # # # # # 

#product_type_repository

def setup_brands():

    brand1_name = "Dappel"
    brand1_description = "like Mappel but with a D"
    brand1_warranty_details = "you get robbed"
    global brand1# = Brand(brand1_name,brand1_description,brand1_warranty_details)
    brand1 = Brand(brand1_name,brand1_description,brand1_warranty_details)
    global brand2 #= Brand("ShangTsung","soul-stealer","certain-death")
    brand2 = Brand("ShangTsung","soul-stealer","certain-death")
    brand_repository.save(brand1)
    brand_repository.save(brand2)


# # # # # # UPDATE BRANDS by ID
# brand_repository.update(Brand("Goro","a monster","fatality",brand2.id))    
# brand_repository.delete(brand2.id)
    



def setup_products():

    product_1_name = "Zapper"
    product_1_description = "It will zapp you into the future"
    product_1_distributor_price = 200
    product_1_sale_price = 600
    product_1_warranty_length = 120
    global product_1 #= Product(product_1_name,product_type_1,brand1,product_1_description, product_1_distributor_price,product_1_sale_price,product_1_warranty_length)      
    product_1 = Product(product_1_name,product_type_1,brand1,product_1_description, product_1_distributor_price,product_1_sale_price,product_1_warranty_length)      
    product_2_name = "dezapper"
    product_2_description = "It will zapp you into the past"
    product_2_distributor_price = 300
    product_2_sale_price = 700
    product_2_warranty_length = 140
    global product_2 #= Product(product_2_name,product_type_1,brand1,product_2_description, product_2_distributor_price,product_2_sale_price,product_2_warranty_length)
    product_2 = Product(product_2_name,product_type_1,brand1,product_2_description, product_2_distributor_price,product_2_sale_price,product_2_warranty_length)
    product_repository.save(product_1)   
    product_repository.save(product_2)    

#product_repository.delete(product_1.id)
#product_repository.delete(product_2.id)

#print(product_repository.select(product_1.id).name)

clear_all_tables()
setup_product_types()
setup_brands()
setup_products()


# # # # # UPDATE product works
# product3= Product("buzzbuzz",product_type_1,brand2,"makes Buzzing sounds",100,245,365,product_2.id)
# product_repository.update(product3)


pdb.set_trace()