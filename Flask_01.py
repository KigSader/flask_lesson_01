from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/main/')
def index():
    content = {"title": "Основное меню"}
    return render_template("Main_01.html", **content)


@app.route('/products/')
def products():
    content = {"title": "Брюки"}
    return render_template("products.html", **content)


@app.route('/shoes/')
def shoes():
    content = {"title": "Обувь"}
    return render_template("shoes.html", **content)


@app.route('/jackets/')
def jackets():
    content = {"title": "Куртки"}
    return render_template("jackets.html", **content)


if __name__ == '__main__':
    app.run(debug=True)
