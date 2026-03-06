#Note: code generated with ChatGPT

from src.searching import (
    linear_search,
    binary_search,
    jump_search,
    interpolation_search,
    exponential_search
)

from src.data_generator import (
    generate_sorted_data,
    generate_target
)

from src.execution_time_gathering import measure_execution_time

from src.plot_results import plot_results


def run_experiment():
    sizes = [100, 500, 1000, 5000, 10000]

    algorithms = {
        "Linear Search": linear_search,
        "Binary Search": binary_search,
        "Jump Search": jump_search,
        "Interpolation Search": interpolation_search,
        "Exponential Search": exponential_search
    }

    results = {name: {} for name in algorithms}

    for size in sizes:
        print(f"Testing size {size}")

        data = generate_sorted_data(size)
        target = generate_target(data)

        for name, algorithm in algorithms.items():

            exec_time = measure_execution_time(algorithm, data, target)
            results[name][size] = exec_time

    return results


if __name__ == "__main__":
    results = run_experiment()
    plot_results(results)