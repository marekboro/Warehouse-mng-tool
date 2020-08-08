import pdb

from models.product_type import ProductType
import repositories.product_type_repository as product_type_repository


product_type_repository.delete_all()

product_name = "Le-Phonette"
product_type_1 = ProductType(product_name)

product_name_2= "Le-Phonne"
product_type_2 = ProductType(product_name_2)
        
product_name_3 = "Zz Charger"
product_type_3 = ProductType(product_name_3)
        
product_name_4 = "Some accessory"
product_type_4 = ProductType(product_name_4)

product_type_repository.save(product_type_1)        
product_type_repository.save(product_type_2)
product_type_repository.save(product_type_3)
product_type_repository.save(product_type_4)

new_name_for_product1 = "it works"
new_id = product_type_1.id
new_product_1 = ProductType(new_name_for_product1,new_id)
product_type_repository.update(new_product_1)

pdb.set_trace()