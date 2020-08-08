from db.run_sql import run_sql
from models.product_type import ProductType
from models.brand import Brand
from models.product import Product


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
    result = run_sql(sql, values)
    id = result[0]["id"]
    product.id = id


def select_all():
    all_products = []
    sql = "SELECT * FROM products"
    results = run_sql(sql)

    for row in results:
        a_product = Product(
            row["name"],
            row["product_type"],
            row["brand"],
            row["description"],
            row["distributor_price"],
            row["sale_price"],
            row["warranty_length"],
            row["id"],
        )
        all_products.append(a_product)

    return all_products

def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM products WHERE id=%s"
    values = [id]
    run_sql(sql,values)


# SELECT one using ID
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
