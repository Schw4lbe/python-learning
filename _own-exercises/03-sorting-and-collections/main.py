"""
3. Sorting & Collections

List sort()
sorted()
List Comprehension
Sets

https://www.w3schools.com/python/ref_list_sort.asp
https://www.w3schools.com/python/ref_func_sorted.asp
https://www.w3schools.com/python/python_lists_comprehension.asp
https://www.w3schools.com/python/python_sets.asp

Mini Project: E-Commerce Inventory Dashboard

Scenario:
You manage the product inventory for a small online shop.
An admin needs to inspect the inventory, create different views of
the products, and get a quick summary before updating the shop.

products = [
    ("Laptop", 1200, "Electronics"),
    ("Mouse", 25, "Electronics"),
    ("Desk", 300, "Furniture"),
    ("Laptop", 1200, "Electronics"),
    ("Chair", 150, "Furniture")
]

1. SORT
   Sort the inventory in place by product price so the admin can
   see the current inventory from cheapest to most expensive.

2. SORTED
   Use sorted() to create a separate view ordered by product name
   without changing the original inventory order.

3. LIST COMPREHENSION
   Create an admin view containing only products above a chosen
   price or belonging to a chosen category.

4. SET
   Remove duplicate products from the inventory and create a set
   of all unique product categories.

5. INVENTORY SUMMARY
   Combine the results to display a simple dashboard showing:
   - cleaned product count
   - available categories
   - most/least expensive products
   - products matching the admin's filter

The goal is to build one small inventory workflow where each tool
solves a different part of the admin's actual task.
"""


def main():
    print("Hello from 03-sorting-and-collections!")


if __name__ == "__main__":
    main()
