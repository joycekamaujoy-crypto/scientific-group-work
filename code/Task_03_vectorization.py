"""
TASK B: Mathematical Functions and Vectorization
Real-world case: processing a large set of network-latency measurements.
"""
import numpy as np
import timeit

# INPUT: reproducible simulated latency values in milliseconds.
rng = np.random.default_rng(42)
latency_ms = rng.uniform(5, 250, 1_000_000)

def loop_version():
    """Convert each value to seconds and square it using a Python loop."""
    squared = []
    for value in latency_ms:
        seconds = value / 1000.0
        squared.append(seconds ** 2)
    return squared

def vectorized_version():
    """Perform the same calculation on the entire NumPy array."""
    seconds = latency_ms / 1000.0
    return seconds ** 2

# TIMEIT compares execution speed. Loop is measured once; vectorized thrice.
loop_time = timeit.timeit(loop_version, number=1)
vector_time = timeit.timeit(vectorized_version, number=3) / 3
result = vectorized_version()

print("First five squared latency values:", result[:5])
print(f"Python loop time: {loop_time:.4f} s")
print(f"NumPy vectorized time: {vector_time:.4f} s")
print(f"Approximate speed-up: {loop_time / vector_time:.1f}x")
