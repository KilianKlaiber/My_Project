# Measure timing and  plot result

import matplotlib.pyplot as plt
import timeit
import random


def measure_time(source, algorithm, data):
    setup_code = f"from {source} import {algorithm}"
    stmt = f"{algorithm}({data})"
    execution_time = timeit.timeit(stmt, setup=setup_code, number=1)
    return execution_time * 1000


merge_times = []
binary_times = []
input_sizes = [10, 100]

for size in input_sizes:
    input_array = list(range(size))
    linear_time = measure_time(
        source="kilian2_merge", algorithm="kilian2_merge", data=input_array
    )
    merge_times.append(linear_time)

print("merge times: ", merge_times)
plt.plot(input_sizes, merge_times, label="kilian2_merge sort")
plt.xlabel("Input Size")
plt.ylabel("Execution Time (seconds)")
plt.title("Time Complexity of Searchin Algorithms")
plt.legend()
plt.show()
