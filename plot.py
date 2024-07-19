# Measure timing and  plot result

import matplotlib.pyplot as plt
import timeit
import random

def measure_time(source,algorithm, arr, target):
    setup_code = f"from {source} import {algorithm}"
    stmt = f"{algorithm}({arr},{target})"
    execution_time = timeit.timeit(stmt, setup=setup_code, number=1)
    return execution_time*1000

linear_times = []
binary_times = []
input_sizes = [10, 100, 1000, 10000]

for size in input_sizes:
    input_array = list(range(size))
    input_target = random.randint(0, size + size)
    linear_time = measure_time(source="linear_search", algorithm="search", arr=input_array, target=input_target)
    linear_times.append(linear_time)
    binary_time = measure_time(source="binary_search", algorithm="binary_search", arr=input_array, target=input_target)
    binary_times.append(binary_time)
print("linear times", linear_times)
print("binary_times", binary_times)
plt.plot(input_sizes,linear_times,label='linear sort')
plt.plot(input_sizes,binary_times,label='binary sort')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Time Complexity of Searchin Algorithms')
plt.legend()
plt.show()