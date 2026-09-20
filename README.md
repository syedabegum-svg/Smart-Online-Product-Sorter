# Smart Online Product Sorter

A Python-based graphical application that demonstrates the practical application of the **Merge Sort algorithm** in a real-world online shopping scenario.

The application allows users to view, search, add, and sort products based on different attributes such as **price, rating, discount, and product name**.

This project was developed as a **Design and Analysis of Algorithms (DAA) case study**.

---

## 📌 Project Overview

Online shopping platforms contain a large number of products with different prices, ratings, categories, and discounts. Finding products according to a user's preference requires efficient data organization and sorting.

The **Smart Online Product Sorter** demonstrates how the **Merge Sort algorithm** can be used to organize product information efficiently.

The application provides a simple graphical interface where users can:

- View available products
- Search for products
- Add new products
- Sort products by different attributes
- Sort products in ascending or descending order
- View a calculated Best Deal

---

## 🎯 Objectives

- To understand the practical application of sorting algorithms.
- To implement **Merge Sort** manually.
- To apply the algorithm to real-world product data.
- To sort products using multiple attributes.
- To provide ascending and descending sorting options.
- To develop an interactive graphical user interface.
- To demonstrate the relationship between algorithm design and real-world applications.

---

## 🧠 DAA Concept

### Merge Sort

The main algorithm used in this project is **Merge Sort**.

Merge Sort is a **divide-and-conquer sorting algorithm**. It works by:

1. Dividing the list into smaller halves.
2. Recursively sorting each half.
3. Merging the sorted halves.

The project implements Merge Sort manually instead of using Python's built-in sorting function.

### Time Complexity

| Case | Complexity |
|---|---|
| Best Case | O(n log n) |
| Average Case | O(n log n) |
| Worst Case | O(n log n) |

### Space Complexity

**O(n)**

---

## ✨ Features

### 🔎 Product Search
Users can search for products using the product name or category.

### ➕ Add Product
Users can enter:

- Product Name
- Category
- Price
- Rating
- Discount

and add the product to the displayed product list.

### ↕️ Product Sorting

Products can be sorted according to:

- Price
- Rating
- Discount
- Product Name

The user can also choose:

- Low → High
- High → Low

### 🏆 Best Deal

The application calculates a simple deal score based on product discount and rating and displays the product with the highest score as the **Best Deal**.

---

## 🖥️ User Interface

The application is developed using **Tkinter** and contains:

- Application header
- Product search section
- Add Product section
- Product table
- Sorting controls
- Best Deal section

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Tkinter | Graphical User Interface |
| CSV | Product data storage |
| Git | Version control |
| GitHub | Source code management |
| VS Code | Development environment |

---

## 📂 Project Structure

```text
Smart-Online-Product-Sorter/
│
├── frontend.py
├── product_logic.py
├── sorting_algorithms.py
├── products.csv
├── app.py
└── README.md
