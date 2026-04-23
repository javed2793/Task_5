n = 10

fib = lambda n: [0, 1] if n == 2 else None

series = [0, 1]
for i in range(2, n):
    series.append(series[-1] + series[-2])

print(series[:n])