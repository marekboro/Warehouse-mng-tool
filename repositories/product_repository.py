from db.run_sql import run_sql
from models.product_type import ProductType
from models.brand import Brand


def save(product):
    sql = "INSERT INTO products (name,product_type_id, brand_id, description,distributor_price,sale_price,warranty_length) VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING id"
    values = [
        product.name,
        product.product_type.id,
        product.brand.id,
        product.description,
        product.distributor_price,
        product.sale_price,
        product.warranty_length,
    ]
    result = run_sql(sql,values)
    id = result[0]['id']
    product.id = id


# SAVE
# SELECT ALL
# SELECT one using ID
# DELETE ALL
# DELETE one using ID
# UPDATE one using ID

# CREATE TABLE products(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(255),
#     product_type_id SERIAL REFERENCES types(id),
#     brand_id SERIAL REFERENCES brands(id),
#     description TEXT,
#     distributor_price FLOAT,
#     sale_price FLOAT,
#     warranty_length INT
# );
# #
