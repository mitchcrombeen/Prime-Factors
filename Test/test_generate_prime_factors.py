"""Test my generate_prime_factors function"""
import pytest
from prime import generate_prime_factors

def test_raises_value_error_given_not_an_int():
    """when generate_prime_factors is called with a data type that is;
    not an integer (e.g. a string or float), a ValueError is raised."""
    with pytest.raises(ValueError):
        generate_prime_factors(3.14)
