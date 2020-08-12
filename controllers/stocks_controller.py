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
    #print(stocks[0].product)
    
    #products = product_repository.select_all()
    return render_template("stock/index.html", stocks = stocks)#, products = products)


# @products_blueprint.route("/")
# def products_main():
#     products = product_repository.select_all()
    
#     return render_template("index.html", products = products)

@stocks_blueprint.route("/basket")
def basket_main():
    
    stocks = stock_repository.select_all()
    
    return render_template("stock/basket.html", stocks = stocks)


@stocks_blueprint.route("/SubmitOrders", methods = ["POST"])
def basket_to_stock():
    
    stocks = stock_repository.select_all()
    for stock in stocks:
        stock.count += stock.basket
        stock.basket =0
        stock_repository.update(stock)

    return redirect("/")  


@stocks_blueprint.route("/updatebasket<id>", methods = ["POST"])
def update_basket(ID):
    stock_item = stock_repository.select(id)
    print("1")
    new_basket= int(request.form["newBasketCount"])
    print(new_basket)
    new_stock_item = Stock(stock_item.product,stock_item.count,new_basket,stock_item.id)
    #print("3")
    stock_repository.update(new_stock_item)
    #print("4")
    

    #return render_template("stock/basket.html", stocks = stocks)
    return redirect("/basket")
    