from db.run_sql import run_sql
from models.brand import Brand

def save(brand):
    sql = "INSERT INTO brands (name,description,warranty_details) VALUES (%s,%s,%s) RETURNING *"
    values = [brand.name,brand.description,brand.warranty_details]
    results = run_sql(sql,values)
    id = results[0]['id']
    brand.id = id


def select_all():
    sql = "SELECT * FROM brands"
    results = run_sql(sql)
    all_brands = []
    for row in results:
        brand = Brand(row['name'],row['description'],row['warranty_details'],row['id'])
        all_brands.append(brand)
    return all_brands

def delete_all():
    sql = "DELETE FROM brands"
    run_sql(sql)    


def select(id):
    sql = "SELECT * FROM brands WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]
    if result is not None:
        the_brand = Brand(result['name'],result['description'],result['warranty_details'],result['id'])
    return the_brand

def delete(id):
    sql = "DELETE FROM brands WHERE id = %s"
    values = [id]
    run_sql(sql,values)


def update(brand):
    sql = "UPDATE brands SET (name, description, warranty_details) = (%s,%s,%s) WHERE id = %s"
    values = [brand.name,brand.description,brand.warranty_details,brand.id]
    run_sql(sql,values)
