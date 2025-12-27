"""Performance tests."""

import time
from src.temp_conv import (
    celsius_to_fahrenheit,
    celsius_to_kelvin,
    fahrenheit_to_celsius,
    kelvin_to_celsius,
)


def test_single_function_speed():
    """Test single function performance."""
    iterations = 100000

    start = time.time()
    for i in range(iterations):
        celsius_to_fahrenheit(25)
    elapsed = time.time() - start

    print(f"\n{iterations:,} conversions: {elapsed:.3f}s")
    assert elapsed < 1.0


def test_all_functions_speed():
    """Test all conversion functions."""
    iterations = 10000

    start = time.time()
    for i in range(iterations):
        celsius_to_fahrenheit(25)
        celsius_to_kelvin(25)
        fahrenheit_to_celsius(77)
        kelvin_to_celsius(298)
    elapsed = time.time() - start

    print(f"{iterations * 4:,} operations: {elapsed:.3f}s")
    assert elapsed < 1.0


def test_batch_conversion():
    """Test batch processing performance."""
    temps = list(range(-50, 51))
    iterations = 1000

    start = time.time()
    for _ in range(iterations):
        [celsius_to_fahrenheit(t) for t in temps]
    elapsed = time.time() - start

    print(f"Batch {len(temps) * iterations:,}: {elapsed:.3f}s")
    assert elapsed < 2.0