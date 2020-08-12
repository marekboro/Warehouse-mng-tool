from db.run_sql import run_sql

from models.stock import Stock
from models.product import Product

from models.product_type import ProductType
from models.brand import Brand

import repositories.brand_repository as brand_repository
import repositories.product_type_repository as product_type_repository
import repositories.product_repository as product_repository


def save(stock):

    sql = "INSERT INTO stock (product_id, count1, basket) VALUES (%s, %s, %s) RETURNING id"

    values = [stock.product.id, stock.count1, stock.basket]
    result = run_sql(sql, values)
    id = result[0]["id"]
    stock.id = id


def select_all():
    all_stock = []
    sql = "SELECT * FROM stock"
    result = run_sql(sql)
    for row in result:

        product = product_repository.select(row[1])
        a_product_in_stock = Stock(product, row["count1"], row["basket"], row["id"])
        all_stock.append(a_product_in_stock)

    return all_stock


def delete_all():
    sql = "DELETE FROM stock"
    run_sql(sql)


def select(id):
    sql = "SELECT * FROM stock WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        product = product_repository.select(result["product_id"])
        the_stock = Stock(product, result["count1"], result["basket"], result["id"])

    return the_stock


def update(stock):
    sql = "UPDATE stock SET(product_id,count1,basket) = (%s,%s,%s) WHERE id = %s"
    values = [stock.product.id, stock.count1, stock.basket, stock.id]
    run_sql(sql, values)


def modify_stock_count_of_item(stock, count_modifier):
    sql = "UPDATE stock SET(product_id,count1,basket) = (%s,%s,%s) WHERE id = %s"
    new_count = stock.count1 + count_modifier
    values = [stock.product.id, new_count, stock.basket, stock.id]
    run_sql(sql, values)


def delete_stock(id):
    sql = "DELETE FROM stock WHERE id =%s"
    values = [id]
    run_sql(sql, values)


def add_product(product, ammount):
    pass

