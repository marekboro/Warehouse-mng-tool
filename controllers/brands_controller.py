from flask import Blueprint, Flask, redirect, render_template, request
from models.brand import Brand

import repositories.brand_repository as brand_repository
import repositories.product_repository as product_repository


brands_blueprint = Blueprint("brands", __name__)

@brands_blueprint.route("/edit/brand-edit") # TO view the brands
def brands_editing_view():
    #products = product_repository.select_all()  
    brands = brand_repository.select_all()
    return render_template("editing/brandedit.html",brands = brands)



@brands_blueprint.route("/edit/removeBrand<id>")    # TO delete brand
def delete_brand(id):
    brand_repository.delete(id)
    return redirect("/edit/brand-edit")



@brands_blueprint.route("/edit/editBrand<id>")  # display brand modification form
def editor_for_brand(id):
    brand = brand_repository.select(id)
    return render_template("/editing/editBrand.html", brand=brand)



@brands_blueprint.route("/edit/modifyBrand<id>", methods = ['post'])  # apply the brand modification form
def apply_brand_edits(id):

    old_brand = brand_repository.select(id)
    old_id = old_brand.id
    modified_brand = Brand(request.form['newBrandName'],request.form['newBrandDescription'],request.form['newBrandWarranty'],old_id)
    brand_repository.update(modified_brand)

    return redirect("/edit/brand-edit")