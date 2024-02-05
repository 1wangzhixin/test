def fibonacci_sequence(max_value):
    if max_value <= 0:
        return [0] if max_value == 0 else []

    fibonacci_list = [0, 1]
    while fibonacci_list[-1] + fibonacci_list[-2] <= max_value:
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])

    return fibonacci_list

# Test cases
print(fibonacci_sequence(10))  # Expected output: [0, 1, 1, 2, 3, 5, 8]
print(fibonacci_sequence(1))   # Expected output: [0, 1, 1]
print(fibonacci_sequence(0))   # Expected output: [0]
print(fibonacci_sequence(-5))  # Expected output: []
