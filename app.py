from flask import Flask, jsonify
import csv

app = Flask(__name__)

products = []

# Read products from CSV
with open("products.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["price"] = int(row["price"])
        row["rating"] = float(row["rating"])
        products.append(row)


# Home page
@app.route("/")
def home():
    return "Welcome to Product Sorter!"


# Get all products
@app.route("/products")
def get_products():
    return jsonify(products)


# Get products under a specific budget
@app.route("/products/under/<int:budget>")
def products_under_budget(budget):
    result = []

    for product in products:
        if product["price"] <= budget:
            result.append(product)

    return jsonify(result)


# Sort products by price - lowest to highest
@app.route("/products/sort/price")
def sort_price():
    result = sorted(products, key=lambda x: x["price"])

    return jsonify(result)


# Sort products by rating - highest to lowest
@app.route("/products/sort/rating")
def sort_rating():
    result = sorted(
        products,
        key=lambda x: x["rating"],
        reverse=True
    )

    return jsonify(result)


# Filter products by category
@app.route("/products/category/<category>")
def products_by_category(category):
    result = []

    for product in products:
        if product["category"].lower() == category.lower():
            result.append(product)

    return jsonify(result)


# Start Flask server
if __name__ == "__main__":
    app.run(debug=True)