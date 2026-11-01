"""Test my generate_prime_factors function"""
import pytest
from prime import generate_prime_factors

def test_raises_value_error_given_not_an_int():
    """when generate_prime_factors is called with a data type that is;
    not an integer (e.g. a string or float), a ValueError is raised."""
    with pytest.raises(ValueError):
        generate_prime_factors(3.14)

def test_returns_empty_list_given_1():
    """when generate_prime_factors is called with 1, an empty list is returned"""
    assert generate_prime_factors(1) == []

def test_returns_2_given_2():
    """when generate_prime_factors is called with 2, the list [2] is returned"""
    assert generate_prime_factors(2) == [2]
