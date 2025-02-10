"""
Actividad 5.2
Joaquin Diaz    A01281536
"""

import time
import sys
import json

# Request catalogue file name
file_catalogue = input("Type catalogue file name: ")

# Request sales file name
file_sales = input("Type sales file name: ")

# Try to open catalogue file and convert this json file to python dictionary
try:
    with open(file_catalogue, "r", encoding = "utf-8") as f_c:
        data_catalogue = json.load(f_c)
except FileNotFoundError:
    print(f"The file '{file_catalogue}' was not found.")
    sys.exit()

# Try to open sales file and convert this json file to python dictionary
try:
    with open(file_sales, "r", encoding = "utf-8") as f_s:
        data_sales = json.load(f_s)
except FileNotFoundError:
    print(f"The file '{file_sales}' was not found.")
    sys.exit()

# Register initial time
start_time = time.perf_counter()

# Create dictionary to store product name and its price
item_price_dict = {}

for i in data_catalogue:
    title = i.get('title')
    price = i.get('price')
    if title is not None and price is not None:
        item_price_dict[title] = price

# Create dictionary to store quantity saled per product
product_quantity_dict = {}

for i in data_sales:
    product = i.get('Product')
    quantity = i.get('Quantity')
    if product is not None and quantity is not None:
        try:
            product_quantity_dict[product] += quantity
        except KeyError:
            product_quantity_dict[product] = quantity

# Compute total cost for all sales on the sales json file
total_sales = 0

for key, value in product_quantity_dict.items():
    try:
        item_sale = item_price_dict[key] * value
        total_sales += item_sale
    except KeyError:
        print(f"The product '{key}' couldn't be found on the Product List.")

print(f"The total cost for all sales in the file is: {total_sales}")

# Register ending time
end_time = time.perf_counter()
execution_time = end_time - start_time

# Create Execution time message
execution_time_str = f"Execution time: {execution_time} seconds"

# Write results on a file
with open('SaleResults.txt', 'w', encoding = "utf-8") as archivo:
    archivo.write(f"The total cost for all sales in the file is: {total_sales}\n")
    archivo.write(execution_time_str)

# Show execution time in console
print(execution_time_str)
