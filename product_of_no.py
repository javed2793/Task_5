from functools import reduce

numbers = [4, 3, 9, 5]

# Calculate product
product = reduce(lambda x, y: x * y, numbers)

print(product)