from flask import Blueprint, Flask, redirect, render_template, request
from models.brand import Brand
import repositories.brand_repository as brand_repository
import repositories.product_repository as product_repository


brands_blueprint = Blueprint("brands", __name__)

@brands_blueprint.route("/edit/brand-edit")
def products_editing_view():
    products = product_repository.select_all()  
    return render_template("editing/brandedit.html", products = products)