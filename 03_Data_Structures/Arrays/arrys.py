import array as arr

numbers = arr.array('i', [10, 20, 30, 40, 50])
floats = arr.array('d', [1.1, 2.2, 3.3])

print(numbers[0])
print(numbers[2])
print(numbers[-1])

numbers.append(60)
numbers.insert(1, 15)
numbers.extend([70, 80, 90])

numbers.remove(30)
numbers.pop()
numbers.pop(2)

print(len(numbers))
print(numbers.index(40))
print(numbers.typecode)

numbers[0] = 100

for x in numbers:
    print(x)

subset = numbers[1:4]

numbers.reverse()

print(numbers)
print(floats)