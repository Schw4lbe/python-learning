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
   see the current inventory from most expensive to cheapest.

2. SORTED
   Use sorted() to create a separate view ordered by product name
   without changing the original inventory order.

3. LIST COMPREHENSION
   Create an admin view containing only products above a chosen
   price or belonging to a chosen category.

4. SET
   Remove duplicate products from the inventory and create a set
   of all unique product categories.

The goal is to build one small inventory workflow where each tool
solves a different part of the admin's actual task.
"""

products: list[tuple] = [
    ("Laptop", 1200, "Electronics"),
    ("Mouse", 25, "Electronics"),
    ("Desk", 300, "Furniture"),
    ("Laptop", 1200, "Electronics"),
    ("Chair", 150, "Furniture"),
]


def init_sorting():
    sort_by_price_descending()
    sorted_by_name()
    delete_duplicates()
    admin_tool_user_select()


def admin_tool_user_select():
    user_input: str = input("category(1) price(2): ")
    while True:
        if user_input == "1":
            select_category()
            break
        elif user_input == "2":
            select_price_range()
            break
        else:
            print("invalid number.")
            continue

    init_sorting()


def delete_duplicates():
    my_set: set[tuple] = set(products)
    print(my_set)
    new_list: list[tuple] = list(my_set)
    print(new_list)


def select_price_range():
    max_price: int = int(input("set max price: "))
    results: list[str] = [prod for prod in products if prod[1] <= max_price]
    for result in results:
        print(result)


def select_category():
    categories: list[str] = set_categories()
    for i, category in enumerate(categories):
        print(i, category)
    user_input: int = int(input("select category: "))

    if user_input > len(categories):
        print("invalid selection.")
        select_category()

    else:
        results: list[str] = [
            prod for prod in products if prod[2] is categories[user_input]
        ]
        for result in results:
            print(result)


def set_categories() -> list[str]:
    results: list[str] = []
    for product in products:
        if product[2] not in results:
            results.append(product[2])
    return results


def sorted_by_name():
    results: list[tuple] = sorted(products, key=lambda product: product[0])
    print("sort by price descending:")
    for result in results:
        print(result)
    print("\n")


def sort_by_price_descending():
    # always returns none and sorst in place so this returns None
    products_sorted: list[tuple] = products.sort(
        key=lambda product: product[1], reverse=True
    )
    print(products_sorted)

    # actually returns propper value because in place mutation
    products.sort(key=lambda product: product[1], reverse=True)
    print("sort by name:")
    for product in products:
        print(product)
    print("\n")


def main():
    init_sorting()


if __name__ == "__main__":
    main()
