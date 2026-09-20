import csv
from sorting_algorithms import merge_sort


products = []


# Load products from CSV
with open("products.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["price"] = int(row["price"])
        row["rating"] = float(row["rating"])
        row["discount"] = float(row["discount"])

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
    return merge_sort(products, "price")


def sort_by_rating():
    return merge_sort(products, "rating", True)


def products_by_category(category):
    result = []

    for product in products:
        if product["category"].lower() == category.lower():
            result.append(product)

    return result


def sort_by_discount():
    return merge_sort(products, "discount", True)


def sort_products(sort_by, reverse=False, product_list=None):

    if product_list is None:
        product_list = products

    key_map = {
        "Price": "price",
        "Rating": "rating",
        "Discount": "discount",
        "Product Name": "name"
    }

    key = key_map[sort_by]

    return merge_sort(product_list, key, reverse)


def search_products(search_text):
    search_text = search_text.lower()

    result = []

    for product in products:
        if (
            search_text in product["name"].lower()
            or search_text in product["category"].lower()
        ):
            result.append(product)

    return result