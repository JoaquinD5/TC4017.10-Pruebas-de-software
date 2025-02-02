"""
Exercise 1 - Compute Statistics
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
        list_numbers.append(float(line.strip()))
    except ValueError:
        print(f"Ignoring not valid value: {line.strip()}")

# Calculate sum, count and frequency
data_sum = 0
data_count = 0
frequency = {}

for number in list_numbers:
    data_sum += number
    data_count += 1
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

# Caluclate Mean
data_mean = data_sum / data_count

# Calculate Mode
max_frequency = 0
data_mode = None

for data, freq in frequency.items():
    if freq > max_frequency:
        max_frequency = freq
        data_mode = data

# Order the list to calculate the median
for i in range(data_count):
    for j in range(0, data_count - i - 1):
        if list_numbers[j] > list_numbers[j + 1]:
            list_numbers[j], list_numbers[j + 1] = list_numbers[j + 1], list_numbers[j]

center = data_count // 2

if data_count % 2 == 1:
    data_median = list_numbers[center]
else:
    data_median = (list_numbers[center - 1] + list_numbers[center]) / 2

# Calculate standard deviation
sum_quad_dif = 0

for num in list_numbers:
    sum_quad_dif += (num - data_mean)**2

data_std_dev = (sum_quad_dif / (data_count - 1))**0.5

# Calculate variance
data_var = data_std_dev**2

# Results to write on a file
data_output_list = [data_count, data_mean, data_median, data_mode, data_std_dev, data_var]

# Show data in console
print(f"Count: {data_count}")
print(f"Mean: {data_mean}")
print(f"Median: {data_median}")
print(f"Moda: {data_mode}")
print(f"Standar Deviation: {data_std_dev}")
print(f"Variance: {data_var}")

# Register ending time
end_time = time.perf_counter()
execution_time = end_time - start_time

# Create Execution time message
execution_time_str = f"Execution time: {execution_time} seconds"

# Write results on a file
with open('StatisticsResults.txt', 'w', encoding = "utf-8") as archivo:
    for result in data_output_list:
        archivo.write(f"{result}\n")
    archivo.write(execution_time_str)

# Show execution time in console
print(execution_time_str)
