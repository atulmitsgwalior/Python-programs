def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def first_n_primes(n):
    primes = []
    num = 2  # Start checking from the first prime number

    # Continue finding primes until we have n of them
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1

    return primes

# Get the number of prime numbers the user wants
n = int(input("Enter the number of prime numbers you want: "))

# Find the first n prime numbers
prime_numbers = first_n_primes(n)

# Display the prime numbers
print(f"The first {n} prime numbers are: {prime_numbers}")
