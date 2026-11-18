"""MODIFIED VERSION of Task B: process 200,000 rather than 1,000,000 samples."""
import numpy as np
import timeit
rng = np.random.default_rng(42)
SAMPLE_COUNT = 200_000  # CHANGED PARAMETER: was 1_000_000
latency_ms = rng.uniform(5, 250, SAMPLE_COUNT)
def loop_version():
    return [(value / 1000.0) ** 2 for value in latency_ms]
def vectorized_version():
    return (latency_ms / 1000.0) ** 2
loop_time = timeit.timeit(loop_version, number=1)
vector_time = timeit.timeit(vectorized_version, number=3) / 3
print("MODIFIED SAMPLE COUNT:", SAMPLE_COUNT)
print("First five:", vectorized_version()[:5])
print(f"Loop: {loop_time:.4f}s; vectorized: {vector_time:.4f}s")
