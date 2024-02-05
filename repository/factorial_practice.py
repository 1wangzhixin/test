def calculate_factorial(number):
    if number < 0:
        return "Factorial is not defined for negative numbers"
    
    result = 1
    for i in range(1, number + 1):
        result *= i

    return result

# Test cases
print(calculate_factorial(5))  # Expected output: 120
print(calculate_factorial(0))  # Expected output: 1
print(calculate_factorial(3))  # Expected output: 6
print(calculate_factorial(-1))  # Expected output: "Factorial is not defined for negative numbers"
