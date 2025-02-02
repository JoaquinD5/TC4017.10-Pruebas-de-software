"""
Exercise 2 - Convert Numbers
Joaquin Diaz    A01281536
"""

import time
import sys

# Request file name
file_name = input("Type file name: ")

# Try to open the file
try:
    with open(file_name, encoding = "utf-8") as f:
        data_read = f.read()
except FileNotFoundError:
    print(f"The file '{file_name}' was not found.")
    sys.exit()

# Register initial time
start_time = time.perf_counter()

# Create a list of numbers with the data read
list_numbers = []
for line in data_read.split("\n"):
    try:
        list_numbers.append(int(line.strip()))
    except ValueError:
        print(f"Ignoring not valid value: {line.strip()}")

# Convert the decimal number into binary
binary_list = []

for number in list_numbers:
    binary_number = []

    if number < 0:
        number = 65536 + number

    while number > 0:
        binary_number.append(str(number % 2))
        number = number // 2

    binary_number.reverse()

    binary_list.append(''.join(binary_number))

# Convert the decimal number into hexadecimal
hexadecimal_list = []

hex_dictionary = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
}

for number in list_numbers:
    hexadecimal_number = []

    if number < 0:
        number = 65536 + number + 1

    while number > 0:
        value = number % 16
        hexadecimal_number.append(hex_dictionary[value])
        number = number // 16

    hexadecimal_number.reverse()

    hexadecimal_list.append(''.join(hexadecimal_number))

# Register ending time
end_time = time.perf_counter()
execution_time = end_time - start_time

# Create Execution time message
execution_time_str = f"Execution time: {execution_time} seconds"

# Write results on a file and show in console
with open('ConvertionResults.txt', 'w', encoding = "utf-8") as archivo:
    for i, num in enumerate(list_numbers):
        message = (f"{num} in binary is {binary_list[i]} "
            f"and in hexadecimal is {hexadecimal_list[i]}")
        print(message)
        archivo.write(f"{message}\n")
    archivo.write(execution_time_str)

# Show execution time in console
print(execution_time_str)
