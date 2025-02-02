"""
Exercise 3 - Count Words
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
list_words = []
for line in data_read.split("\n"):
    try:
        list_words.append(line.strip())
    except ValueError:
        print(f"Ignoring not valid value: {line.strip()}")

# Create dictionary with frequency of each word on the file
frequency = {}

for word in list_words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# Order dictionary from largest to smallest frequency
sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

# Register ending time
end_time = time.perf_counter()
execution_time = end_time - start_time

# Create Execution time message
execution_time_str = f"Execution time: {execution_time} seconds"

# Write results on a file and show in console
with open('WordCountResults.txt', 'w', encoding = "utf-8") as archivo:
    for word, qty in sorted_frequency:
        message = f"{word} {qty}"
        print(message)
        archivo.write(f"{message}\n")
    archivo.write(execution_time_str)

# Show execution time in console
print(execution_time_str)
