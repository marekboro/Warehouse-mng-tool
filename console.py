import pdb

from models.product_type import ProductType
import repositories.product_type_repository as product_type_repository

product_name = "Le-Phonette"
product_type_1 = ProductType(product_name)
product_type_repository.save(product_type_1)
product_type_repository.delete_all()

pdb.set_trace()