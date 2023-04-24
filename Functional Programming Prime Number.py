def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def find_primes(limit):
    return [number for number in range(2, limit+1) if is_prime(number)]

print(find_primes(20))
