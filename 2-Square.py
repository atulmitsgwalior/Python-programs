
#Prog-2 Find the Square root of number (Newton's Methods)


def newton_sqrt(number, tolerance=1e-10):
    if number < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    elif number == 0:
        return 0

    # Initial guess (can be any positive number, but let's start with half of the input)
    guess = number / 2.0
    
    # Iterate until the difference between guesses is within the desired tolerance
    while True:
        next_guess = 0.5 * (guess + number / guess)
        if abs(next_guess - guess) < tolerance:
            return next_guess
        guess = next_guess

# Test the function
number = 25
sqrt = newton_sqrt(number)
print(f"The square root of {number} is approximately: {sqrt}")
