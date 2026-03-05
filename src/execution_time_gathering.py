#Note: code generated with ChatGPT

import time

def measure_execution_time(search_function, data, target):
    start = time.perf_counter()
    search_function(data, target)
    end = time.perf_counter()

    return end - start