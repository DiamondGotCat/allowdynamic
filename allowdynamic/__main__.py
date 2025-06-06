# allowdynamic
# (c) 2025 DiamondGotCat
# MIT License

from .container import DynamicContainer

print("Example #1, Fibonacci Sequence")

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

fibonacci_array = DynamicContainer(fibonacci)
for i in range(0, 10):
    print(f"#{i} in fibonacci_array: {fibonacci_array[i]}")

print("Example #2, Square Sequence")

def square_sequence(n):
    return n ** 2

square_sequence_dict = DynamicContainer(square_sequence)

for i in range(0, 10):
    print(f"#{i} in square_sequence_dict: {square_sequence_dict[i]}")
