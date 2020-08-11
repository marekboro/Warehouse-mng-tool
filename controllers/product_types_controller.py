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
    #products = product_repository.select_all()
    types = product_type_repository.select_all()
    return render_template("editing/typeedit.html", types = types)


@product_types_blueprint.route("/edit/removeType<id>")
def delete_product_type(id):
    product_type_repository.delete(id)
    return redirect("/edit/type-edit")

@product_types_blueprint.route("/edit/modifyType<id>", methods = ['post'])
def update_product_type(id):
    modified_product_type = ProductType(request.form['newTypeName'],id)

    product_type_repository.update(modified_product_type)
    
    return redirect("/edit/type-edit")

@product_types_blueprint.route("/edit/createType", methods = ['post'])
def add_product_type():
    new_type = ProductType(request.form['newTypeName'])
    
    product_type_repository.save(new_type)
    return redirect("/edit/type-edit")
    # types = product_type_repository.select_all()
    # return render_template("/edit/type-edit", types = types)


# @brands_blueprint.route("/edit/createNewBrand", methods = ['post'])  # create a brand from the form details
# def adding_new_brand():
#     new_brand = Brand(request.form['newBrandName'],request.form['newBrandDescription'],request.form['newBrandWarranty'])
#     brand_repository.save(new_brand)
#     return redirect("/edit/brand-edit")


