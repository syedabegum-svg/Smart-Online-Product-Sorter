import tkinter as tk
from tkinter import ttk

from product_logic import get_products, sort_products, search_products


products_data = []


# ---------------- MAIN WINDOW ----------------

root = tk.Tk()

root.title("Smart Online Product Sorter")
root.geometry("1100x700")
root.minsize(900, 600)

root.configure(bg="#f4f6f8")


# ---------------- HEADER ----------------

header = tk.Frame(root, bg="#1f2937", height=100)
header.pack(fill="x")

title = tk.Label(
    header,
    text="SMART ONLINE PRODUCT SORTER",
    font=("Segoe UI", 24, "bold"),
    bg="#1f2937",
    fg="white"
)
title.pack(pady=(20, 2))

subtitle = tk.Label(
    header,
    text="DAA Case Study • Product Sorting using Algorithms",
    font=("Segoe UI", 11),
    bg="#1f2937",
    fg="#d1d5db"
)
subtitle.pack()


# ---------------- SEARCH SECTION ----------------

search_frame = tk.Frame(root, bg="#f4f6f8")
search_frame.pack(fill="x", padx=30, pady=(20, 5))


def search_product():
    search_text = search_entry.get()

    results = search_products(search_text)

    for item in product_table.get_children():
        product_table.delete(item)

    for product in results:
        product_table.insert(
            "",
            "end",
            values=(
                product["name"],
                product["category"],
                product["price"],
                product["rating"],
                str(product["discount"]) + "%"
            )
        )


search_label = tk.Label(
    search_frame,
    text="🔎 Search Product",
    font=("Segoe UI", 10, "bold"),
    bg="#f4f6f8"
)

search_label.pack(side="left", padx=(0, 10))


search_entry = ttk.Entry(
    search_frame,
    width=35
)

search_entry.pack(side="left", padx=5)


search_button = ttk.Button(
    search_frame,
    text="SEARCH",
    command=search_product
)

search_button.pack(side="left", padx=5)


# ---------------- PRODUCT INPUT SECTION ----------------

input_frame = tk.LabelFrame(
    root,
    text=" Add Product ",
    font=("Segoe UI", 12, "bold"),
    bg="#f4f6f8",
    fg="#1f2937",
    padx=20,
    pady=15
)

input_frame.pack(
    fill="x",
    padx=30,
    pady=20
)


# ---------------- PRODUCT NAME ----------------

tk.Label(
    input_frame,
    text="Product Name",
    font=("Segoe UI", 10, "bold"),
    bg="#f4f6f8"
).grid(
    row=0,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)

product_name_entry = ttk.Entry(
    input_frame,
    width=25
)

product_name_entry.grid(
    row=1,
    column=0,
    padx=10,
    pady=5
)


# ---------------- CATEGORY ----------------

tk.Label(
    input_frame,
    text="Category",
    font=("Segoe UI", 10, "bold"),
    bg="#f4f6f8"
).grid(
    row=0,
    column=1,
    padx=10,
    pady=8,
    sticky="w"
)

category_combo = ttk.Combobox(
    input_frame,
    values=[
        "Electronics",
        "Footwear",
        "Clothing",
        "Beauty",
        "Accessories",
        "Home",
        "Toys"
    ],
    state="readonly",
    width=22
)

category_combo.grid(
    row=1,
    column=1,
    padx=10,
    pady=5
)

category_combo.set("Electronics")


# ---------------- PRICE ----------------

tk.Label(
    input_frame,
    text="Price (₹)",
    font=("Segoe UI", 10, "bold"),
    bg="#f4f6f8"
).grid(
    row=0,
    column=2,
    padx=10,
    pady=8,
    sticky="w"
)

price_entry = ttk.Entry(
    input_frame,
    width=15
)

price_entry.grid(
    row=1,
    column=2,
    padx=10,
    pady=5
)


# ---------------- RATING ----------------

tk.Label(
    input_frame,
    text="Rating",
    font=("Segoe UI", 10, "bold"),
    bg="#f4f6f8"
).grid(
    row=0,
    column=3,
    padx=10,
    pady=8,
    sticky="w"
)

rating_entry = ttk.Entry(
    input_frame,
    width=12
)

rating_entry.grid(
    row=1,
    column=3,
    padx=10,
    pady=5
)


# ---------------- DISCOUNT ----------------

tk.Label(
    input_frame,
    text="Discount (%)",
    font=("Segoe UI", 10, "bold"),
    bg="#f4f6f8"
).grid(
    row=0,
    column=4,
    padx=10,
    pady=8,
    sticky="w"
)

discount_entry = ttk.Entry(
    input_frame,
    width=12
)

discount_entry.grid(
    row=1,
    column=4,
    padx=10,
    pady=5
)


# ---------------- PRODUCT TABLE ----------------

table_frame = tk.LabelFrame(
    root,
    text="  Products  ",
    font=("Segoe UI", 12, "bold"),
    bg="#f4f6f8",
    fg="#1f2937",
    padx=15,
    pady=10
)

table_frame.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=(0, 15)
)


columns = (
    "name",
    "category",
    "price",
    "rating",
    "discount"
)

product_table = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings",
    height=8
)

product_table.heading(
    "name",
    text="Product"
)

