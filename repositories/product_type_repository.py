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
        a_type = ProductType(row['name'])
        product_types.append(a_type)
    
    return product_types

def delete_all():
    sql = "DELETE FROM types"
    run_sql(sql)


