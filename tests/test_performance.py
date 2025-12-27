"""Performance tests"""

import time
from temp_conv import (
    celsius_to_fahrenheit,
    celsius_to_kelvin,
    fahrenheit_to_celsius,
    kelvin_to_celsius,
    fahrenheit_to_kelvin,
    kelvin_to_fahrenheit,
)


def test_single_function_speed():
    """Test single function performance."""
    iterations = 100_000

    start = time.time()
    for _ in range(iterations):
        celsius_to_fahrenheit(25)
    elapsed = time.time() - start

    print(f"\n{iterations:,} conversions: {elapsed:.3f}s")
    assert elapsed < 1.0


def test_all_functions_speed():
    """Test all conversion functions."""
    iterations = 10_000

    start = time.time()
    for _ in range(iterations):
        celsius_to_fahrenheit(25)
        celsius_to_kelvin(25)
        fahrenheit_to_celsius(77)
        kelvin_to_celsius(298)
        fahrenheit_to_kelvin(77)
        kelvin_to_fahrenheit(298)
    elapsed = time.time() - start

    print(f"{iterations * 6:,} operations: {elapsed:.3f}s")
    assert elapsed < 1.2  # slightly relaxed for CI stability


def test_batch_conversion():
    """Test batch processing performance."""
    temps = list(range(-50, 51))  # 101 values
    iterations = 1_000

    start = time.time()
    for _ in range(iterations):
        [celsius_to_fahrenheit(t) for t in temps]
        [fahrenheit_to_kelvin(t) for t in temps]
    elapsed = time.time() - start

    print(f"Batch {len(temps) * iterations * 2:,}: {elapsed:.3f}s")
    assert elapsed < 2.5
