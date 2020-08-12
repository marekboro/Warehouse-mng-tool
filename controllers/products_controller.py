from flask import Blueprint, Flask, redirect, render_template, request

from models.product_type import ProductType
from models.brand import Brand
from models.product import Product
from models.stock import Stock
import repositories.product_type_repository as product_type_repository
import repositories.brand_repository as brand_repository
import repositories.product_repository as product_repository
import repositories.stock_repository as stock_repository


products_blueprint = Blueprint("products", __name__)


@products_blueprint.route("/")
def products_main():
    stocks = stock_repository.select_all()
    return render_template("index.html", stocks=stocks)


@products_blueprint.route("/fullview1")
def products_extended_view():
    products = product_repository.select_all()

    return render_template("fullview/index.html", products=products)


@products_blueprint.route("/edit")
def products_edit():

    products = product_repository.select_all()
    return render_template("editing/index.html", products=products)


@products_blueprint.route("/edit/prod-edit")
def products_editing_view():
    products = product_repository.select_all()
    return render_template("editing/prodedit.html", products=products)


@products_blueprint.route("/edit/removeProduct<id>")
def delete_product(id):
    product_repository.delete(id)
    return redirect("/edit/prod-edit")


@products_blueprint.route("/edit/editAProduct<id>")
def view_product_to_edit(id):
    product = product_repository.select(id)
    brands = brand_repository.select_all()
    types = product_type_repository.select_all()
    return render_template(
        "editing/editProduct.html", product=product, brands=brands, types=types
    )


@products_blueprint.route("/edit/editTheProduct<id>", methods=["POST"])
def edit_a_product(id):
    old_product = product_repository.select(id)

    the_id = old_product.id

    updated_type = product_type_repository.select(request.form["type_choice"])

    updated_brand = brand_repository.select(request.form["brand_choice"])

    updated_product = Product(
        request.form["newProductName"],
        updated_type,
        updated_brand,
        request.form["newProductDescription"],
        request.form["newProductDistPrice"],
        request.form["newProductSalePrice"],
        request.form["newProductWarrantyLength"],
        the_id,
    )

    product_repository.update(updated_product)

    return redirect("/fullview")


@products_blueprint.route("/edit/addAProduct")
def add_a_product():
    brands = brand_repository.select_all()
    types = product_type_repository.select_all()

    return render_template("editing/addProduct.html", brands=brands, types=types)


@products_blueprint.route("/edit/CreateProduct", methods=["POST"])
def create_a_product():
    product_type = product_type_repository.select(request.form["type_choice"])
    product_brand = brand_repository.select(request.form["brand_choice"])
    new_product = Product(
        request.form["newProductName"],
        product_type,
        product_brand,
        request.form["newProductDescription"],
        request.form["newProductDistPrice"],
        request.form["newProductSalePrice"],
        request.form["newProductWarrantyLength"],
    )

    product_repository.save(new_product)
    new_stock_item = Stock(new_product)
    stock_repository.save(new_stock_item)

    return redirect("/fullview")
