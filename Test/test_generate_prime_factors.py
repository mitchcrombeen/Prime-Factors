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

def test_returns_3_given_3():
    """when generate_prime_factors is called with 3, the list [3] is returned"""
    assert generate_prime_factors(3) == [3]

def test_returns_2_2_given_4():
    """when generate_prime_factors is called with 4, the list [2, 2] is returned."""
    assert generate_prime_factors(4) == [2,2]

def test_returns_2_3_given_6():
    """when generate_prime_factors is called with 6, the list [2, 3] is returned"""
    assert generate_prime_factors(6) == [2,3]

def test_returns_2_2_2_given_8():
    """when generate_prime_factors is called with 8, the list [2, 2, 2] is returned"""
    assert generate_prime_factors(8) == [2,2,2]

def test_returns_3_3_given_9():
    """when generate_prime_factors is called with 9, the list [3, 3] is returned"""
    assert generate_prime_factors(9) == [3,3]
