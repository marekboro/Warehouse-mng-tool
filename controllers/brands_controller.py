from flask import Blueprint, Flask, redirect, render_template, request
from models.brand import Brand

import repositories.brand_repository as brand_repository
import repositories.product_repository as product_repository


brands_blueprint = Blueprint("brands", __name__)

@brands_blueprint.route("/edit/brand-edit")
def brands_editing_view():
    #products = product_repository.select_all()  
    brands = brand_repository.select_all()
    return render_template("editing/brandedit.html",brands = brands)



@brands_blueprint.route("/edit/removeBrand<id>")
def delete_brand(id):
    brand_repository.delete(id)
    return redirect("/edit/brand-edit")

@brands_blueprint.route("/edit/editBrand<id>")
def edit_brand(id):
    brand = brand_repository.select(id)
    return render_template("/edit/editingBrand", brand=brand)