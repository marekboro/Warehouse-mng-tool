import pdb

from models.product_type import ProductType
from models.brand import Brand
from models.product import Product
import repositories.product_type_repository as product_type_repository
import repositories.brand_repository as brand_repository
import repositories.product_repository as product_repository


product_type_repository.delete_all()
brand_repository.delete_all()


product_type_name = "Le-Phonette"
product_type_1 = ProductType(product_type_name)

product_type_name_2= "Le-Phonne"
product_type_2 = ProductType(product_type_name_2)
        
product_type_name_3 = "Zz Charger"
product_type_3 = ProductType(product_type_name_3)
        
product_type_name_4 = "Some accessory"
product_type_4 = ProductType(product_type_name_4)

product_type_repository.save(product_type_1)        
product_type_repository.save(product_type_2)
product_type_repository.save(product_type_3)
product_type_repository.save(product_type_4)

new_name_for_product1 = "it works"
new_id = product_type_1.id
new_product_1 = ProductType(new_name_for_product1,new_id)
product_type_repository.update(new_product_1)

#product_type_repository
brand_repository.delete_all()
brand1_name = "Dappel"
brand1_description = "like Mappel but with a D"
brand1_warranty_details = "you get robbed"
brand1 = Brand(brand1_name,brand1_description,brand1_warranty_details)
brand_repository.save(brand1)
brand2 = Brand("ShangTsung","soul-stealer","certain-death")
brand_repository.save(brand2)

brand_repository.update(Brand("Goro","a monster","fatality",brand2.id))
brand_repository.delete(brand2.id)






product_1_name = "Zapper"
product_1_description = "It will zapp you into the future"
product_1_distributor_price = 200
product_1_sale_price = 600
product_1_warranty_length = 120

product_1 = Product(product_1_name,product_type_1,brand1,product_1_description,product_1_distributor_price,product_1_sale_price,product_1_warranty_length)
product_repository.save(product_1)       

product_2_name = "dezapper"
product_2_description = "It will zapp you into the past"
product_2_distributor_price = 300
product_2_sale_price = 700
product_2_warranty_length = 140

product_2 = Product(product_2_name,product_type_1,brand1,product_2_description,product_2_distributor_price,product_2_sale_price,product_2_warranty_length)
product_repository.save(product_2)    



pdb.set_trace()