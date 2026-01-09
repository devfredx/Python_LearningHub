r1 = range(10)
print(list(r1))

r2 = range(5, 15)
print(list(r2))

r3 = range(0, 20, 2)
print(list(r3))

r4 = range(10, 0, -1)
print(list(r4))

for i in range(5):
    print(i)

for i in range(100, 105):
    print(i)

for i in range(0, 50, 10):
    print(i)

numbers = range(1, 100, 5)
print(21 in numbers)
print(22 in numbers)

print(numbers[0])
print(numbers[5])
print(numbers[-1])

print(len(numbers))

import sys
big_range = range(1000000)
print(sys.getsizeof(big_range))

l1 = list(range(10))
l2 = list(range(5, 10))
l3 = list(range(0, 30, 5))

print(l1)
print(l2)
print(l3)