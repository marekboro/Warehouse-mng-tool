from flask import Flask, render_template
from controllers.products_controller import products_blueprint
from controllers.stocks_controller import stocks_blueprint
from controllers.brands_controller import brands_blueprint
from controllers.product_types_controller import product_types_blueprint

app = Flask(__name__)


app.register_blueprint(products_blueprint)
app.register_blueprint(stocks_blueprint)
app.register_blueprint(brands_blueprint)
app.register_blueprint(product_types_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)