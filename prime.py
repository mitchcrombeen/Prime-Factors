"""return the prime factors for a given integer"""

def generate_prime_factors(number):
    if not isinstance(number,int):
        raise ValueError("Input must be a whole number")
