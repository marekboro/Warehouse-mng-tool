from flask import Blueprint, Flask, redirect, render_template, request

from models.product_type import ProductType
from models.brand import Brand
from models.product import Product
import repositories.product_type_repository as product_type_repository
import repositories.brand_repository as brand_repository
import repositories.product_repository as product_repository

products_blueprint = Blueprint("products", __name__)

# @products_blueprint.route("/simpleview")
# def products_simple_view():
#     products = product_repository.select_all()  
#     return render_template("index.html", products = products)
#     #product_types = product_type_repository.select_all() #TEST prod-type
#     #return render_template("index.html", product_types = product_types) #TEST prod-type

@products_blueprint.route("/")
def products_main():
    products = product_repository.select_all()
    
    return render_template("index.html", products = products)


@products_blueprint.route("/fullview")
def products_extended_view():
    products = product_repository.select_all()
    # count_total = product_repository.count_total()  
    #count = product_repository.count()
    return render_template("fullview/index.html", products = products)#, count_total = count_total)


@products_blueprint.route("/edit")
def products_edit():
    products = product_repository.select_all()  
    return render_template("index.html", products = products)

@products_blueprint.route("/basket")
def products_basket():
    products = product_repository.select_all()  
    return render_template("index.html", products = products)