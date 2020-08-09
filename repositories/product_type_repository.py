from db.run_sql import run_sql
from models.product_type import ProductType

def save(product_type):
    sql = "INSERT INTO types (name) VALUES (%s) RETURNING *"
    values = [product_type.name]
    results = run_sql(sql,values)
    id = results[0]['id']
    product_type.id = id

def select_all():
    product_types = []
    sql = "SELECT * FROM types"
    results = run_sql(sql)

    for row in results:
        a_type = ProductType(row['name'],row['id'])
        product_types.append(a_type)
    
    return product_types

def delete_all():
    sql = "DELETE FROM types"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM types WHERE id = %s"
    values = [id]
    run_sql(sql,values)

def select(id):
    sql = "SELECT FROM types WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]
    product_type = ProductType(result['name'],result['id'])
    return product_type

def update(product_type):
    sql = "UPDATE types SET name = %s WHERE id =%s"     # now I get it. 
    values = [product_type.name,product_type.id]
    run_sql(sql,values)

def update_name(product_type,new_name):
    sql = "UPDATE types SET name = %s WHERE id = %s"
    values = [new_name,product_type.id]
    run_sql(sql,values)


