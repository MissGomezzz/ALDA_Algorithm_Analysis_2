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
    sizes = [100_000_000, 200_000_000, 300_000_000]

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
        inf_limit = data[0]
        max_limit = data[len(data)-1]
        print (f"Inferior limit of list: {inf_limit} ")
        print (f"Superior limit of list: {max_limit}")
        print (f"Target: {target}")

        for name, algorithm in algorithms.items():

            exec_time = measure_execution_time(algorithm, data, target)
            results[name][size] = exec_time

    return results


if __name__ == "__main__":
    results = run_experiment()
    plot_results(results)