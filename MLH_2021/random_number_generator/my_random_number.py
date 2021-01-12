# RANDOM NUMBER GENERATOR FROM SCRATCH
# Santiago Garcia Arango
# MHL 2021


# Inspired on linear conguential generator
# https://towardsdatascience.com/how-to-generate-random-variables-from-scratch-no-library-used-4b71eb3c8dc7
# X_(i) = m*X_(i-1) + p
# --> U_(i) = X_(i)/p

import time
import numpy as np
import matplotlib.pyplot as plt


def my_linear_congruential_generator(mult=16803, mod=(2**31) - 1, seed=12345678909, size=100):
    """
    My own pseudo-random generator with multiplier and modulus
    """
    U = np.zeros(size)
    x = (seed * mult + 1) % mod
    U[0] = x / mod

    for i in range(1, size):
        x = (x * mult + 1) % mod
        U[i] = x / mod

    return U


def my_pseudo_uniform(lower=-5, higher=5, seed=123456789, size=100):
    """
    Uniformly random numbers between two given limits
    """

    return lower + (higher - lower) * my_linear_congruential_generator(seed=seed, size=size)


def plot_distribution(vector):
    """
    Plot given vector
    """
    plt.hist(vector, bins=20, edgecolor="black")
    plt.title("MY AWESOME RANDOM PLOT: san99tiago")
    plt.xlim(min(vector), max(vector))
    plt.show()


def sample_picker_based_on_clock(vector):
    """
    Pick item from vector based on system's clock
    """
    t = time.perf_counter()
    seed = int(10**9 * float(str(t - int(t))[0:]))
    # print(t)
    # print(seed)

    # Get the random index number based on changing higher input and seed
    index_float = my_pseudo_uniform(lower=0, higher=len(vector), seed=seed, size=1)
    index = int(index_float)
    # print(index_float)
    # print(index)

    return vector[index]


# TEST RESULTS
# ----------------- Random numbers between 0 and 1 ----------------
vector_1 = my_linear_congruential_generator()
# plot_distribution(vector_1)
random_number_1 = sample_picker_based_on_clock(vector_1)
print("RANDOM NUMBER 1: ", random_number_1)

# ----------------- Random numbers between -5 and 5 ---------------
vector_2 = my_pseudo_uniform(-5, 5)
plot_distribution(vector_2)
random_number_2 = sample_picker_based_on_clock(vector_2)
print("RANDOM NUMBER 2: ", random_number_2)
