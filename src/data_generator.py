#Note: code generated with ChatGPT

import random

def generate_sorted_data(size):
    data = random.sample(range(size * 3), size)
    data.sort()
    return data


def generate_unsorted_data(size):
    return random.sample(range(size * 3), size)


def generate_target(data, case="random"):
    if case == "best":
        return data[0]
    elif case == "worst":
        return -1  # value not in array
    else:
        return random.choice(data)