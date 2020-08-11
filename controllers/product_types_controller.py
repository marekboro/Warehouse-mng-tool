from flask import Blueprint, Flask, redirect, render_template, request
from models.product_type import ProductType



from models.brand import Brand
from models.product import Product
from models.stock import Stock
import repositories.brand_repository as brand_repository
import repositories.stock_repository as stock_repository


import repositories.product_type_repository as product_type_repository
import repositories.product_repository as product_repository

product_types_blueprint = Blueprint("types", __name__)


@product_types_blueprint.route("/edit/type-edit")
def types_editing_view():
    products = product_repository.select_all()
    types = product_type_repository.select_all()
    return render_template("editing/typeedit.html", types = types)

