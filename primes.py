"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    number = 2
    
    if number_of_primes < 1:
        raise ValueError("The size of the list must be at least 1")
        
    while len(list) != number_of_primes:
        isPrime = True
        for i in range(2, number):
            if number % i == 0 and number != 2:
                isPrime = False
                break
        if isPrime:
            list.append(number)
        number += 1
            
    return list