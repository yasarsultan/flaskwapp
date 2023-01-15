from flask import Flask, render_template

app = Flask(__name__)

#safe
# upper
# lower
# capitalized
# title
# trim
# striptags

@app.route('/')
def index():
    stuff = "This is <strong>Bold</strong> Text."
    pizza = ["Fullpizza", "Halfpizza", "Cheese", "slice"]
    return render_template('index.html', stuff=stuff, pizza=pizza)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', Name=name)

# creating custom error pages

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404 

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500