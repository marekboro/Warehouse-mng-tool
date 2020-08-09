from db.run_sql import run_sql
from models.product_type import ProductType
from models.brand import Brand
from models.product import Product
import repositories.brand_repository as brand_repository
import repositories.product_type_repository as product_type_repository


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
        product_type = product_type_repository.select(row["product_type_id"])
        brand = brand_repository.select(row["brand_id"])
        a_product = Product(
            row["name"],
            product_type,
            brand,
            row["description"],
            row["distributor_price"],
            row["sale_price"],
            row["warranty_length"],
            row["id"]
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

def select(id):
    sql = "SELECT FROM products WHERE id=%s"
    values = [id]
    result = run_sql(sql,values)[0]
    
    product_type = product_type_repository.select(result["product_type_id"])
    brand = brand_repository.select(result["brand_id"])
    
    a_product = Product(
            result["name"],
            product_type,
            brand,
            result["description"],
            result["distributor_price"],
            result["sale_price"],
            result["warranty_length"],
            result["id"]
        )
    return a_product

def update(product):
    sql = "UPDATE products SET (name,product_type_id, brand_id, description,distributor_price,sale_price,warranty_length) = (%s,%s,%s,%s,%s,%s,%s) WHERE id = %s"
    values = [
        product.name,
        product.product_type.id,
        product.brand.id,
        product.description,
        product.distributor_price,
        product.sale_price,
        product.warranty_length,
        product.id
    ]
    run_sql(sql,values)

# UPDATE one using ID
