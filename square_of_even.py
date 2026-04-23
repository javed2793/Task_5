numbers = [10, 22, 23, 45, 55, 66, 37, 8]

# List comprehension with lambda
squares = [x**2 for x in numbers if (lambda n: n % 2 == 0)(x)]

print(squares)