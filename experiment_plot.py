import matplotlib.pyplot as plt

# Example data for multiple curves
input_sizes = [10, 100, 1000, 10000]
merge_times = [0.001, 0.01, 0.1, 1]  # Example times for merge sort
quick_times = [0.002, 0.02, 0.2, 2]  # Example times for quick sort
bubble_times = [0.1, 1, 10, 100]     # Example times for bubble sort

# Plot the first curve
plt.plot(input_sizes, merge_times, label="Merge Sort")

# Plot the second curve
plt.plot(input_sizes, quick_times, label="Quick Sort")

# Plot the third curve
plt.plot(input_sizes, bubble_times, label="Bubble Sort")

# Add labels and title
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Sorting Algorithm Performance')

# Add a legend to distinguish between the curves
plt.legend()

# Display the plot
plt.show()
