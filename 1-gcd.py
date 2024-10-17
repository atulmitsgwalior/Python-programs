#Programme-1-A Greatest Common Divisor (GCD)
import math

# Define two numbers
a = 5
b = 98
#compute GCD
gcd = math.gcd(a, b)
print(f"The GCD of {a} and {b} is: {gcd}")



#Programme-1-B Greatest Common Divisor (GCD)
def compute_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# Define two numbers
a = 56
b = 98

# Compute GCD
gcd = compute_gcd(a, b)
print(f"The GCD of {a} and {b} is: {gcd}")
