#Note: code generated with ChatGPT

import random

def generate_sorted_data(size):
    # ya viene ordenado, O(1)
    return list(range(size))

def generate_target(data):
    return random.randint(0, len(data) - 1)