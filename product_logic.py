import csv

products = []

# Load products from CSV
with open("products.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["price"] = int(row["price"])
        row["rating"] = float(row["rating"])
        products.append(row)


def get_products():
    return products


def products_under_budget(budget):
    result = []

    for product in products:
        if product["price"] <= budget:
            result.append(product)

    return result


def sort_by_price():
    return sorted(products, key=lambda x: x["price"])


def sort_by_rating():
    return sorted(products, key=lambda x: x["rating"], reverse=True)


def products_by_category(category):
    result = []

    for product in products:
        if product["category"].lower() == category.lower():
            result.append(product)

    return result