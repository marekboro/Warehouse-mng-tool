from db.run_sql import run_sql

from models.stock import Stock
from models.product import Product

from models.product_type import ProductType
from models.brand import Brand

import repositories.brand_repository as brand_repository
import repositories.product_type_repository as product_type_repository
import repositories.product_repository as product_repository

# def save(stock):
    
#     sql = "INSERT INTO stock (product_id, product_type_id, brand_id) VALUES (%s,%s,%s) RETURNING id"
#     values = [stock.product.id, stock.product.stock.product_type.id, stock.product.brand.id]
#     result = run_sql(sql,values)[0]
#     stock.id= result['id']
#     stock.count +=1

def save(stock):
    
    sql = "INSERT INTO stock (product_id, product_type_id, brand_id, count) VALUES (%s,%s,%s, %s) RETURNING id"
    values = [stock.product.id, stock.product.product_type.id, stock.product.brand.id, 0]
    result = run_sql(sql,values)[0]
    stock.id= result['id']
    return stock

def select_all():
    all_stock = []
    sql = "SELECT * FROM stock"
    result = run_sql(sql)
    for row in result:
        a_product_in_stock = Stock(row['product'],row['count'])
        all_stock.append(a_product_in_stock)
    
    return all_stock


def delete_all():
    sql = "DELETE FROM stock"
    run_sql(sql)



#SELECT one using ID
#DELETE one using ID
#UPDATE one using ID


# def save(biting):
    
#     sql = "INSERT INTO bitings (human_id, zombie_id) VALUES (%s,%s) RETURNING id"
#     values = [biting.human.id,biting.zombie.id]
#     result = run_sql(sql,values)[0]

#     biting.id = result['id'] 
#     return biting




def add_product(product,ammount):
    pass