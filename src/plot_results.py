#Note: code generated with ChatGPT

import matplotlib.pyplot as plt


def plot_results(results):
    for algorithm, times in results.items():
        sizes = list(times.keys())
        execution_times = list(times.values())
        plt.plot(sizes, execution_times, label=algorithm)

    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Searching Algorithms Performance Comparison")
    plt.legend()
    plt.grid(True)
    plt.show()