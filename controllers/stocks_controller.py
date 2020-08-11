from flask import Blueprint, Flask, redirect, render_template, request

from models.product_type import ProductType
from models.brand import Brand
from models.product import Product
from models.stock import Stock
import repositories.product_type_repository as product_type_repository
import repositories.brand_repository as brand_repository
import repositories.product_repository as product_repository
import repositories.stock_repository as stock_repository

stocks_blueprint = Blueprint("stock", __name__)

@stocks_blueprint.route("/fullview")
def stocks_main():
    #products = product_repository.select_all()
    stocks = stock_repository.select_all()
    print(stocks[0].product)
    
    #products = product_repository.select_all()
    return render_template("stock/index.html", stocks = stocks)#, products = products)


# @products_blueprint.route("/")
# def products_main():
#     products = product_repository.select_all()
    
#     return render_template("index.html", products = products)