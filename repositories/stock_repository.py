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

# def save(stock):
    
#     sql = "INSERT INTO stock (product_id, count) VALUES (%s, %s) RETURNING id"
#     #sql = "INSERT INTO stock (product_id, product_type_id, brand_id, count) VALUES (%s,%s,%s, %s) RETURNING id"
#     #values = [stock.product.id, stock.product.product_type.id, stock.product.brand.id, 0]
#     values = [stock.product.id,0]
#     result = run_sql(sql,values)[0]
#     stock.id= result['id']
#     return stock

def save(stock):
    
    sql = "INSERT INTO stock (product_id, count) VALUES (%s, %s) RETURNING *"
    #sql = "INSERT INTO stock (product_id) VALUES (%s) RETURNING *"
    #sql = "INSERT INTO stock (product_id, product_type_id, brand_id, count) VALUES (%s,%s,%s, %s) RETURNING id"
    #values = [stock.product.id, stock.product.product_type.id, stock.product.brand.id, 0]
    
    values = [stock.product.id, stock.count]
    result = run_sql(sql,values)
    id= result[0]['id']
    stock.id = id
    #return stock



# def select_product(stock):
#     sql = "SELECT * FROM products WHERE id = %s"
#     #values = [stock.product_id]
#     values = [stock]
#     print(values) ##
#     product1 = product_repository.select(stock[1])
#     #print(f"name : {product1.name}")
#     results = run_sql(sql,values)[0]
#     product = Product(results['name'],results['product_type'],results['brand'],results['description'],results['distributor_price'],results['sale_price'],results['warranty_length'],results['id'])
    
#     #return product
#     return product1

def select_all():
    all_stock = []
    sql = "SELECT * FROM stock"
    result = run_sql(sql)
    for row in result:
        #print(f" this is the row :{row}")
        #print(row[1])
        product = product_repository.select(row[1])

        #product = select_product(row) ## # 
        #product = product_repository.select(row) ## # 
        #product = product_repository.select(row['product_id']) ## # 

        a_product_in_stock = Stock(product,row['count'])
        #a_product_in_stock = Stock(product,row['count'])
        all_stock.append(a_product_in_stock)
    
    return all_stock


def delete_all():
    sql = "DELETE FROM stock"
    run_sql(sql)


def select(id):
    sql = "SELECT * FROM stock WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)
    if result is not None:
        product = product_repository.select(result['product_id'])
        the_stock = Stock(product,result['count'])
    return the_stock




# def update(product):
#     sql = "UPDATE products SET (name,product_type_id, brand_id, description,distributor_price,sale_price,warranty_length) = (%s,%s,%s,%s,%s,%s,%s) WHERE id = %s"
#     values = [
#         product.name,
#         product.product_type.id,
#         product.brand.id,
#         product.description,
#         product.distributor_price,
#         product.sale_price,
#         product.warranty_length,
#         product.id
#     ]
#     run_sql(sql,values)

def update(stock):
    sql = "UPDATE stock SET(product_id,count) = (%s,%s) WHERE id = %s"
    values = [stock.product.id, stock.count,stock.id]
    run_sql(sql,values)


def modify_stock_count_of_item(stock, count_modifier):
    sql = "UPDATE stock SET(product_id,count) = (%s,%s) WHERE id = %s"
    new_count = stock.count + count_modifier
    values = [[stock.product.id, new_count ,stock.id]]
    run_sql(sql,values)
    
    
    # result = run_sql(sql, values)
    # if result is not None:
    #     product = product_repository.select(result['product_id'])
    #     new_count = result['count'] + count_modifier
    #     the_stock = Stock(product,new_count)
    # return the_stock
    
    
    



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