product_table.heading(
    "category",
    text="Category"
)

product_table.heading(
    "price",
    text="Price (₹)"
)

product_table.heading(
    "rating",
    text="Rating"
)

product_table.heading(
    "discount",
    text="Discount"
)

product_table.column(
    "name",
    width=250
)

product_table.column(
    "category",
    width=150
)

product_table.column(
    "price",
    width=120
)

product_table.column(
    "rating",
    width=100
)

product_table.column(
    "discount",
    width=120
)

product_table.pack(
    fill="both",
    expand=True
)


# ---------------- BEST DEAL FUNCTION ----------------

def update_best_deal():

    if not products_data:
        best_deal_label.config(
            text="🏆 Best Deal: No products available"
        )
        return

    # Calculate a simple deal score
    best_product = products_data[0]

    best_score = (
        best_product["discount"] * 0.5
        + best_product["rating"] * 10
    )

    for product in products_data[1:]:

        score = (
            product["discount"] * 0.5
            + product["rating"] * 10
        )

        if score > best_score:
            best_score = score
            best_product = product

    best_deal_label.config(
        text=(
            f"🏆 Best Deal: {best_product['name']}  |  "
            f"₹{best_product['price']}  |  "
            f"⭐ {best_product['rating']}  |  "
            f"{best_product['discount']}% OFF"
        )
    )


# ---------------- ADD PRODUCT ----------------

def add_product():

    name = product_name_entry.get()
    category = category_combo.get()
    price = price_entry.get()
    rating = rating_entry.get()
    discount = discount_entry.get()

    if name and category and price and rating and discount:

        product = {
            "name": name,
            "category": category,
            "price": int(price),
            "rating": float(rating),
            "discount": float(discount.replace("%", ""))
        }

        products_data.append(product)

        product_table.insert(
            "",
            "end",
            values=(
                product["name"],
                product["category"],
                product["price"],
                product["rating"],
                str(product["discount"]) + "%"
            )
        )

        update_best_deal()

        product_name_entry.delete(
            0,
            "end"
        )

        price_entry.delete(
            0,
            "end"
        )

        rating_entry.delete(
            0,
            "end"
        )

        discount_entry.delete(
            0,
            "end"
        )


add_button = ttk.Button(
    input_frame,
    text="+  Add Product",
    command=add_product
)

add_button.grid(
    row=1,
    column=5,
    padx=15,
    pady=5
)


# ---------------- LOAD PRODUCTS ----------------

backend_products = get_products()

for product in backend_products:

    products_data.append(product)

    product_table.insert(
        "",
        "end",
        values=(
            product["name"],
            product["category"],
            product["price"],
            product["rating"],
            str(product["discount"]) + "%"
        )
    )


# ---------------- SORTING FUNCTION ----------------

def sort_products_gui():

    sort_by = sort_combo.get()
    order = order_combo.get()

    reverse = order == "High → Low"

    sorted_products = sort_products(
        sort_by,
        reverse,
        products_data
    )

    for item in product_table.get_children():
        product_table.delete(item)

    for product in sorted_products:

        product_table.insert(
            "",
            "end",
            values=(
                product["name"],
                product["category"],
                product["price"],
                product["rating"],
                str(product["discount"]) + "%"
            )
        )


# ---------------- SORTING CONTROLS ----------------

control_frame = tk.Frame(
    root,
    bg="#f4f6f8"
)

control_frame.pack(
    fill="x",
    padx=30,
    pady=10
)


tk.Label(
    control_frame,
    text="Sort By:",
    font=("Segoe UI", 10, "bold"),
    bg="#f4f6f8"
).pack(
    side="left",
    padx=(0, 8)
)


sort_combo = ttk.Combobox(
    control_frame,
    values=[
        "Price",
        "Rating",
        "Discount",
        "Product Name"
    ],
    state="readonly",
    width=18
)

sort_combo.pack(
    side="left",
    padx=5
)

sort_combo.set("Price")


tk.Label(
    control_frame,
    text="Order:",
    font=("Segoe UI", 10, "bold"),
    bg="#f4f6f8"
).pack(
    side="left",
    padx=(25, 8)
)


order_combo = ttk.Combobox(
    control_frame,
    values=[
        "Low → High",
        "High → Low"
    ],
    state="readonly",
    width=18
)

order_combo.pack(
    side="left"
)

order_combo.set("Low → High")


sort_button = ttk.Button(
    control_frame,
    text="SORT PRODUCTS",
    command=sort_products_gui
)

sort_button.pack(
    side="right",
    padx=5
)


# ---------------- BEST DEAL SECTION ----------------

best_deal_frame = tk.Frame(
    root,
    bg="#e8f5e9",
    padx=15,
    pady=10
)

best_deal_frame.pack(
    fill="x",
    padx=30,
    pady=(0, 20)
)


best_deal_label = tk.Label(
    best_deal_frame,
    text="🏆 Best Deal: Calculating...",
    font=("Segoe UI", 11, "bold"),
    bg="#e8f5e9",
    fg="#166534"
)

best_deal_label.pack(
    side="left"
)


# Update Best Deal after the label has been created
update_best_deal()


# ---------------- RUN APPLICATION ----------------

root.mainloop()